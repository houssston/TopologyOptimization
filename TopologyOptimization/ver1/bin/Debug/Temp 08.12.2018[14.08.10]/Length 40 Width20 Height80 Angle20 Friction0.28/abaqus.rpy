# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.11-3 replay file
# Internal Version: 2011_12_07-08.24.59 112213
# Run by admin on Mon Dec 10 17:49:09 2018
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
#: Model: D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/Length 40 Width20 Height80 Angle20 Friction0.28/Job-1.odb
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
session.viewports['Viewport: 1'].view.setValues(nearPlane=418.886, 
    farPlane=503.446, width=230.723, height=122.78, viewOffsetX=36.402, 
    viewOffsetY=4.50455)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=29)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=19)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-2', frame=20)
session.viewports['Viewport: 1'].view.setValues(nearPlane=400.852, 
    farPlane=451.558, width=77.7809, height=41.3913, viewOffsetX=-23.843, 
    viewOffsetY=13.2486)
session.viewports['Viewport: 1'].view.setValues(nearPlane=363.451, 
    farPlane=520.235, width=70.5237, height=37.5294, cameraPosition=(-249.236, 
    74.0838, 373.273), cameraUpVector=(0.121983, 0.992365, -0.0182256), 
    cameraTarget=(-2.19169, 37.2049, 18.7185), viewOffsetX=-21.6184, 
    viewOffsetY=12.0125)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=402.028, 
    farPlane=450.382, width=68.9289, height=36.6807, viewOffsetX=-35.4686, 
    viewOffsetY=-14.2057)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=404.827, 
    farPlane=447.582, width=47.8831, height=25.4811, viewOffsetX=41.2094, 
    viewOffsetY=-12.5906)
session.viewports['Viewport: 1'].view.setValues(nearPlane=388.307, 
    farPlane=496.24, width=45.929, height=24.4413, cameraPosition=(157.931, 
    30.0648, 423.01), cameraUpVector=(-0.0182626, 0.999409, 0.0291252), 
    cameraTarget=(0.013047, 38.9479, 19.1743), viewOffsetX=39.5277, 
    viewOffsetY=-12.0768)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=404.427, 
    farPlane=447.982, width=50.8891, height=27.0808, viewOffsetX=35.6891, 
    viewOffsetY=13.5178)
session.viewports['Viewport: 1'].view.setValues(nearPlane=380.867, 
    farPlane=502.245, width=47.9245, height=25.5032, cameraPosition=(153.786, 
    101.865, 419.272), cameraUpVector=(-0.0352673, 0.989533, -0.139929), 
    cameraTarget=(0.30708, 39.7107, 18.422), viewOffsetX=33.61, 
    viewOffsetY=12.7304)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-3', frame=0)
session.viewports[session.currentViewportName].odbDisplay.setFrame(
    step='Step-4', frame=30)
