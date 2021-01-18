
from odbAccess import *

# Open the output database.

odb = openOdb(path='D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 08.12.2018[14.08.10]/TempCalculat/Job-1.odb')

FileCoordinates = open('Coordinates.csv','w')

assembly = odb.rootAssembly

numNodes = numElements = 0

lastFrame = odb.steps['Step-2'].frames[-1]
strain=lastFrame.fieldOutputs['COORD']
# FileCoordinates.write('Y\n')
for COORD in strain.values:
    FileCoordinates.write('%6.4f\n' % (COORD.data[1]))

FileCoordinates.close()

print 'Number of instances: ', len(assembly.instances)
print 'Total number of elements: ', numElements
print 'Total number of nodes: ', numNodes
