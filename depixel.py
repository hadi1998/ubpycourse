import os
import sys

repairList = [];

for i in range(len(sys.argv)):
    if i != 0:
        repairList.append(i);






def Repair(repairList):
    for j in repairList:
        os.system("potrace -b svg -b pdf {0} -o {1}.pdf".format(j, j[:-4]))
    os.system('echo has been done')
Repair(repairList);