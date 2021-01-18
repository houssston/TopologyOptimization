# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro2():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/TempCalculat/Upper.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='upper', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE, topology=SHELL, 
        convertToAnalytical=1, stitchEdges=1)
    p = mdb.models['Model-1'].parts['upper']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['upper']
    p.ReferencePoint(point=(0.0, 80, 10))
    p = mdb.models['Model-1'].parts['upper']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-upper')
    p = mdb.models['Model-1'].parts['upper']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#fff ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Upper')
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/TempCalculat/Model.IGS', msbo=False, trimCurve=DEFAULT, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='model', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DEFORMABLE_BODY, convertToAnalytical=1, 
        stitchEdges=1)
    p = mdb.models['Model-1'].parts['model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=121.191, 
        farPlane=253.507, width=216.176, height=88.4448, viewOffsetX=6.81647, 
        viewOffsetY=-6.46684)
    p = mdb.models['Model-1'].parts['model']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(cells=cells, name='Set-Model')
    p = mdb.models['Model-1'].parts['model']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3f ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Model')
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/TempCalculat/Tool.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='tool', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE, topology=SHELL, 
        convertToAnalytical=1, stitchEdges=1)
    p = mdb.models['Model-1'].parts['tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['tool']
    p.ReferencePoint(point=(0.0, 40, 5.0))
    p = mdb.models['Model-1'].parts['tool']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-Tool')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=223.788, 
        farPlane=448.668, width=336.461, height=137.657, viewOffsetX=8.81758, 
        viewOffsetY=1.41326)
    p = mdb.models['Model-1'].parts['tool']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3ff ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Tool')
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/TempCalculat/Lower.IGS', 
        msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='lower', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE, topology=SHELL, 
        convertToAnalytical=1, stitchEdges=1)
    p = mdb.models['Model-1'].parts['lower']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['lower']
    p.ReferencePoint(point=(0.0, 0.0, 10))
    p = mdb.models['Model-1'].parts['lower']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-Lower')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=185.623, 
        farPlane=318.781, width=181.396, height=74.2152, viewOffsetX=2.29141, 
        viewOffsetY=0.737231)
    p = mdb.models['Model-1'].parts['lower']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3fff ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Lower')
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    mdb.models['Model-1'].Material(name='Titan')
    mdb.models['Model-1'].materials['Titan'].Density(table=((4.5E-09, ), ))
    mdb.models['Model-1'].materials['Titan'].Elastic(table=((112000, 0.32), ))
    mdb.models['Model-1'].materials['Titan'].Plastic(table=((1.0,0.0),(75.0,0.1),(125.0,0.2),(140.0,0.3),(160.0,0.4),(165.0,0.5),(167.0,0.6),(175.0,1.0)))
    mdb.models['Model-1'].HomogeneousSolidSection(name='Section-Titan', 
        material='Titan', thickness=None)
    p1 = mdb.models['Model-1'].parts['model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=123.65, 
        farPlane=251.048, width=194.889, height=79.7355, viewOffsetX=1.97121, 
        viewOffsetY=-0.338491)
    p = mdb.models['Model-1'].parts['model']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['model']
    p.SectionAssignment(region=region, sectionName='Section-Titan', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['lower']
    a.Instance(name='lower-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['model']
    a.Instance(name='model-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['tool']
    a.Instance(name='tool-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['upper']
    a.Instance(name='upper-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
        timePeriod=0.05)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-2', previous='Step-1', 
        timePeriod=0.05)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.4, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['upper-1'].surfaces['Surf-Upper']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Upper', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['tool-1'].surfaces['Surf-Tool']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Tool', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['lower-1'].surfaces['Surf-Lower']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Lower', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    regionDef=mdb.models['Model-1'].rootAssembly.instances['model-1'].sets['Set-Model']
    mdb.models['Model-1'].FieldOutputRequest(name='F-Output-2', 
        createStepName='Step-1', variables=('COORD', ), region=regionDef, 
        sectionPoints=DEFAULT, rebar=EXCLUDE)
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['upper-1'].sets['Set-upper']
    mdb.models['Model-1'].DisplacementBC(name='Fix-Upper', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['tool-1'].sets['Set-Tool']
    mdb.models['Model-1'].DisplacementBC(name='Fix-Tool', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['lower-1'].sets['Set-Lower']
    mdb.models['Model-1'].DisplacementBC(name='Fix-Lower', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['upper-1'].sets['Set-upper']
    mdb.models['Model-1'].DisplacementBC(name='Load-Upper', 
        createStepName='Step-1', region=region, u1=UNSET, u2=-560, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
    mdb.models['Model-1'].boundaryConditions['Load-Upper'].setValuesInStep(
        stepName='Step-2', u2=0.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['lower-1'].sets['Set-Lower']
    mdb.models['Model-1'].DisplacementBC(name='Load-Lower', 
        createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
    mdb.models['Model-1'].boundaryConditions['Load-Lower'].setValuesInStep(
        stepName='Step-2', u2=560)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['model']
    p.seedPart(size=3.5, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['model']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['lower']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['lower']
    p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['lower']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['tool']
    p.seedPart(size=12.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['tool']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['upper']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['upper']
    p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['upper']
    p.generateMesh()
    a1 = mdb.models['Model-1'].rootAssembly
    a1.regenerate()
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', parallelizationMethodExplicit=DOMAIN, numDomains=2, 
        activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=2)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
Macro2()

