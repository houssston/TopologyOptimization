# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Mon Dec 10 18:37:04 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle25 Friction0.32/Job-1.odb
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=398.594, 
    farPlane=475.019, width=174.688, height=92.9607, viewOffsetX=-1.54546, 
    viewOffsetY=3.0299)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=16)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=17)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=417.993, 
    farPlane=455.621, width=28.6244, height=15.2326, viewOffsetX=-34.8908, 
    viewOffsetY=20.436)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407.353, 
    farPlane=480.661, width=27.8958, height=14.8448, cameraPosition=(-70.9675, 
    67.6931, 447.441), cameraUpVector=(0.0992665, 0.993518, -0.0553829), 
    cameraTarget=(-2.74966, 36.8879, 17.0954), viewOffsetX=-34.0026, 
    viewOffsetY=19.9158)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=406.208, 
    farPlane=446.202, width=37.5121, height=19.9622, viewOffsetX=37.0457, 
    viewOffsetY=17.0931)
session.viewports['Viewport: 1'].view.setValues(nearPlane=398.721, 
    farPlane=462.407, width=36.8208, height=19.5943, cameraPosition=(26.2916, 
    87.4978, 437.143), cameraUpVector=(-0.0828079, 0.990143, -0.112955), 
    cameraTarget=(1.25066, 36.355, 7.19238), viewOffsetX=36.363, 
    viewOffsetY=16.778)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=29)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=29)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
