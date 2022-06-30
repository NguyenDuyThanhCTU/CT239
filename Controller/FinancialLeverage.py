from cProfile import label
from datetime import date
from tkinter import *
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# %matplotlib inline
from matplotlib import style

def thisyear():
    YEAR = date.today()
    return YEAR.year
def lastyear():
    YEAR = date.today()
    result = YEAR.year
    return result -1

def Option1(self):

    df = pd.read_csv(self)
    df.head()

    Tsan = df['TÀI SẢN']
    This_year = df['ThisYear']

    fig = plt.figure(figsize=(15,10))
    if(self == "Data/DataFinal.csv"):
        plt.bar(Tsan,This_year,color ='blue')
    else:
        plt.barh(Tsan,This_year,color ='blue')
    plt.xlabel('Tsan')
    plt.ylabel(thisyear())
    plt.title('tittle')
    plt.show()


def Option2(self):
    df = pd.read_csv(self)
    df.head()

    Tsan = df['TÀI SẢN']
    last_year = df['LastYear']

    fig = plt.figure(figsize=(15,10))
    if(self == "Data/DataFinal.csv"):
        plt.bar(Tsan,last_year,color ='red')
    else:
        plt.barh(Tsan,last_year,color ='red')
    plt.xlabel('Tsan')
    plt.ylabel(lastyear())
    plt.title('tittle')
    plt.show()

def Option3(self):
    df = pd.read_csv(self)
    df.head()

    this_year = df['ThisYear']
    last_year = df['LastYear']
    Tsan = df['TÀI SẢN']

    xpos = np.arange(len(Tsan))
    xpos

    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.title('tittle')
    if(self == "Data/DataFinal.csv"):
        plt.bar(xpos,this_year, color ='blue',width= barWidth, label= 'this year')
        plt.bar(xpos,last_year, color ='red',width= barWidth, label= 'last year')
        plt.xlabel('xla')
        plt.ylabel('yla')
        plt.legend()
        plt.xticks(xpos,('Tài sản ngắn hạn','Tài sản dài hạn','Tổng cộng tài sản','Nợ phải trả','Tổng cộng nguồn vốn'))
    else:
        plt.barh(xpos,this_year, color ='blue', label= 'this year')
        plt.barh(xpos,last_year, color ='red', label= 'last year')
        plt.yticks(xpos,('Tiền và các khoản tương đương tiền','Các khoản đầu tư tài chính ngắn hạn','Các khoản phải thu','Hàng tồn kho','Tài sản ngắn hạn khác','Phải thu dài hạn','Tài sản cố định','Bất động sản đầu tư','Tài sản dở dang dài hạn','Đầu tư tài chính dài hạn','Tài sản dài hạn khác','Nợ ngắn hạn','Nợ dài hạn','Vốn chủ sở hữu'))
        plt.xlabel('xla')
        plt.ylabel('yla')
        plt.legend()
    plt.show()






    

# def sosanh(self):
#     df = pd.read_csv(self)
#     df.head()

#     this_year = df['2020']
#     last_year = df['2019']
#     Tsan = df['TÀI SẢN']

#     xpos = np.arange(len(Tsan))
#     xpos

#     style.use('ggplot')
#     plt.figure(figsize=(10,7))
#     barWidth = 0.2
#     plt.bar(xpos,this_year, color ='blue',width= barWidth, label= 'this year')
#     plt.bar(xpos,last_year, color ='red',width= barWidth, label= 'last year')
#     plt.xlabel('xla')
#     plt.ylabel('yla')
#     plt.legend()
#     plt.xticks(xpos,('Tài sản ngắn hạn','Tài sản dài hạn','Tổng cộng tài sản','Nợ phải trả','Tổng cộng nguồn vốn'))
    
#     plt.show()





# def center_window_on_screen(root):
#     window_width = 1000
#     window_height = 600

#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     center_x = int(screen_width/2 - window_width / 2)
#     center_y = int(screen_height/2 - window_height / 2)

#     screen = (f'{window_width}x{window_height}+{center_x}+{center_y}')
#     return screen


# class Nhanxet(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Menu")
#         self.iconbitmap('../assets/img/logo/logo.ico')

#         screen = center_window_on_screen(self)
#         data = "{}".format(screen)
#         self.geometry(data)
        
#         self.configure(bg = "#ffffff")
#         canvas = Canvas(
#             self,
#             bg = "#ffffff",
#             height = 600,
#             width = 1000,
#             bd = 0,
#             highlightthickness = 0,
#             relief = "ridge")
#         canvas.place(x = 0, y = 0)

#         background_img = PhotoImage(file = f"../assets/img/Nhanxet/background.png")
#         background = canvas.create_image(
#             0.0, 5.5,
#             image=background_img)
            
#         df = pd.read_csv(self)
#         df.head()
#         label_showfile = Label(
#             bg="#E8E8E8"
#         )

#         label_showfile.place(
#             x=37, y=210,
#             width=486,height=258,
#         )
#         label_showfile.configure(text="File: ")

#         self.resizable(False, False)
#         self.mainloop()

# # if __name__ == "__main__":
# Nhanxet()
#     start = Nhanxet()
