# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Sat Dec 08 20:18:53 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.41667, 1.41667), width=208.533, 
    height=140.533)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('TempExtract.py', __main__.__dict__)
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/TempCalculat/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     4
#: Number of Meshes:             4
#: Number of Element Sets:       4
#: Number of Node Sets:          7
#: Number of Steps:              2
#: Number of instances:  4
#: Total number of elements:  0
#: Total number of nodes:  0
print 'RT script done'
#: RT script done
