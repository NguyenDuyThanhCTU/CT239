import matplotlib.pyplot as plt
import pandas as pd

def namhientai(self):
    plt.style.use('bmh')

    df = pd.read_csv(self)
    x = df['TÀI SẢN']
    y = df['2020']

    #bar chart
    plt.xlabel('TÀI SẢN',fontsize=18)
    plt.xlabel('2020',fontsize=16)
    plt.bar(x,y)

    plt.show()

def namtruoc(self):
    plt.style.use('bmh')

    df = pd.read_csv(self)
    x = df['TÀI SẢN']
    y = df['2019']

    #bar chart
    plt.xlabel('TÀI SẢN',fontsize=18)
    plt.xlabel('2019',fontsize=16)
    plt.bar(x,y)

    plt.show()