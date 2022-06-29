from cProfile import label
from tkinter import *
import tkinter as tk
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
