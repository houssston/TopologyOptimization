using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swcommands;
using SolidWorks.Interop.swconst;
using System.Text.RegularExpressions;
using System.IO;
using System.Diagnostics;
using System.Threading;

namespace ver1
{
    
    class Solid
    {
        SldWorks SwApp;
        IModelDoc2 swModel;

        double lowerPlate;
        double upperPlate;
        double Length;
        double Width;
        double Height;

        object processSW = System.Activator.CreateInstance(System.Type.GetTypeFromProgID("SldWorks.Application"));
        
        public Solid(PrmModel prmModel, PrmСalculation prmСalculation)
        {  
            Length = prmModel.prmLength / 1000;
            Width = prmModel.prmWidth / 1000;
            Height = prmModel.prmHeight / 1000;            
        }
            
        public void CreateModel(PrmPath prmPath)
        {
            SwApp = (SldWorks)processSW;
            SwApp.Visible = false;

            SwApp.NewPart();
            swModel = SwApp.IActiveDoc2;

            swModel.Extension.SelectByID2("Сверху", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.SketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swModel.SketchManager.CreateLine(Length / -2, Width / -1, 0, Length / 2, Width / -1, 0);
            swModel.SketchManager.CreateLine(Length / 2, Width / -1, 0, Length / 2, 0, 0);
            swModel.SketchManager.CreateLine(Length / 2, 0, 0, Length / -2, 0, 0);
            swModel.SketchManager.CreateLine(Length / -2, 0, 0, Length / -2, Width / -1, 0);
            swModel.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swModel.FeatureManager.FeatureExtrusion2(true, false, false, 0, 0, Height, 0.01, false, false, false, false, 1.74532925199433E-02, 1.74532925199433E-02, false, false, false, false, true, true, true, 0, 0, false);
            swModel.SaveAs3((Path.Combine(prmPath.prmFolderСalculated, "Model.IGS")), 0, 0);
        }

        public void CreateUpperPunch(PrmModel prmModel, PrmPath prmPath)
        {
            SwApp = (SldWorks)processSW;
            SwApp.Visible = false;

            SwApp.NewPart();
            swModel = SwApp.IActiveDoc2;
            SwApp.CloseDoc("Деталь1.SLDPRT");

            swModel.Extension.SelectByID2("Спереди", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.SketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swModel.SketchManager.CreateLine(0, Height, 0, Length / 2, Height, 0);//прямая
            swModel.SketchManager.CreateLine(Length / 2, Height, 0, Height + 0.01, (Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)) + Height, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, (Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)) + Height, 0, Height + 0.01, (Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)) + Height + 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, (Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)) + Height + 0.005, 0, Length / 2, Height + 0.005, 0);
            swModel.SketchManager.CreateLine(0, Height + 0.005, 0, Length / 2, Height + 0.005, 0);
            swModel.SketchManager.CreateCenterLine(0, 0, 0, 0, 0.123875, 0);
            swModel.Extension.SelectByID2("Point2", "SKETCHPOINT", Length / 2, Height, 0, false, 0, null, 0);
            swModel.SketchManager.CreateFillet(0.005, 1);
            swModel.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line5", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line6", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.SketchMirror();
            swModel.ClearSelection2(true);
            swModel.SketchManager.InsertSketch(true);
            swModel.Extension.SelectByID2("Line5", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swModel.FeatureManager.FeatureExtrusion2(false, false, false, 0, 0, Width + 0.005, 0.005, false, false, false, false, 1.74532925199433E-02, 1.74532925199433E-02, false, false, false, false, true, true, true, 0, 0, false);
            swModel.SaveAs3((Path.Combine(prmPath.prmFolderСalculated, "Upper.IGS")), 0, 0);
            
        }

