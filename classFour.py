import pandas as pd
import sys

data = pd.read_table(sys.argv[1], encoding='gbk', header=None)
dataLen = data.shape
res = []
resT = []
nowP = ''
sumT = 0
for i in range(dataLen[0]):
    lastP = nowP
    nowP = data[0][i]
    if nowP != lastP:
        res.sort(key=lambda x: x[1], reverse=True)
        resT.append([lastP, sumT, res])
        res = []
        sumT = 0
    else:
        sumT += data[2][i]
        res.append([data[1][i], data[2][i]])
resT.sort(key=lambda x: x[1], reverse=True)
resT.pop(-1)
res = []
for i in range(len(resT)):
    res.append('\n'+resT[i][0]+'\t'+str(resT[i][1])+'\n')
    for j in range(len(resT[i][2])):
        res.append(resT[i][2][j][0]+'\t'+str(resT[i][2][j][1])+'\n')
fd = open(sys.argv[2], 'w')
fd.writelines(res)
fd.close()


