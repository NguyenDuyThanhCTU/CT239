import matplotlib.pyplot as plt
import pandas as pd

def namhientai():
    plt.style.use('bmh')

    df = pd.read_csv('DataFinal.csv')
    x = df['TÀI SẢN']
    y = df['2019']

    #bar chart
    plt.xlabel('TÀI SẢN',fontsize=18)
    plt.xlabel('2019',fontsize=16)
    plt.bar(x,y)

    plt.show()