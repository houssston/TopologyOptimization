# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Mon Dec 10 16:49:35 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle15 Friction0.28/Job-1.odb
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
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Z-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Z-Plane'].setValues(
    position=6.7)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=18)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=401.457, 
    farPlane=450.953, width=73.2245, height=38.9666, viewOffsetX=-30.1704, 
    viewOffsetY=-12.9021)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Z-Plane'].setValues(
    position=10.6)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Z-Plane'].setValues(
    position=10)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.94, 
    farPlane=454.47, width=112.386, height=59.8066, viewOffsetX=-23.8536, 
    viewOffsetY=-20.9685)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=396.375, 
    farPlane=456.035, width=111.488, height=59.3287, viewOffsetX=-18.6206, 
    viewOffsetY=13.1219)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=399.529, 
    farPlane=452.881, width=99.2947, height=52.8399, viewOffsetX=23.3842, 
    viewOffsetY=8.39194)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=406.504, 
    farPlane=445.906, width=35.2871, height=18.7781, viewOffsetX=42.8657, 
    viewOffsetY=-17.6288)
session.viewports['Viewport: 1'].view.setValues(nearPlane=384.275, 
    farPlane=504.792, width=33.3575, height=17.7513, cameraPosition=(187.886, 
    64.5356, 412.155), cameraUpVector=(-0.0284691, 0.998308, -0.0507102), 
    cameraTarget=(0.659749, 39.3656, 21.7544), viewOffsetX=40.5216, 
    viewOffsetY=-16.6648)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
