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
    class Abaqus
    {
        public void RunMacros(PathAbaqus pathAbaqus)
        {
            string cmdMacros = pathAbaqus.prmCmd + pathAbaqus.prmMacrosName;
            var runMacros = new ProcessStartInfo();          
            {
                runMacros.UseShellExecute = true;
                runMacros.WorkingDirectory = Path.Combine(pathAbaqus.prmFolderСalculated);
                runMacros.FileName = Path.Combine(pathAbaqus.prmSystemDirectory, "cmd.exe");
                runMacros.Arguments = "/" + pathAbaqus.prmArguments + cmdMacros;              
                runMacros.WindowStyle = ProcessWindowStyle.Hidden;
            };
            Process.Start(runMacros).WaitForExit(); 
        }
        public void RunExtract(PathAbaqus pathAbaqus)
        {   
            string cmdExtract = pathAbaqus.prmCmd + pathAbaqus.prmExtractName;
            var runExtract = new ProcessStartInfo();
            {
                runExtract.UseShellExecute = true;
                runExtract.WorkingDirectory = Path.Combine(pathAbaqus.prmFolderСalculated);
                runExtract.FileName = Path.Combine(pathAbaqus.prmSystemDirectory, "cmd.exe");
                runExtract.Arguments = "/" + pathAbaqus.prmArguments + cmdExtract;
                runExtract.WindowStyle = ProcessWindowStyle.Hidden;
            };
            Process.Start(runExtract).WaitForExit();          
        }
    }
}
