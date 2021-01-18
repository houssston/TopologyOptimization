# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Sun Dec 16 15:35:42 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle15 Friction0.4/Job-1.odb
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=394.191, 
    farPlane=479.422, width=235.396, height=125.267, viewOffsetX=-7.89919, 
    viewOffsetY=-4.13924)
session.graphicsOptions.setValues(backgroundColor='#FFFFFF')
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.073, 
    farPlane=476.54, width=237.117, height=126.183, viewOffsetX=10.3849, 
    viewOffsetY=-46.8197)
session.graphicsOptions.setValues(backgroundStyle=SOLID)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.089, 
    farPlane=476.524, width=237.128, height=126.188, viewOffsetX=16.1312, 
    viewOffsetY=-45.0536)
session.viewports['Viewport: 1'].view.setValues(nearPlane=400.431, 
    farPlane=473.182, width=198.612, height=105.692, viewOffsetX=8.70335, 
    viewOffsetY=-37.0831)
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.916, 
    farPlane=471.697, width=199.349, height=106.084, viewOffsetX=2.60467, 
    viewOffsetY=-38.1496)
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.824, 
    farPlane=471.789, width=199.303, height=106.06, viewOffsetX=3.53279, 
    viewOffsetY=-36.0977)
session.viewports['Viewport: 1'].view.setValues(width=187.348, height=99.6978, 
    viewOffsetX=0.696484, viewOffsetY=-33.6853)
session.viewports['Viewport: 1'].view.setValues(nearPlane=403.328, 
    farPlane=470.285, width=188.047, height=100.07, viewOffsetX=-1.75446, 
    viewOffsetY=-35.3882)
session.viewports['Viewport: 1'].view.setValues(nearPlane=403.24, 
    farPlane=470.373, width=188.006, height=100.048, viewOffsetX=-1.75408, 
    viewOffsetY=-33.6283)
