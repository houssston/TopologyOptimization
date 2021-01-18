# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Sun Dec 16 15:08:00 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle30 Friction0.4/Job-1.odb
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
    farPlane=473.699, width=164.751, height=87.6725, viewOffsetX=1.93319, 
    viewOffsetY=7.55047)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].odbDisplay.setFrame(step='Step-1')
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=16)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports['Viewport: 1'].view.setValues(nearPlane=395.64, 
    farPlane=477.973, width=197.038, height=104.854, viewOffsetX=13.1637, 
    viewOffsetY=24.0067)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.021, 
    farPlane=476.592, width=197.726, height=105.22, viewOffsetX=-10.5617, 
    viewOffsetY=-37.8255)
session.viewports['Viewport: 1'].view.setValues(width=210.35, height=111.938, 
    viewOffsetX=-11.3441, viewOffsetY=-35.6442)
session.viewports['Viewport: 1'].view.setValues(nearPlane=395.445, 
    farPlane=478.168, width=209.512, height=111.492, viewOffsetX=-4.85534, 
    viewOffsetY=-37.65)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=400.211, 
    farPlane=473.402, width=212.037, height=112.836, viewOffsetX=2.59537, 
    viewOffsetY=-37.3133)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF')
session.viewports['Viewport: 1'].view.setValues(nearPlane=403.232, 
    farPlane=470.381, width=200.819, height=106.867, viewOffsetX=-2.49657, 
    viewOffsetY=-34.6982)
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.739, 
    farPlane=471.874, width=200.076, height=106.471, viewOffsetX=0.682563, 
    viewOffsetY=-35.3156)
