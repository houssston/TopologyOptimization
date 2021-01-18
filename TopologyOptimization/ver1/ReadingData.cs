using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.IO;
using System.Diagnostics;
using System.Threading;
using System.Windows.Forms;


namespace ver1
{
    class DataCSV
    {
        private double Width;
        private double Height;
        private double Grid1;

        public double dataWidth
        {
            get { return Width; }
            set { Width = value; }
        }
        public double dataHeight
        {
            get { return Height; }
            set { Height = value; }
        }
        public double dataGrid1
        {
            get { return Grid1; }
            set { Grid1 = value; }
        }
    }   

    class ReadingData
    {
        class Parameters
        {
            public double X { get; set; }
            public double Y { get; set; }
            public double Z { get; set; }
            public double XY { get; set; }
            public double YZ { get; set; }
            public double XZ { get; set; }

            public Parameters(double x, double y, double z, double xy, double yz, double xz)
            {
                this.X = x;
                this.Y = y;
                this.Z = z;
                this.XY = xy;
                this.YZ = yz;
                this.XZ = xz;
            }
        }

        public void ReadingDictionary(PathCSV pathCSV, DataCSV dataCSV)
        {
            double count;
            double nodeColum;
            double nodeRow;
            double maxStrain = 0;
            double avgStrain = 0;
            double minStress = 0;
            double avgStress = 0;
            nodeColum = Math.Round(dataCSV.dataHeight / dataCSV.dataGrid1);
            nodeRow = Math.Round(dataCSV.dataWidth / dataCSV.dataGrid1);


            for (int i = 1; i <= 4; )
            {
                Dictionary<int, Parameters> StrainDictionary = new Dictionary<int, Parameters>();
                StrainDictionary = File.ReadLines(Path.Combine(pathCSV.prmFolderСalculated, "StrainS" + i + ".csv")).Select(line => line.Split(';'))
                    .Where(split => split[0] != "Element").ToDictionary(split => int.Parse(split[0]),
                       split => new Parameters(double.Parse(split[1]), double.Parse(split[2]), double.Parse(split[3]), double.Parse(split[4]), double.Parse(split[5]), double.Parse(split[6])));
                count = StrainDictionary.Count();
                Dictionary<int, double> ShearStrain = new Dictionary<int, double>();
                ShearStrain = StrainDictionary.Where(v => (v.Key <= nodeColum * nodeRow) || (v.Key >= count - nodeColum * nodeRow)).ToDictionary(k => k.Key, v => Math.Abs(v.Value.XY));
                maxStrain = maxStrain + ShearStrain.Max(x => x.Value);
                i++;
            }
            avgStrain = maxStrain / 4;
            for (int i = 1; i <= 4;)
            {
                Dictionary<int, Parameters> AllStressDictionary = new Dictionary<int, Parameters>();
                AllStressDictionary = File.ReadLines(Path.Combine(pathCSV.prmFolderСalculated, "StressS" + i + ".csv")).Select(line => line.Split(';'))
                    .Where(split => split[0] != "Element").ToDictionary(split => int.Parse(split[0]),
                        split => new Parameters(double.Parse(split[1]), double.Parse(split[2]), double.Parse(split[3]), double.Parse(split[4]), double.Parse(split[5]), double.Parse(split[6])));
                count = AllStressDictionary.Count();
                Dictionary<int, double> StressDictionary = new Dictionary<int, double>();
                StressDictionary = AllStressDictionary.Where(v => (v.Value.X >= 0 && v.Key <= nodeColum * nodeRow) || (v.Value.X >= 0 && v.Key >= count - nodeColum * nodeRow)).ToDictionary(k => k.Key, v => v.Value.X);
                minStress = minStress + StressDictionary.Min(v => v.Value);
                i++;
            }
            avgStress = minStress / 4;
            Dictionary<double, double> PeeqDictionary = new Dictionary<double, double>();
            PeeqDictionary = File.ReadLines(Path.Combine(pathCSV.prmFolderСalculated, "PEEQ.csv")).Select(line => line.Split(';'))
                .ToDictionary(split => double.Parse(split[0]), split => double.Parse(split[1]));
            var minPEEQ = PeeqDictionary.Min(x => x.Value);


            string delimiter = ";";
            string[][] table = { new string[] { pathCSV.prmFolderСalculated.Substring(pathCSV.prmFolderСalculated.LastIndexOf('\\') + 1), Math.Round(avgStress, 3).ToString(), Math.Round(avgStrain, 3).ToString() }, };
            string[] csvLines = table.Select(x => string.Join(delimiter, x)).ToArray();
            File.AppendAllLines(Path.Combine(pathCSV.prmPathDesk, pathCSV.prmFolder, "ouput.csv"), csvLines, Encoding.GetEncoding(1251));   
        }
    }
}
   


