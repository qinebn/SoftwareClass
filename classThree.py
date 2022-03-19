import numpy as np
import pandas as pd
import sys


data = pd.read_csv(sys.argv[1], encoding='gbk', header=None)
data = np.array(data)
lastLabel = ''
nowLabel = ''
resData = []
lenArgv = len(sys.argv)
if lenArgv==3:
    for i in data:
        lastLabel = nowLabel
        nowLabel = i[0][0:3]
        if nowLabel != lastLabel:
            resData.append('\n'+nowLabel+'\n')
        resData.append(i[0][4:]+'\n')
elif lenArgv==4:
    resData.append('\n' + sys.argv[3] + '\n')
    for i in data:
        nowLabel = i[0][0:3]
        if nowLabel==sys.argv[3]:
            resData.append(i[0][4:]+'\n')
fd = open(sys.argv[2], 'w')
fd.writelines(resData)
fd.close()