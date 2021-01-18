# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Mon Dec 10 18:40:05 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle30 Friction0.24/Job-1.odb
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
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(session.views['Back'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Z-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=397.271, 
    farPlane=476.342, width=185.221, height=98.5661, viewOffsetX=-2.82336, 
    viewOffsetY=4.76135)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=15)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=14)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
