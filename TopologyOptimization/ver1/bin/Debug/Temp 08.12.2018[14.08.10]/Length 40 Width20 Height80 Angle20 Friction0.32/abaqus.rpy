# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Mon Dec 10 17:50:03 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle20 Friction0.32/Job-1.odb
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
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=419.168, 
    farPlane=454.446, width=19.8026, height=10.538, viewOffsetX=43.244, 
    viewOffsetY=18.6248)
session.viewports['Viewport: 1'].view.setValues(nearPlane=407.037, 
    farPlane=490.749, width=19.2295, height=10.2331, cameraPosition=(110.717, 
    59.3296, 444.623), cameraUpVector=(0.0804073, 0.995153, -0.0566214), 
    cameraTarget=(0.0602551, 44.2435, 22.3345), viewOffsetX=41.9925, 
    viewOffsetY=18.0858)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=407.95, 
    farPlane=444.46, width=24.4301, height=13.0005, viewOffsetX=-39.0524, 
    viewOffsetY=16.8329)
session.viewports['Viewport: 1'].view.setValues(nearPlane=394.891, 
    farPlane=476.868, width=23.6481, height=12.5844, cameraPosition=(-84.8691, 
    80.2739, 435.638), cameraUpVector=(-0.0078288, 0.995429, -0.0951871), 
    cameraTarget=(0.813971, 40.4711, 12.3484), viewOffsetX=-37.8023, 
    viewOffsetY=16.2941)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=407.045, 
    farPlane=445.365, width=31.2212, height=16.6145, viewOffsetX=-40.3412, 
    viewOffsetY=-18.6482)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.233, 
    farPlane=455.177, width=105.026, height=55.8897, viewOffsetX=26.8163, 
    viewOffsetY=-7.80788)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
