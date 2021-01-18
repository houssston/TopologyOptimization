# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
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
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/Model.IGS', msbo=False, trimCurve=DEFAULT, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='Model', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DEFORMABLE_BODY, convertToAnalytical=1, 
        stitchEdges=1)
    p = mdb.models['Model-1'].parts['Model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/Lower.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='Lower', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE, topology=SHELL, 
        convertToAnalytical=1, stitchEdges=1)
    p = mdb.models['Model-1'].parts['Lower']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/LowerPlate.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='LowerPlate', 
        geometryFile=iges, combine=False, stitchAfterCombine=False, 
        stitchTolerance=1.0, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE, topology=SHELL, convertToAnalytical=1, 
        stitchEdges=1)
    p = mdb.models['Model-1'].parts['LowerPlate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/Tool.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='Tool', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE, topology=SHELL, 
        convertToAnalytical=1, stitchEdges=1)
    p = mdb.models['Model-1'].parts['Tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/Upper.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='Upper', geometryFile=iges, 
        combine=False, stitchAfterCombine=False, stitchTolerance=1.0, 
        dimensionality=THREE_D, type=DISCRETE_RIGID_SURFACE, topology=SHELL, 
        convertToAnalytical=1, stitchEdges=1)
    p = mdb.models['Model-1'].parts['Upper']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    iges = mdb.openIges('D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/UpperPlate.IGS', msbo=False, trimCurve=DEFAULT, topology=SHELL, scaleFromFile=OFF)
    mdb.models['Model-1'].PartFromGeometryFile(name='UpperPlate', 
        geometryFile=iges, combine=False, stitchAfterCombine=False, 
        stitchTolerance=1.0, dimensionality=THREE_D, 
        type=DISCRETE_RIGID_SURFACE, topology=SHELL, convertToAnalytical=1, 
        stitchEdges=1)
    p = mdb.models['Model-1'].parts['UpperPlate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Lower']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Lower']
    p.ReferencePoint(point=(0.0, 0.0, 10))
    mdb.models['Model-1'].parts['Lower'].features.changeKey(fromName='RP', 
        toName='RP-Lower')
    p = mdb.models['Model-1'].parts['Lower']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-Lower')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=311.045, 
        farPlane=515.37, width=214.383, height=87.7113, viewOffsetX=4.57066, 
        viewOffsetY=5.25753)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=312.474, 
        farPlane=513.941, width=215.368, height=88.1141, viewOffsetX=12.2188, 
        viewOffsetY=-5.75768)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=303.523, 
        farPlane=522.892, width=303.244, height=124.067, viewOffsetX=12.0078, 
        viewOffsetY=-6.13213)
    p = mdb.models['Model-1'].parts['Lower']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#fff ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Lower')
    p = mdb.models['Model-1'].parts['LowerPlate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['LowerPlate']
    p.ReferencePoint(point=(0.0, 13.1686, 10))
    mdb.models['Model-1'].parts['LowerPlate'].features.changeKey(fromName='RP', 
        toName='RP-LowerPlate')
    p = mdb.models['Model-1'].parts['LowerPlate']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-LowerPlate')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=307.979, 
        farPlane=489.639, width=242.919, height=99.3863, viewOffsetX=-9.89327, 
        viewOffsetY=3.57225)
    p = mdb.models['Model-1'].parts['LowerPlate']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3f ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-LowerPlate')
    p = mdb.models['Model-1'].parts['Model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=123.65, 
        farPlane=251.048, width=194.889, height=79.7355, viewOffsetX=5.15701, 
        viewOffsetY=-4.63932)
    p = mdb.models['Model-1'].parts['Model']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    p.Set(cells=cells, name='Set-Model')
    p = mdb.models['Model-1'].parts['Model']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3f ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Model')
    p = mdb.models['Model-1'].parts['Tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Tool']
    p.ReferencePoint(point=(0.0, 40, 20))
    mdb.models['Model-1'].parts['Tool'].features.changeKey(fromName='RP', 
        toName='RP-Tool')
    p = mdb.models['Model-1'].parts['Tool']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-Tool')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=323.164, 
        farPlane=612.976, width=417.134, height=170.663, viewOffsetX=-5.15671, 
        viewOffsetY=-4.56007)
    p = mdb.models['Model-1'].parts['Tool']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3ff ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Tool')
    p = mdb.models['Model-1'].parts['Upper']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Upper']
    p.ReferencePoint(point=(0.0, 80, 10))
    mdb.models['Model-1'].parts['Upper'].features.changeKey(fromName='RP', 
        toName='RP-Upper')
    p = mdb.models['Model-1'].parts['Upper']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-Upper')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=302.182, 
        farPlane=524.232, width=314.504, height=128.674, viewOffsetX=0.116993, 
        viewOffsetY=-0.194986)
    p = mdb.models['Model-1'].parts['Upper']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#fff ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-Upper')
    p = mdb.models['Model-1'].parts['UpperPlate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['UpperPlate']
    p.ReferencePoint(point=(0.0, 67.5867, 10))
    mdb.models['Model-1'].parts['UpperPlate'].features.changeKey(fromName='RP', 
        toName='RP-UpperPlate')
    p = mdb.models['Model-1'].parts['UpperPlate']
    r = p.referencePoints
    refPoints=(r[2], )
    p.Set(referencePoints=refPoints, name='Set-UpperPlate')
    session.viewports['Viewport: 1'].view.setValues(nearPlane=306.3, 
        farPlane=491.317, width=257.016, height=105.154, viewOffsetX=9.47142, 
        viewOffsetY=2.04286)
    p = mdb.models['Model-1'].parts['UpperPlate']
    s = p.faces
    side1Faces = s.getSequenceFromMask(mask=('[#3f ]', ), )
    p.Surface(side1Faces=side1Faces, name='Surf-UpperPlate')
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
    p1 = mdb.models['Model-1'].parts['Model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p1)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=123.65, 
        farPlane=251.048, width=194.889, height=79.7355, viewOffsetX=3.04642, 
        viewOffsetY=-3.52429)
    p = mdb.models['Model-1'].parts['Model']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['Model-1'].parts['Model']
    p.SectionAssignment(region=region, sectionName='Section-Titan', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model-1'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model-1'].parts['Lower']
    a.Instance(name='Lower-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['LowerPlate']
    a.Instance(name='LowerPlate-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Model']
    a.Instance(name='Model-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Tool']
    a.Instance(name='Tool-1', part=p, dependent=ON)
    p = mdb.models['Model-1'].parts['Upper']
    a.Instance(name='Upper-1', part=p, dependent=ON)
    a = mdb.models['Model-1'].rootAssembly
    p = mdb.models['Model-1'].parts['UpperPlate']
    a.Instance(name='UpperPlate-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-1', previous='Initial', 
        timePeriod=0.05)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-2', previous='Step-1', 
        timePeriod=0.05)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-3', previous='Step-2', 
        timePeriod=0.05)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    mdb.models['Model-1'].ExplicitDynamicsStep(name='Step-4', previous='Step-3', 
        timePeriod=0.05)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValuesInStep(
        stepName='Step-4', variables=('S', 'SVAVG', 'PE', 'PEVAVG', 'PEEQ', 
        'PEEQVAVG', 'LE', 'SE', 'U', 'V', 'A', 'RF', 'CSTRESS', 'EVF'), 
        numIntervals=30)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=ON, 
        constraints=ON, connectors=ON, engineeringFeatures=ON, 
        adaptiveMeshConstraints=OFF)
    mdb.models['Model-1'].ContactProperty('IntProp-1')
    mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
        formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
        pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
        table=((0.2, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
        fraction=0.005, elasticSlipStiffness=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, 
        interactions=OFF, constraints=OFF, connectors=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Model']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
        engineeringFeatures=OFF, mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['Model-1'].parts['Model']
    p.seedPart(size=3.5, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Model']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Lower']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Lower']
    p.seedPart(size=10, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Lower']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['LowerPlate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['LowerPlate']
    p.seedPart(size=15, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['LowerPlate']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Tool']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Tool']
    p.seedPart(size=15, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Tool']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['Upper']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['Upper']
    p.seedPart(size=10, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['Upper']
    p.generateMesh()
    p = mdb.models['Model-1'].parts['UpperPlate']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['Model-1'].parts['UpperPlate']
    p.seedPart(size=15, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['Model-1'].parts['UpperPlate']
    p.generateMesh()
    a = mdb.models['Model-1'].rootAssembly
    a.regenerate()
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, 
        interactions=ON, constraints=ON, connectors=ON, engineeringFeatures=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['Upper-1'].surfaces['Surf-Upper']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Upper', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    mdb.models['Model-1'].interactions['Upper'].setValuesInStep(stepName='Step-3', 
        activeInStep=False)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['Tool-1'].surfaces['Surf-Tool']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Tool', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['Lower-1'].surfaces['Surf-Lower']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='Lower', 
        createStepName='Step-1', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    mdb.models['Model-1'].interactions['Lower'].setValuesInStep(stepName='Step-3', 
        activeInStep=False)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['UpperPlate-1'].surfaces['Surf-UpperPlate']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='UpperPlate', 
        createStepName='Step-3', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    a = mdb.models['Model-1'].rootAssembly
    region1=a.instances['LowerPlate-1'].surfaces['Surf-LowerPlate']
    a = mdb.models['Model-1'].rootAssembly
    region2=a.instances['Model-1'].surfaces['Surf-Model']
    mdb.models['Model-1'].SurfaceToSurfaceContactExp(name ='LowerPlate', 
        createStepName='Step-3', master = region1, slave = region2, 
        mechanicalConstraint=KINEMATIC, sliding=FINITE, 
        interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
        clearanceRegion=None)
    mdb.models['Model-1'].TabularAmplitude(name='Amp-1', timeSpan=STEP, 
        smooth=SOLVER_DEFAULT, data=((0.0, 0.0), (1.0, 1.0)))
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, interactions=OFF, constraints=OFF, 
        engineeringFeatures=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Upper-1'].sets['Set-Upper']
    mdb.models['Model-1'].DisplacementBC(name='Fix-Upper', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['UpperPlate-1'].sets['Set-UpperPlate']
    mdb.models['Model-1'].DisplacementBC(name='Fix-UpperPlate', 
        createStepName='Step-1', region=region, u1=0.0, u2=UNSET, u3=0.0, 
        ur1=0.0, ur2=0.0, ur3=0.0, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Tool-1'].sets['Set-Tool']
    mdb.models['Model-1'].DisplacementBC(name='Fix-Tool', createStepName='Step-1', 
        region=region, u1=0.0, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['LowerPlate-1'].sets['Set-LowerPlate']
    mdb.models['Model-1'].DisplacementBC(name='Fix-LowerPlate', 
        createStepName='Step-1', region=region, u1=0.0, u2=UNSET, u3=0.0, 
        ur1=0.0, ur2=0.0, ur3=0.0, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Lower-1'].sets['Set-Lower']
    mdb.models['Model-1'].DisplacementBC(name='Fix-Lower', createStepName='Step-1', 
        region=region, u1=0.0, u2=UNSET, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
        amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='', 
        localCsys=None)
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Upper-1'].sets['Set-Upper']
    mdb.models['Model-1'].DisplacementBC(name='Load-Upper', 
        createStepName='Step-1', region=region, u1=UNSET, u2=-560, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
    mdb.models['Model-1'].boundaryConditions['Load-Upper'].setValuesInStep(
        stepName='Step-2', u2=0.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['Lower-1'].sets['Set-Lower']
    mdb.models['Model-1'].DisplacementBC(name='Load-Lower', 
        createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-2')
    mdb.models['Model-1'].boundaryConditions['Load-Lower'].setValuesInStep(
        stepName='Step-2', u2=560)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    mdb.models['Model-1'].boundaryConditions['Load-Lower'].setValuesInStep(
        stepName='Step-3', u2=0.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['UpperPlate-1'].sets['Set-UpperPlate']
    mdb.models['Model-1'].DisplacementBC(name='Load-UpperPlate', 
        createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-3')
    mdb.models['Model-1'].boundaryConditions['Load-UpperPlate'].setValuesInStep(
        stepName='Step-3', u2=-335.734)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')
    mdb.models['Model-1'].boundaryConditions['Load-UpperPlate'].setValuesInStep(
        stepName='Step-4', u2=0.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
    a = mdb.models['Model-1'].rootAssembly
    region = a.instances['LowerPlate-1'].sets['Set-LowerPlate']
    mdb.models['Model-1'].DisplacementBC(name='Load-LoerPlate', 
        createStepName='Step-1', region=region, u1=UNSET, u2=0.0, u3=UNSET, 
        ur1=UNSET, ur2=UNSET, ur3=UNSET, amplitude='Amp-1', fixed=OFF, 
        distributionType=UNIFORM, fieldName='', localCsys=None)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-4')
    mdb.models['Model-1'].boundaryConditions['Load-LoerPlate'].setValuesInStep(
        stepName='Step-4', u2=320.628)
    mdb.saveAs(pathName='D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle30 Friction0.2/cae')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', parallelizationMethodExplicit=DOMAIN, numDomains=2, 
        activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=2)
    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
Macro1()

