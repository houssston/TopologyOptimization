# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Tue Oct 30 18:56:02 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=295.516662597656, 
    height=165.75)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('extract.py', __main__.__dict__)
#* OdbError: Cannot open file F:/MyProject/ver1/bin/Debug/@Path. *** ERROR: No 
#* such file: F:/MyProject/ver1/bin/Debug/@Path.
#* File "extract.py", line 6, in <module>
#*     odb = openOdb(path='@Path')
