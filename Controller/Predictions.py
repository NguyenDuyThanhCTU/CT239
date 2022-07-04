from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %matplotlib inline
from matplotlib import style
def DuDoan(self):
    file = open(self,mode="r",encoding="utf-8-sig")
    header = file.readline()

    flag = 0
    TSNH = 0
    TSDH = 0
    TCTS = 0
    NPT = 0
    TCNV = 0
    row = file.readline()
    while row != "":
        row_list = row.split(",")
        Data = float(row_list[3])
        AI = float(row_list[4])
        if(flag == 0):
            temp = Data * AI
            TSNH = TSNH + temp
        elif(flag == 1):
            temp1 = Data * AI
            TSDH = TSDH + temp1
        elif(flag == 2):
            temp2 = Data * AI
            TCTS = TCTS + temp2
        elif(flag == 3):
            temp3 = Data * AI
            NPT = NPT + temp3
        elif(flag == 4):
            temp4 = Data * AI
            TCNV = TCNV + temp4
        flag = flag +1
        row = file.readline()
        
    file.close()

    FinalData = (TSNH,TSDH,TCTS,NPT,TCNV)
    xpos = np.arange(len(FinalData))
    xpos

    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.bar(xpos,FinalData,color='green',width= barWidth,label = 'Data')
    plt.xticks(xpos,('Điểm dự đoán 1','Điểm dự đoán 2','Điểm dự đoán 3','Điểm dự đoán 4','Điểm dự đoán 5'))
    plt.show()


