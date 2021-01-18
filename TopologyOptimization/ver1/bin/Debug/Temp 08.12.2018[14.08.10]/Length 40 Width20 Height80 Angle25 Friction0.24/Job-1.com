from driverConstants import *
from driverExplicitMPI import ExplicitMPIAnalysis
import driverUtils, sys
options = {
    'ams':OFF,
    'analysisType':EXPLICIT,
    'applicationName':'analysis',
    'aqua':OFF,
    'ask_delete':OFF,
    'beamSectGen':OFF,
    'biorid':OFF,
    'cavityTypes':[],
    'cavparallel':OFF,
    'complexFrequency':OFF,
    'contact':ON,
    'cosimulation':OFF,
    'coupledProcedure':OFF,
    'cpus':2,
    'cse':OFF,
    'cyclicSymmetryModel':OFF,
    'directCyclic':OFF,
    'domains':2,
    'dsa':OFF,
    'dynamic':OFF,
    'filPrt':[],
    'fils':[],
    'finitesliding':ON,
    'foundation':OFF,
    'geostatic':OFF,
    'heatTransfer':OFF,
    'importer':OFF,
    'importerParts':OFF,
    'includes':[],
    'initialConditionsFile':OFF,
    'input':'Job-1',
    'interactive':None,
    'job':'Job-1',
    'keyword_licenses':[],
    'lanczos':OFF,
    'libs':[],
    'massDiffusion':OFF,
    'memory':'90%',
    'moldflowFiles':[],
    'moldflowMaterial':OFF,
    'mp_mode':MPI,
    'multiphysics':OFF,
    'noDmpDirect':[],
    'noGUI':None,
    'noMultiHost':[],
    'noStdParallel':[],
    'no_domain_check':ON,
    'outputKeywords':ON,
    'parallel':DOMAIN,
    'parallel_odb':SINGLE,
    'parameterized':OFF,
    'partsAndAssemblies':ON,
    'parval':OFF,
    'postOutput':OFF,
    'restart':OFF,
    'restartEndStep':OFF,
    'restartIncrement':0,
    'restartStep':0,
    'restartWrite':ON,
    'rezone':OFF,
    'runCalculator':OFF,
    'soils':OFF,
    'soliter':OFF,
    'solverTypes':['DIRECT', 'DIRECT', 'DIRECT', 'DIRECT'],
    'staticNonlinear':OFF,
    'steadyStateTransport':OFF,
    'step':ON,
    'subGen':OFF,
    'subGenLibs':[],
    'subGenTypes':[],
    'submodel':OFF,
    'substrLibDefs':OFF,
    'substructure':OFF,
    'symmetricModelGeneration':OFF,
    'tmpdir':'C:\\Users\\admin\\AppData\\Local\\Temp',
    'tracer':OFF,
    'visco':OFF,
}
analysis = ExplicitMPIAnalysis(options)
status = analysis.run()
sys.exit(status)
