# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Sun Dec 16 02:31:07 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle30 Friction0.2/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     6
#: Number of Meshes:             6
#: Number of Element Sets:       6
#: Number of Node Sets:          11
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Z-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='LE', outputPosition=INTEGRATION_POINT, refinement=(
    INVARIANT, 'Max. Principal'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Mises'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=461.943, 
    farPlane=537.918, width=172.943, height=92.0319, viewOffsetX=5.5091, 
    viewOffsetY=10.1727)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=15)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=14)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=15)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=16)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=17)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=18)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=29)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
