
from odbAccess import *

# Open the output database.

odb = openOdb(path='D:/MyProject(31.11.18)/ver1/bin/Debug/Temp 09.12.2018[14.14.06]/Length 40 Width20 Height80 Angle25 Friction0.36/Job-1.odb')

FileStrainS1 = open('StrainS1.csv','w')
FileStressS1 = open('StressS1.csv','w')
FileStrainS2 = open('StrainS2.csv','w')
FileStressS2 = open('StressS2.csv','w')
FileStrainS3 = open('StrainS3.csv','w')
FileStressS3 = open('StressS3.csv','w')
FileStrainS4 = open('StrainS4.csv','w')
FileStressS4 = open('StressS4.csv','w')
FilePEEQ = open('PEEQ.csv','w')
assembly = odb.rootAssembly

# Model data output

# For each instance in the assembly.

numNodes = numElements = 0
# for stepName in odb.steps.keys():
#     print stepName 

lastFrame = odb.steps['Step-1'].frames[-1]
strain=lastFrame.fieldOutputs['LE']
FileStrainS1.write('Element;X;Y;Z;XY;YZ;XZ\n')
for LE in strain.values:
    FileStrainS1.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (LE.elementLabel, LE.data[0], LE.data[1], LE.data[2], LE.data[3], LE.data[4], LE.data[5]))

stress=lastFrame.fieldOutputs['S']
FileStressS1.write('Element;X;Y;Z;XY;YZ;XZ\n')
for S in stress.values:
    FileStressS1.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (S.elementLabel, S.data[0], S.data[1], S.data[2], S.data[3], S.data[4], S.data[5]))

parametr=lastFrame.fieldOutputs['PEEQ']
for PEEQ in parametr.values:
    FilePEEQ.write('%d; %6.4f\n' % (PEEQ.elementLabel, PEEQ.data))

lastFrame = odb.steps['Step-2'].frames[-1]
strain=lastFrame.fieldOutputs['LE']
FileStrainS2.write('Element;X;Y;Z;XY;YZ;XZ\n')
for LE in strain.values:
    FileStrainS2.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (LE.elementLabel, LE.data[0], LE.data[1], LE.data[2], LE.data[3], LE.data[4], LE.data[5]))

stress=lastFrame.fieldOutputs['S']
FileStressS2.write('Element;X;Y;Z;XY;YZ;XZ\n')
for S in stress.values:
    FileStressS2.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (S.elementLabel, S.data[0], S.data[1], S.data[2], S.data[3], S.data[4], S.data[5]))

lastFrame = odb.steps['Step-3'].frames[-1]
strain=lastFrame.fieldOutputs['LE']
FileStrainS3.write('Element;X;Y;Z;XY;YZ;XZ\n')
for LE in strain.values:
    FileStrainS3.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (LE.elementLabel, LE.data[0], LE.data[1], LE.data[2], LE.data[3], LE.data[4], LE.data[5]))

stress=lastFrame.fieldOutputs['S']
FileStressS3.write('Element;X;Y;Z;XY;YZ;XZ\n')
for S in stress.values:
    FileStressS3.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (S.elementLabel, S.data[0], S.data[1], S.data[2], S.data[3], S.data[4], S.data[5]))

lastFrame = odb.steps['Step-4'].frames[-1]
strain=lastFrame.fieldOutputs['LE']
FileStrainS4.write('Element;X;Y;Z;XY;YZ;XZ\n')
for LE in strain.values:
    FileStrainS4.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (LE.elementLabel, LE.data[0], LE.data[1], LE.data[2], LE.data[3], LE.data[4], LE.data[5]))

stress=lastFrame.fieldOutputs['S']
FileStressS4.write('Element;X;Y;Z;XY;YZ;XZ\n')
for S in stress.values:
    FileStressS4.write('%d;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f;%6.4f\n' % (S.elementLabel, S.data[0], S.data[1], S.data[2], S.data[3], S.data[4], S.data[5]))

print 'Number of instances: ', len(assembly.instances)
print 'Total number of elements: ', numElements
print 'Total number of nodes: ', numNodes