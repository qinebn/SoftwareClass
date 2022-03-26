import numpy as np
import pandas as pd


class yq:
    def __init__(self, input_file_address, out_file_address):
        self.province = ''
        self.input_file_address = input_file_address
        self.out_file_address = out_file_address

    def yq_province(self, province):
        self.province = province
        data = pd.read_csv(self.input_file_address, encoding='gbk', header=None)
        data = np.array(data)
        resData = ['\n' + self.province + '\n']
        for i in data:
            nowLabel = i[0][0:3]
            if nowLabel == self.province:
                resData.append(i[0][4:] + '\n')
        fd = open(self.out_file_address, 'w')
        fd.writelines(resData)
        fd.close()

    def yq_sort(self):
        data = pd.read_table(self.input_file_address, encoding='gbk', header=None)
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
            res.append('\n' + resT[i][0] + '\t' + str(resT[i][1]) + '\n')
            for j in range(len(resT[i][2])):
                res.append(resT[i][2][j][0] + '\t' + str(resT[i][2][j][1]) + '\n')
        fd = open(self.out_file_address, 'w')
        fd.writelines(res)
        fd.close()

    def yq_arrange(self):
        data = pd.read_csv(self.input_file_address, encoding='gbk', header=None)
        data = np.array(data)
        nowLabel = ''
        resData = []
        for i in data:
            lastLabel = nowLabel
            nowLabel = i[0][0:3]
            if nowLabel != lastLabel:
                resData.append('\n'+nowLabel+'\n')
            resData.append(i[0][4:]+'\n')
        fd = open(self.out_file_address, 'w')
        fd.writelines(resData)
        fd.close()
