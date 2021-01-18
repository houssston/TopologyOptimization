# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Tue Dec 11 00:06:19 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 10.12.2018[20.50.28]/Length 40 Width20 Height80 Angle25 Friction0.24/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     6
#: Number of Meshes:             6
#: Number of Element Sets:       6
#: Number of Node Sets:          11
#: Number of Steps:              4
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Z-Plane', 
    ), viewCut=ON)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
session.viewports['Viewport: 1'].view.setValues(nearPlane=437.743, 
    farPlane=520.696, width=199.315, height=106.066, viewOffsetX=0.192609, 
    viewOffsetY=3.58131)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=445.606, 
    farPlane=512.833, width=139.971, height=74.4861, viewOffsetX=15.3553, 
    viewOffsetY=10.2925)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=453.283, 
    farPlane=505.156, width=92.7098, height=49.3358, viewOffsetX=-9.89135, 
    viewOffsetY=-18.7952)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=407.045, 
    farPlane=445.365, width=31.2212, height=16.6145, viewOffsetX=-37.0055, 
    viewOffsetY=19.8983)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=405.893, 
    farPlane=446.517, width=39.8756, height=21.2199, viewOffsetX=39.5934, 
    viewOffsetY=17.2184)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=2)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=3)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=4)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=5)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=6)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=29)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=5)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=4)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
