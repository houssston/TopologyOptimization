using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;
using System.Globalization;
using System.Threading;
using System.IO;
using System.Text.RegularExpressions;

namespace ver1
{
    public partial class program1 : Form
    {
        string PathDesk = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
        string pathMaterial = Path.Combine(Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location), "Material");
        string Folder = ("Calculation " + DateTime.Now.ToShortDateString() + "[" + DateTime.Now.ToLongTimeString() + "]").Replace(":", ".");
        string FolderСalculated;
        string MacrosName = "abaqusMacros.py";
        string ExtractName = "extract.py";
        double Length;
        double Width;
        double Height;
        double Angle;
        double Friction;
        double[] arrLength;
        double[] arrWidth;
        double[] arrHeight;
        double[] arrAngle;
        double[] arrFriction;

        public program1()
        {
            InitializeComponent();
        }
        private void TextBox_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar != 8 && e.KeyChar != 46 && e.KeyChar != 45 && e.KeyChar != 101 && (e.KeyChar < 48 || e.KeyChar > 57))
            {
                e.Handled = true;
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            bool someEmpty = true;
            foreach (TextBox textBox in groupBox.Controls.OfType<TextBox>())
            {
                if (string.IsNullOrEmpty(textBox.Text) || dataGridLength.Rows.Count == 1 || dataGridWidth.Rows.Count == 1 || dataGridHeight.Rows.Count == 1 || dataGridAngle.Rows.Count == 1 || dataGridMaterial.Rows.Count == 0)
                {
                    someEmpty = true;
                    MessageBox.Show("Заполните все поля");
                    return;
                }
                else
                    someEmpty = false;
            }
            if (!someEmpty)
                Program();

        }

        public void Program()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
            arrLength = new double[dataGridLength.RowCount];
            arrWidth = new double[dataGridWidth.RowCount];
            arrHeight = new double[dataGridHeight.RowCount];
            arrAngle = new double[dataGridAngle.RowCount];
            arrFriction = new double[dataGridFriction.RowCount];
            Directory.CreateDirectory(Folder);

            for (int l = 0; l < dataGridLength.RowCount - 1; l++)
            {
                for (int w = 0; w < dataGridWidth.RowCount - 1; w++)
                {
                    for (int h = 0; h < dataGridHeight.RowCount - 1; h++)
                    {
                        for (int a = 0; a < dataGridAngle.RowCount - 1; a++)
                        {
                            for (int f = 0; f < dataGridFriction.RowCount - 1; f++)
                            {
                                arrFriction[f] = Convert.ToDouble(dataGridFriction[0, f].Value);
                                arrLength[l] = Convert.ToDouble(dataGridLength[0, l].Value);
                                arrWidth[w] = Convert.ToDouble(dataGridWidth[0, w].Value);
                                arrHeight[h] = Convert.ToDouble(dataGridHeight[0, h].Value);
                                arrAngle[a] = Convert.ToDouble(dataGridAngle[0, a].Value);
                                Length = arrLength[l];
                                Width = arrWidth[w];
                                Height = arrHeight[h];
                                Angle = arrAngle[a];
                                Friction = arrFriction[f];
                                //TempCalculat();
                                //CheckSolid();
                                //Parameters();
                                //CheckSolid();
                                //StartAbaqus();
                                //Dictionary();
                            }
                        }
                    }
                }
            }
            //Results();
            MessageBox.Show("Сompleted");
        }

        public void Parameters()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            double Density = double.Parse(density.Text, NumberStyles.Any);
            double ElasticYM = double.Parse(elasticYM.Text, NumberStyles.Any);
            double ElasticPR = Convert.ToDouble(elasticPR.Text);
            double Grid1 = Convert.ToDouble(grid1.Text);
            double Grid2 = Convert.ToDouble(grid2.Text);
            double Moving = Convert.ToDouble(moving.Text);
            string dataGridColumn1 = string.Empty;
            string dataGridColumn2 = string.Empty;
            string Material = string.Empty;
            FolderСalculated = Path.Combine(PathDesk, Folder, "Length " + Length + " Width" + Width + " Height" + Height + " Angle" + Angle + " Friction" + Friction);

            for (int i = 0; i < dataGridMaterial.RowCount - 1; i++)
            {
                dataGridColumn1 = dataGridMaterial[0, i].Value.ToString();
                dataGridColumn2 = dataGridMaterial[1, i].Value.ToString();
                Material += "(" + dataGridColumn1 + "," + dataGridColumn2 + ")" + ",";
            }
            Material = Material.Remove(Material.LastIndexOf(','), 1);

            PrmModel prmModel = new PrmModel();
            prmModel.prmLength = Length;
            prmModel.prmWidth = Width;
            prmModel.prmHeight = Height;
            prmModel.prmAngle = Angle;

            PrmСalculation prmСalculation = new PrmСalculation();
            prmСalculation.prmDensity = Density;
            prmСalculation.prmElasticYM = ElasticYM;
            prmСalculation.prmElasticPR = ElasticPR;
            prmСalculation.prmGrid1 = Grid1;
            prmСalculation.prmGrid2 = Grid2;
            prmСalculation.prmFriction = Friction;
            prmСalculation.prmMoving = Moving;
            prmСalculation.prmMaterial = Material;

            PrmPath prmPath = new PrmPath();
            prmPath.prmPathDesk = PathDesk;
            prmPath.prmFolder = Folder;
            prmPath.prmMacrosName = MacrosName;
            prmPath.prmExtractName = ExtractName;
            prmPath.prmFolderСalculated = FolderСalculated;


            var chScript = new Script();
            chScript.СhangeInScript(prmСalculation, prmModel, prmPath);
            chScript.СhangeMoving(prmСalculation, prmModel, prmPath);

            var CAD = new Solid(prmModel, prmСalculation);
            CAD.CreateModel(prmPath);
            CAD.CreateUpperPunch(prmModel, prmPath);
            CAD.CreateLowerPunch(prmModel, prmPath);
            CAD.CreateTool(prmModel, prmPath);
            CAD.CreateLowerPlate(prmModel, prmPath);
            CAD.CreateUpperPlate(prmModel, prmPath);
        }

        public void CheckSolid()
        {
            Process[] processes = Process.GetProcessesByName("SLDWORKS");
            foreach (Process process in processes)
            {
                process.CloseMainWindow();
                process.Kill();
            }
        }

        public void StartAbaqus()
        {
            string cmd = "abaqus cae noGUI=";// script/noGUI
            string SystemDirectory = Environment.SystemDirectory;
            string Arguments = SystemDirectory.Remove(SystemDirectory.IndexOf(':'));

            PathAbaqus pathAbaqus = new PathAbaqus();
            pathAbaqus.prmCmd = cmd;
            pathAbaqus.prmSystemDirectory = SystemDirectory;
            pathAbaqus.prmArguments = Arguments;
            pathAbaqus.prmPathDesk = PathDesk;
            pathAbaqus.prmMacrosName = MacrosName;
            pathAbaqus.prmExtractName = ExtractName;
            pathAbaqus.prmFolderСalculated = FolderСalculated;

            var abaqus = new Abaqus();
            abaqus.RunMacros(pathAbaqus);
            abaqus.RunExtract(pathAbaqus);

        }

        public void Dictionary()
        {
            double Grid1 = Convert.ToDouble(grid1.Text);
            PathCSV pathCSV = new PathCSV();
            pathCSV.prmPathDesk = PathDesk;
            pathCSV.prmFolder = Folder;
            pathCSV.prmFolderСalculated = FolderСalculated;

            DataCSV dataCSV = new DataCSV();
            dataCSV.dataWidth = Width;
            dataCSV.dataHeight = Height;
            dataCSV.dataGrid1 = Grid1;
            var data = new ReadingData();
            data.ReadingDictionary(pathCSV, dataCSV);
        }

        public void TempCalculat()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
            double Density = double.Parse(density.Text, NumberStyles.Any);
            double ElasticYM = double.Parse(elasticYM.Text, NumberStyles.Any);
            double ElasticPR = Convert.ToDouble(elasticPR.Text);
            double Grid1 = Convert.ToDouble(grid1.Text);
            double Grid2 = Convert.ToDouble(grid2.Text);
            double Moving = Convert.ToDouble(moving.Text);
            string dataGridColumn1 = string.Empty;
            string dataGridColumn2 = string.Empty;
            string Material = string.Empty;
            string cmd = "abaqus cae noGUI=";// script/noGUI
            string SystemDirectory = Environment.SystemDirectory;
            string Arguments = SystemDirectory.Remove(SystemDirectory.IndexOf(':'));
            for (int i = 0; i < dataGridMaterial.RowCount - 1; i++)
            {
                dataGridColumn1 = dataGridMaterial[0, i].Value.ToString();
                dataGridColumn2 = dataGridMaterial[1, i].Value.ToString();
                Material += "(" + dataGridColumn1 + "," + dataGridColumn2 + ")" + ",";
            }
            Material = Material.Remove(Material.LastIndexOf(','), 1);
            string MacrosName = "TempAbaqusMacros.py";
            string ExtractName = "TempExtract.py";
            FolderСalculated = Path.Combine(PathDesk, Folder, "TempCalculat");
            //Directory.CreateDirectory(FolderСalculated);

            PrmModel prmModel = new PrmModel();
            prmModel.prmLength = Length;
            prmModel.prmWidth = Width;
            prmModel.prmHeight = Height;
            prmModel.prmAngle = Angle;

            PrmСalculation prmСalculation = new PrmСalculation();
            prmСalculation.prmDensity = Density;
            prmСalculation.prmElasticYM = ElasticYM;
            prmСalculation.prmElasticPR = ElasticPR;
            prmСalculation.prmGrid1 = Grid1;
            prmСalculation.prmGrid2 = Grid2;
            prmСalculation.prmFriction = Friction;
            prmСalculation.prmMoving = Moving;
            prmСalculation.prmMaterial = Material;

            PrmPath prmPath = new PrmPath();
            prmPath.prmMacrosName = MacrosName;
            prmPath.prmExtractName = ExtractName;
            prmPath.prmFolderСalculated = FolderСalculated;
            prmPath.prmPathDesk = PathDesk;

            PathAbaqus pathAbaqus = new PathAbaqus();
            pathAbaqus.prmCmd = cmd;
            pathAbaqus.prmSystemDirectory = SystemDirectory;
            pathAbaqus.prmArguments = Arguments;
            pathAbaqus.prmPathDesk = PathDesk;
            pathAbaqus.prmMacrosName = MacrosName;
            pathAbaqus.prmExtractName = ExtractName;
            pathAbaqus.prmFolderСalculated = FolderСalculated;

            var chScript = new Script();
            chScript.СhangeInScript(prmСalculation, prmModel, prmPath);

            CheckSolid();

            var CAD = new Solid(prmModel, prmСalculation);
            CAD.CreateModel(prmPath);
            CAD.CreateUpperPunch(prmModel, prmPath);
            CAD.CreateLowerPunch(prmModel, prmPath);
            CAD.CreateTool(prmModel, prmPath);

            CheckSolid();

            var abaqus = new Abaqus();
            abaqus.RunMacros(pathAbaqus);
            abaqus.RunExtract(pathAbaqus);

        }

        public void Results()
        {
            //string filename = Path.Combine(@"D:\MyProject(31.11.18)\ver1\bin\Debug\Temp 08.12.2018[14.08.10]", "ouput.csv");
            //List<string[]> rows = File.ReadAllLines(filename).Select(x => x.Split(';')).ToList();
            //DataTable dataTable = new DataTable();
            //dataTable.Columns.Add("min. Tensile stress");
            //dataTable.Columns.Add("max. Shear strain");
            //dataTable.Columns.Add("Parameters");
            //dataTable.Columns.Add("1");
            //rows.ForEach(x => { dataTable.Rows.Add(x); });
            //dataGridView1.DataSource = dataTable;



        }

        private void dataGridView1_EditingControlShowing(object sender, DataGridViewEditingControlShowingEventArgs e)
        {
            e.Control.KeyPress += new KeyPressEventHandler(Cell_KeyPress);
        }

        private void Cell_KeyPress(object Sender, KeyPressEventArgs e)
        {
            if (!Char.IsDigit(e.KeyChar) && e.KeyChar != 8 && e.KeyChar != 46)
                e.KeyChar = Convert.ToChar("\0");
        }

        private void comboBox1_DropDownClosed(object sender, EventArgs e)
        {
            string comboText = comboBox1.Text;
            string csvFile = Path.Combine(pathMaterial, comboText + ".csv");
            List<string[]> rows = File.ReadAllLines(csvFile).Select(x => x.Split(';')).ToList();
            DataTable dataTable = new DataTable();
            dataTable.Columns.Add("Yield Stress");
            dataTable.Columns.Add("Plastic Strain");
            rows.ForEach(x => { dataTable.Rows.Add(x); });
            dataGridMaterial.DataSource = dataTable;
        }

        private void comboBox1_DropDown(object sender, EventArgs e)
        {
            string[] fileNames = Directory.GetFiles(pathMaterial).Select(Path.GetFileNameWithoutExtension).ToArray();
            comboBox1.DataSource = new BindingSource(fileNames, null);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            bool someEmpty = true;
            foreach (TextBox textBox in Setting.Controls.OfType<TextBox>())
            {
                if (string.IsNullOrEmpty(textBox.Text) || dataGridAddMaterial.Rows.Count == 1)
                {
                    someEmpty = true;
                    MessageBox.Show("Заполните все поля");
                    return;
                }
                else
                    someEmpty = false;
            }
            if (!someEmpty)
                AddMaterial();

        }

        public void AddMaterial()
        {
            string MaterialName = materialName.Text;
            int rowCounter = dataGridAddMaterial.RowCount;
            int columnCount = dataGridAddMaterial.ColumnCount;
            string[] line = new string[columnCount];
            using (StreamWriter writer = new StreamWriter((Path.Combine(pathMaterial, MaterialName + ".csv")), true))
            {
                for (int i = 0; i < dataGridAddMaterial.RowCount - 1; i++)
                {
                    for (int j = 0; j < dataGridAddMaterial.ColumnCount; j++)
                    {
                        line[j] = (string)(dataGridAddMaterial.Rows[i].Cells[j].Value ?? "");
                    }
                    writer.WriteLine(string.Join(";", line));
                }
            }

        }
        private const int N = 24, M = 2;
        private void button3_Click(object sender, EventArgs e)
        {

            string filename = null;
            OpenFileDialog openFileDialog1 = new OpenFileDialog() { Filter = "(*.csv)|*.csv" };
            openFileDialog1.InitialDirectory = PathDesk;
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
                filename = openFileDialog1.FileName;
            List<string[]> rows = File.ReadAllLines(filename).Select(x => x.Split(';')).ToList();
            DataTable dataTable = new DataTable();           
            dataTable.Columns.Add("min. Tensile stress");
            dataTable.Columns.Add("max. Shear strain");
            dataTable.Columns.Add("Parameters");
            rows.ForEach(x => { dataTable.Rows.Add(x); });
            dataGridView1.DataSource = dataTable;
            richTextBox1.Text = "";

            
            var g = new int[N];
            int m = 1;
            for (int i = 0; i < M; i++)
                for (int j = 0; j < N; j++)
                    dataGridView1[i, j].Value = dataGridView1[i, j].Value.ToString().Replace('.', ',');
            for (int i = 0; i < N - 1; i++)
                for (int k = 0; k < N - 1; k++)
                    if ((i < k) &&
                        (double.Parse(dataGridView1[0, i].Value.ToString()) >=
                         double.Parse(dataGridView1[0, k].Value.ToString())) &&
                        (double.Parse(dataGridView1[1, i].Value.ToString()) <=
                         double.Parse(dataGridView1[1, k].Value.ToString())))

                        if ((i < k) &&
                            (double.Parse(dataGridView1[0, i].Value.ToString()) >
                             double.Parse(dataGridView1[0, k].Value.ToString())) &&
                            (double.Parse(dataGridView1[1, i].Value.ToString()) <
                             double.Parse(dataGridView1[1, k].Value.ToString())))
                        {
                            bool b = true;
                            for (int j = 1; j <= N; j++)
                                if (g[j - 1] == i + 1)
                                {
                                    b = false;
                                    break;
                                }
                            if (b)
                                g[m++] = i + 1;
                        }
            for (int i = 0; i < N - 1; i++)
                for (int k = 0; k < N - 1; k++)
                    if ((i < k) &&
                        (double.Parse(dataGridView1[0, i].Value.ToString()) <=
                         double.Parse(dataGridView1[0, k].Value.ToString())) &&
                        (double.Parse(dataGridView1[1, i].Value.ToString()) >=
                         double.Parse(dataGridView1[1, k].Value.ToString())))

                        if ((i < k) &&
                            (double.Parse(dataGridView1[0, i].Value.ToString()) <
                             double.Parse(dataGridView1[0, k].Value.ToString())) &&
                            (double.Parse(dataGridView1[1, i].Value.ToString()) >
                             double.Parse(dataGridView1[1, k].Value.ToString())))
                        {
                            bool b = true;
                            for (int j = 1; j <= N; j++)
                                if (g[j - 1] == k + 1)
                                {
                                    b = false;
                                    break;
                                }
                            if (b)
                                g[m++] = k + 1;
                        }
            for (int j = 1; j <= N; j++)
            {
                bool b = true;
                for (int k = 1; k < N - 1; k++)
                    if (j == g[k - 1])
                    {
                        b = false;
                        break;
                    }
                if (b)
                    richTextBox1.Text += dataGridView1[2, j - 1].Value.ToString() + "\n";
            }
        }

    }

}






