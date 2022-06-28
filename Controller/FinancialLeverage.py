from cProfile import label
from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %matplotlib inline
from matplotlib import style

def namhientai(self):
    # plt.style.use('bmh')

    df = pd.read_csv(self)
    df.head()

    Tsan = df['TÀI SẢN']
    This_year = df['2020']

    fig = plt.figure(figsize=(15,10))
    plt.bar(Tsan,This_year,color ='blue')
    plt.xlabel('Tsan')
    plt.ylabel('2020')
    plt.title('tittle')
    plt.show()

    # x = df['TÀI SẢN']
    # y = df['2020']

    # #bar chart
    # plt.xlabel('TÀI SẢN',fontsize=18)
    # plt.xlabel('2020',fontsize=16)
    # plt.bar(x,y)

    # plt.show()


def namtruoc(self):
    df = pd.read_csv(self)
    df.head()

    Tsan = df['TÀI SẢN']
    last_year = df['2019']

    fig = plt.figure(figsize=(15,10))
    plt.bar(Tsan,last_year,color ='red')
    plt.xlabel('Tsan')
    plt.ylabel('2019')
    plt.title('tittle')
    plt.show()

def sosanh(self):
    df = pd.read_csv(self)
    df.head()

    this_year = df['2020']
    last_year = df['2019']
    Tsan = df['TÀI SẢN']

    xpos = np.arange(len(Tsan))
    xpos

    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.bar(xpos,this_year, color ='blue',width= barWidth, label= 'this year')
    plt.bar(xpos,last_year, color ='red',width= barWidth, label= 'last year')
    plt.xlabel('xla')
    plt.ylabel('yla')
    plt.legend()
    plt.xticks(xpos,('Tài sản ngắn hạn','Tài sản dài hạn','Tổng cộng tài sản','Nợ phải trả','Tổng cộng nguồn vốn'))
    plt.title('tittle')
    plt.show()

def nhanxet(self):
    df = pd.read_csv(self)
    df.head()
    label_showfile = Label(
        bg="#E8E8E8"
    )

    label_showfile.place(
        x=37, y=210,
        width=486,height=258,
    )
    label_showfile.configure(text="File: ")

if __name__ == "__main__":
    start = nhanxet('../Data/DataFinal.csv')
