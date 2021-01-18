# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Sun Dec 16 15:18:49 2018
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=234.883331298828, 
    height=162.066665649414)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='Job-1.odb')
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle15 Friction0.36/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     6
#: Number of Meshes:             6
#: Number of Element Sets:       6
#: Number of Node Sets:          11
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Z-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.16, 
    farPlane=472.454, width=155.348, height=82.6688, viewOffsetX=3.73946, 
    viewOffsetY=6.77912)
session.viewports['Viewport: 1'].view.setValues(nearPlane=402.281, 
    farPlane=471.332, width=155.782, height=82.8998, viewOffsetX=-26.7386, 
    viewOffsetY=-28.7719)
session.viewports['Viewport: 1'].view.setValues(nearPlane=398.448, 
    farPlane=475.166, width=174.624, height=92.9265, viewOffsetX=-21.1189, 
    viewOffsetY=-30.5035)
leaf = dgo.LeafFromPartInstance(partInstanceName=('LOWER-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('LOWERPLATE-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('TOOL-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('UPPER-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('UPPERPLATE-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].view.setValues(nearPlane=404.567, 
    farPlane=469.046, width=177.306, height=94.3536, viewOffsetX=-7.39756, 
    viewOffsetY=-32.1287)
session.viewports['Viewport: 1'].view.setValues(nearPlane=403.171, 
    farPlane=470.442, width=199.971, height=106.415, viewOffsetX=-7.31937, 
    viewOffsetY=-36.6663)
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.746, 
    farPlane=471.867, width=199.264, height=106.039, viewOffsetX=1.62046, 
    viewOffsetY=-36.1653)