        public void CreateLowerPunch(PrmModel prmModel, PrmPath prmPath)
        {
            SwApp = (SldWorks)processSW;
            SwApp.Visible = false;
            SwApp.NewPart();
            swModel = SwApp.IActiveDoc2;
            SwApp.CloseDoc("Деталь2.SLDPRT");

            swModel.Extension.SelectByID2("Спереди", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.SketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);

            swModel.SketchManager.CreateLine(0, 0, 0, Length / 2, 0, 0);
            swModel.SketchManager.CreateLine(Length / 2, 0, 0, Height + 0.01, -(Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)), 0);
            swModel.SketchManager.CreateLine(Height + 0.01, -(Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)), 0, Height + 0.01, -(Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)) - 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, -(Math.Tan(prmModel.prmAngle * Math.PI / 180) * (Height - Length / 2 + 0.01)) - 0.005, 0, Length / 2, -0.005, 0);
            swModel.SketchManager.CreateLine(0, -0.005, 0, Length / 2, -0.005, 0);
            swModel.SketchManager.CreateCenterLine(0, 0, 0, 0, -0.044984, 0);
            swModel.Extension.SelectByID2("Point2", "SKETCHPOINT", Length / 2, 0, 0, false, 0, null, 0);
            swModel.SketchManager.CreateFillet(0.005, 1);
            swModel.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line5", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.Extension.SelectByID2("Line6", "SKETCHSEGMENT", 0, 0, 0, true, 0, null, 0);
            swModel.SketchMirror();
            swModel.ClearSelection2(true);
            swModel.SketchManager.InsertSketch(true);
            swModel.Extension.SelectByID2("Line5", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swModel.FeatureManager.FeatureExtrusion2(false, false, false, 0, 0, Width + 0.005, 0.005, false, false, false, false, 1.74532925199433E-02, 1.74532925199433E-02, false, false, false, false, true, true, true, 0, 0, false);
            swModel.SaveAs3((Path.Combine(prmPath.prmFolderСalculated, "Lower.IGS")), 0, 0);
        }
        public void CreateTool(PrmModel prmModel, PrmPath prmPath)
        {
            SwApp = (SldWorks)processSW;
            SwApp.Visible = false;
            SwApp.NewPart();
            swModel = SwApp.IActiveDoc2;
            SwApp.CloseDoc("Деталь3.SLDPRT");

            swModel.Extension.SelectByID2("Сверху", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.SketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swModel.SketchManager.CreateLine(Height + 0.01, -Width - 0.005, 0, Height + 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, 0.005, 0, -Height - 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(-Height - 0.01, -Width - 0.005, 0, -Height - 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, -Width - 0.005, 0, -Height - 0.01, -Width - 0.005, 0);

            swModel.SketchManager.CreateLine(Height + 0.005, -Width, 0, Height + 0.005, 0, 0);
            swModel.SketchManager.CreateLine(Height + 0.005, 0, 0, -Height - 0.005, 0, 0);
            swModel.SketchManager.CreateLine(-Height - 0.005, -Width, 0, -Height - 0.005, 0, 0);
            swModel.SketchManager.CreateLine(-Height - 0.005, -Width, 0, Height + 0.005, -Width, 0);

            swModel.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, false, 0, null, 0);
            swModel.FeatureManager.FeatureExtrusion2(false, false, false, 0, 0, Height + 0.02, 0.02, false, false, false, false, 1.74532925199433E-02, 1.74532925199433E-02, false, false, false, false, true, true, true, 0, 0, false);
            swModel.SaveAs3(Path.Combine(prmPath.prmFolderСalculated, "Tool.IGS"), 0, 0);
        }
        public void CreateLowerPlate(PrmModel prmModel, PrmPath prmPath)
        {
            System.Threading.Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
            double[] Coord = File.ReadAllLines(Path.Combine(prmPath.prmPathDesk, prmPath.prmFolder, "TempCalculat", "Coordinates.csv")).Select(n => double.Parse(n)).ToArray();           
            double minCoord = Coord.Min();
            double lowerPlate = (minCoord - 0.4) / 1000;

            SwApp = (SldWorks)processSW;
            SwApp.Visible = false;
            SwApp.NewPart();
            swModel = SwApp.IActiveDoc2;
            SwApp.CloseDoc("Деталь4.SLDPRT");

            swModel.Extension.SelectByID2("Сверху", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.FeatureManager.InsertRefPlane(8, lowerPlate, 0, 0, 0, 0);
            swModel.Extension.SelectByID2("Плоскость4", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.SketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swModel.SketchManager.CreateLine(Height + 0.01, -Width - 0.005, 0, Height + 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, 0.005, 0, -Height - 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(-Height - 0.01, -Width - 0.005, 0, -Height - 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, -Width - 0.005, 0, -Height - 0.01, -Width - 0.005, 0);
            swModel.FeatureManager.FeatureExtrusion2(true, false, true, 0, 0, 0.005, 0.01, false, false, false, false, 1.74532925199433E-02, 1.74532925199433E-02, false, false, false, false, true, true, true, 0, 0, false);
            swModel.SaveAs3(Path.Combine(prmPath.prmFolderСalculated, "LowerPlate.IGS"), 0, 0);
        }
        public void CreateUpperPlate(PrmModel prmModel, PrmPath prmPath)
        {
            System.Threading.Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");
            double[] Coord = File.ReadAllLines(Path.Combine(prmPath.prmPathDesk, prmPath.prmFolder, "TempCalculat", "Coordinates.csv")).Select(n => double.Parse(n)).ToArray();
            double maxCoord = Coord.Max();
            double upperPlate = (maxCoord+0.4) / 1000;
           

            SwApp = (SldWorks)processSW;
            SwApp.Visible = false;
            SwApp.NewPart();
            swModel = SwApp.IActiveDoc2;
            SwApp.CloseDoc("Деталь5.SLDPRT");

            swModel.Extension.SelectByID2("Сверху", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.FeatureManager.InsertRefPlane(8, upperPlate, 0, 0, 0, 0);
            swModel.Extension.SelectByID2("Плоскость4", "PLANE", 0, 0, 0, false, 0, null, 0);
            swModel.SketchManager.InsertSketch(true);
            swModel.ClearSelection2(true);
            swModel.SketchManager.CreateLine(Height + 0.01, -Width - 0.005, 0, Height + 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, 0.005, 0, -Height - 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(-Height - 0.01, -Width - 0.005, 0, -Height - 0.01, 0.005, 0);
            swModel.SketchManager.CreateLine(Height + 0.01, -Width - 0.005, 0, -Height - 0.01, -Width - 0.005, 0);
            swModel.FeatureManager.FeatureExtrusion2(true, false, false, 0, 0, 0.005, 0.01, false, false, false, false, 1.74532925199433E-02, 1.74532925199433E-02, false, false, false, false, true, true, true, 0, 0, false);
            swModel.SaveAs3(Path.Combine(prmPath.prmFolderСalculated, "UpperPlate.IGS"), 0, 0);
        }  
    }
}
