import numpy as np
import pandas as pd
import sys


data = pd.read_csv(sys.argv[1], encoding='gbk')
data = np.array(data)
lastLabel = ''
nowLabel = ''
resData = []
for i in data:
    lastLabel = nowLabel
    nowLabel = i[0][0:3]
    if nowLabel != lastLabel:
        resData.append('\n'+nowLabel+'\n')
    resData.append(i[0][4:]+'\n')
fd = open('yq_out.txt', 'w')
fd.writelines(resData)
fd.close()