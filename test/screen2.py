

from tkinter import *


def screen2(root):
    root.title("screen 1")
    root.geometry("1000x600")
    Label(root,text="screen 2",width= 20).grid()

def fun():
    root = Tk()
    screen2(root)
    root.mainloop()

class hehe:
    def __init__(self) -> None:
        pass
    def temp():
        window = Tk()

        window.geometry("450x500")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 500,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        background
        background_img = PhotoImage(file = f"background.png")
        background = canvas.create_image(
            -45.0, -67.0,
            image=background_img)
        pass