# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Sun Dec 16 15:07:51 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle25 Friction0.4/Job-1.odb
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
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    COMPONENT, 'LE12'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=399.914, 
    farPlane=473.699, width=164.751, height=87.6725, viewOffsetX=5.7266, 
    viewOffsetY=3.4221)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.095, 
    farPlane=472.518, width=165.237, height=87.9314, viewOffsetX=-20.4357, 
    viewOffsetY=-29.0608)
session.viewports['Viewport: 1'].view.setValues(nearPlane=395.74, 
    farPlane=477.873, width=196.285, height=104.454, viewOffsetX=0.946728, 
    viewOffsetY=-25.9327)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.208, 
    farPlane=476.405, width=197.013, height=104.841, viewOffsetX=-0.151419, 
    viewOffsetY=-34.1077)
session.viewports['Viewport: 1'].view.setValues(nearPlane=394.191, 
    farPlane=479.422, width=207.996, height=110.686, viewOffsetX=4.86519, 
    viewOffsetY=-24.208)
leaf = dgo.LeafFromPartInstance(partInstanceName=('LOWER-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('LOWERPLATE-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('MODEL-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
#: Warning: The selected Primary Variable is not available in the current frame for any elements in the current display group.
leaf = dgo.LeafFromPartInstance(partInstanceName=('MODEL-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.add(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('TOOL-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('UPPER-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromPartInstance(partInstanceName=('UPPERPLATE-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=400.307, 
    farPlane=473.306, width=211.224, height=112.403, cameraPosition=(-2.77325, 
    39.2899, 446.807), cameraUpVector=(-0.104483, 0.994527, 0), cameraTarget=(
    -2.77325, 39.2899, 10), viewOffsetX=4.94067, viewOffsetY=-24.5836)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=286.189, 
    farPlane=345.199, width=150.943, height=80.3247, viewOffsetX=-16.1775, 
    viewOffsetY=-24.0552)
session.viewports['Viewport: 1'].view.setValues(nearPlane=281.942, 
    farPlane=349.446, width=179.034, height=95.2736, viewOffsetX=-10.2863, 
    viewOffsetY=-22.1647)
session.viewports['Viewport: 1'].view.setValues(nearPlane=283.257, 
    farPlane=348.131, width=179.869, height=95.7179, viewOffsetX=-6.6464, 
    viewOffsetY=-30.985)
session.viewports['Viewport: 1'].view.setValues(nearPlane=278.836, 
    farPlane=352.552, width=200.387, height=106.636, viewOffsetX=-8.63618, 
    viewOffsetY=-32.1643)
session.viewports['Viewport: 1'].view.setValues(nearPlane=280.581, 
    farPlane=350.807, width=201.641, height=107.304, viewOffsetX=1.6455, 
    viewOffsetY=-34.8086)
session.viewports['Viewport: 1'].view.setValues(nearPlane=280.438, 
    farPlane=350.95, width=201.538, height=107.249, viewOffsetX=3.52293, 
    viewOffsetY=-34.7908)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
