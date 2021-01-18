using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.IO;
using System.Diagnostics;
using System.Threading;

namespace ver1
{
    class Script
    {
        public void СhangeInScript(PrmСalculation prmСalculation, PrmModel prmModel, PrmPath prmPath)
        {
            Directory.CreateDirectory(prmPath.prmFolderСalculated);
            
            string prm = string.Empty;

            using (System.IO.StreamReader reader = System.IO.File.OpenText(Path.Combine(prmPath.prmPathDesk, prmPath.prmMacrosName)))
            {
                prm = reader.ReadToEnd();
            }
            double Width = prmModel.prmWidth / 2;
            double Height = prmModel.prmHeight / 2;
            double Velocity = prmСalculation.prmMoving / 0.05;
           
           
            prm = Regex.Replace(prm, "@Width", prmModel.prmWidth.ToString());
            prm = Regex.Replace(prm, "@Height", prmModel.prmHeight.ToString());
            prm = Regex.Replace(prm, "@RPwidth", Width.ToString());
            prm = Regex.Replace(prm, "@RPheight", Height.ToString());            
            prm = Regex.Replace(prm, "@MassDensity", prmСalculation.prmDensity.ToString());
            prm = Regex.Replace(prm, "@YoungsModulus", prmСalculation.prmElasticYM.ToString());
            prm = Regex.Replace(prm, "@PoissonsRatio", prmСalculation.prmElasticPR.ToString());
            prm = Regex.Replace(prm, "@Grid1", prmСalculation.prmGrid1.ToString());
            prm = Regex.Replace(prm, "@Grid2", prmСalculation.prmGrid2.ToString());
            prm = Regex.Replace(prm, "@Friction", prmСalculation.prmFriction.ToString());
            prm = Regex.Replace(prm, "@Moving", Velocity.ToString());            
            prm = Regex.Replace(prm, "@Material", prmСalculation.prmMaterial);
            prm = Regex.Replace(prm, "@PathModel", Path.Combine(prmPath.prmFolderСalculated, "Model.IGS").ToString()).Replace('\\', '/');
            prm = Regex.Replace(prm, "@PathLower", Path.Combine(prmPath.prmFolderСalculated, "Lower.IGS").ToString()).Replace('\\', '/');
            prm = Regex.Replace(prm, "@PathUpper", Path.Combine(prmPath.prmFolderСalculated, "Upper.IGS").ToString()).Replace('\\', '/');
            prm = Regex.Replace(prm, "@PathTool", Path.Combine(prmPath.prmFolderСalculated, "Tool.IGS").ToString()).Replace('\\', '/');
            prm = Regex.Replace(prm, "@PathPlateLower", Path.Combine(prmPath.prmFolderСalculated, "LowerPlate.IGS").ToString()).Replace('\\', '/');
            prm = Regex.Replace(prm, "@PathPlateUpper", Path.Combine(prmPath.prmFolderСalculated, "UpperPlate.IGS").ToString()).Replace('\\', '/');
            prm = Regex.Replace(prm, "@PathSaveCAE", Path.Combine(prmPath.prmFolderСalculated, "cae").ToString()).Replace('\\', '/');

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(Path.Combine(prmPath.prmFolderСalculated, prmPath.prmMacrosName)))
            {
                file.Write(prm);
            }

            using (System.IO.StreamReader reader = System.IO.File.OpenText(Path.Combine(prmPath.prmPathDesk, prmPath.prmExtractName)))
            {
                prm = reader.ReadToEnd();
            }          
            
            prm = Regex.Replace(prm, "@Path", Path.Combine(prmPath.prmFolderСalculated, "Job-1.odb").ToString().Replace('\\', '/'));

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(Path.Combine(prmPath.prmFolderСalculated, prmPath.prmExtractName)))
            {
                file.Write(prm);
            }
        }
        public void СhangeMoving(PrmСalculation prmСalculation, PrmModel prmModel, PrmPath prmPath)
        {
            System.Threading.Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
            double[] Coord = File.ReadAllLines(Path.Combine(prmPath.prmPathDesk, prmPath.prmFolder, "TempCalculat", "Coordinates.csv")).Select(n => double.Parse(n)).ToArray();
            double maxCoord = Coord.Max();
            double minCoord = Coord.Min();
            double UpperPlateRP = maxCoord + 0.4;
            double LowerPlateRP = minCoord - 0.4;

            double PlateMovingUpper = ((maxCoord + 0.4) - (prmModel.prmHeight / 2 + ((prmModel.prmHeight - prmСalculation.prmMoving * 2) / 2) - ((prmModel.prmHeight - prmСalculation.prmMoving * 2) * 5 / 100))) / 0.05;

            double PlateMovingLower = ((prmModel.prmHeight / 2 - (((prmModel.prmHeight - prmСalculation.prmMoving * 2) / 2) - (prmModel.prmHeight - prmСalculation.prmMoving * 2) * 5 / 100)) - (minCoord - 0.4)) / 0.05;
          


            string prm = string.Empty;

            using (System.IO.StreamReader reader = System.IO.File.OpenText(Path.Combine(prmPath.prmFolderСalculated, prmPath.prmMacrosName)))
            {
                prm = reader.ReadToEnd();
            }

            prm = Regex.Replace(prm, "@PlateMovingUpper", PlateMovingUpper.ToString());
            prm = Regex.Replace(prm, "@PlateMovingLower", PlateMovingLower.ToString());
            prm = Regex.Replace(prm, "@UpperPlateRP", UpperPlateRP.ToString());
            prm = Regex.Replace(prm, "@LowerPlateRP", LowerPlateRP.ToString());

            using (System.IO.StreamWriter file = new System.IO.StreamWriter(Path.Combine(prmPath.prmFolderСalculated, prmPath.prmMacrosName)))
            {
                file.Write(prm);
            }

        }
    }
}
