using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ver1
{
    class PrmModel
    {
        private double ModelLength;
        private double ModelWidth;
        private double ModelHeight;
        private double angle;

        public double prmAngle
        {
            get { return angle; }
            set { angle = value; }
        }
        public double prmLength
        {
            get { return ModelLength; }
            set { ModelLength = value; }
        }
        public double prmWidth
        {
            get { return ModelWidth; }
            set { ModelWidth = value; }
        }
        public double prmHeight
        {
            get { return ModelHeight; }
            set { ModelHeight = value; }
        }
    }

    class PrmСalculation
    {
        private double CalcDensity;
        private double CalcElasticYM;
        private double CalcElasticPR;
        private double CalcGrid1;
        private double CalcGrid2;
        private double CalcFriction;
        private double CalcMoving;
        private string CalcMaterial;

        public double prmDensity
        {
            get { return CalcDensity; }
            set { CalcDensity = value; }
        }
        public double prmElasticYM
        {
            get { return CalcElasticYM; }
            set { CalcElasticYM = value; }
        }
        public double prmElasticPR
        {
            get { return CalcElasticPR; }
            set { CalcElasticPR = value; }
        }
        public double prmGrid1
        {
            get { return CalcGrid1; }
            set { CalcGrid1 = value; }
        }
        public double prmGrid2
        {
            get { return CalcGrid2; }
            set { CalcGrid2 = value; }
        }
        public double prmFriction
        {
            get { return CalcFriction; }
            set { CalcFriction = value; }
        }
        public double prmMoving
        {
            get { return CalcMoving; }
            set { CalcMoving = value; }
        }
        public string prmMaterial
        {
            get { return CalcMaterial; }
            set { CalcMaterial = value; }
        }
    }

    class PrmPath
    {
        private string PathDesk;
        private string Folder;
        private string MacrosName;
        private string FolderСalculated;
        private string ExtractName;

        public string prmPathDesk
        {
            get { return PathDesk; }
            set { PathDesk = value; }
        }
        public string prmFolder
        {
            get { return Folder; }
            set { Folder = value; }
        }
        public string prmMacrosName
        {
            get { return MacrosName; }
            set { MacrosName = value; }
        }
        public string prmFolderСalculated
        {
            get { return FolderСalculated; }
            set { FolderСalculated = value; }
        }
        public string prmExtractName
        {
            get { return ExtractName; }
            set { ExtractName = value; }
        }
    }

    class PathAbaqus
    {
        private string cmd;
        private string SystemDirectory;
        private string Arguments;
        private string ScriptName;
        private string PathDesk;
        private string FolderСalculated;
        private string ExtractName;
        private string NodeName;


        public string prmCmd
        {
            get { return cmd; }
            set { cmd = value; }
        }
        public string prmSystemDirectory
        {
            get { return SystemDirectory; }
            set { SystemDirectory = value; }
        }
        public string prmArguments
        {
            get { return Arguments; }
            set { Arguments = value; }
        }
        public string prmMacrosName
        {
            get { return ScriptName; }
            set { ScriptName = value; }
        }
        public string prmPathDesk
        {
            get { return PathDesk; }
            set { PathDesk = value; }
        }
        public string prmFolderСalculated
        {
            get { return FolderСalculated; }
            set { FolderСalculated = value; }
        }
        public string prmExtractName
        {
            get { return ExtractName; }
            set { ExtractName = value; }
        }
        public string prmNodeName
        {
            get { return NodeName; }
            set { NodeName = value; }
        }


    }

    class PathCSV
    {

        private string FolderСalculated;
        private string PathDesk;
        private string Folder;

        public string prmFolderСalculated
        {
            get { return FolderСalculated; }
            set { FolderСalculated = value; }
        }
        public string prmPathDesk
        {
            get { return PathDesk; }
            set { PathDesk = value; }
        }
        public string prmFolder
        {
            get { return Folder; }
            set { Folder = value; }
        }
    }

}
