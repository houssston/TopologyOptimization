# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Mon Dec 10 16:50:55 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle15 Friction0.32/Job-1.odb
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
    step='Step-3', frame=2)
session.viewports['Viewport: 1'].view.setValues(nearPlane=403.452, 
    farPlane=470.161, width=138.05, height=73.4636, viewOffsetX=1.30089, 
    viewOffsetY=-1.31192)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=1)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=18)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=419, 
    farPlane=454.613, width=21.0582, height=11.2062, viewOffsetX=43.0563, 
    viewOffsetY=15.8368)
session.viewports['Viewport: 1'].view.setValues(nearPlane=405.432, 
    farPlane=490.004, width=20.3763, height=10.8433, cameraPosition=(89.171, 
    90.0971, 445.888), cameraUpVector=(-0.059497, 0.992337, -0.108296), 
    cameraTarget=(1.96703, 38.4992, 20.9958), viewOffsetX=41.662, 
    viewOffsetY=15.324)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=402.567, 
    farPlane=449.843, width=64.88, height=34.5261, viewOffsetX=-30.2289, 
    viewOffsetY=10.3429)
session.viewports['Viewport: 1'].view.setValues(nearPlane=379.684, 
    farPlane=496.022, width=61.192, height=32.5635, cameraPosition=(-141.238, 
    86.9727, 421.783), cameraUpVector=(0.0297003, 0.993958, -0.105664), 
    cameraTarget=(0.354788, 39.4561, 14.6051), viewOffsetX=-28.5106, 
    viewOffsetY=9.75495)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=403.074, 
    farPlane=449.336, width=61.064, height=32.4954, viewOffsetX=-34.3509, 
    viewOffsetY=-15.5697)
session.viewports['Viewport: 1'].view.setValues(nearPlane=381.789, 
    farPlane=496.887, width=57.8395, height=30.7794, cameraPosition=(-123.758, 
    -32.3473, 425.299), cameraUpVector=(-0.0188522, 0.985557, 0.168293), 
    cameraTarget=(0.310487, 39.9092, 16.0481), viewOffsetX=-32.537, 
    viewOffsetY=-14.7475)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=406.783, 
    farPlane=445.627, width=33.1926, height=17.6636, viewOffsetX=44.9793, 
    viewOffsetY=-17.0078)
session.viewports['Viewport: 1'].view.setValues(nearPlane=387.85, 
    farPlane=502.1, width=31.6478, height=16.8415, cameraPosition=(153.229, 
    -13.9589, 424.277), cameraUpVector=(0.0176003, 0.991995, 0.125042), 
    cameraTarget=(0.6945, 39.4786, 21.8126), viewOffsetX=42.8859, 
    viewOffsetY=-16.2162)
