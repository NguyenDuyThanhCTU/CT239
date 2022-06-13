from tkinter import *
from screen2 import *

# def start(root):
#     root.title("screen 1")
#     root.geometry("1000x600")
#     Button(root,text="click",width=20,command=lambda : change(root)).grid()

def change(root):
    root.destroy()
    fun()

# def call():
#     root = Tk()
#     start(root)
#     root.mainloop()

# call()

window = Tk()
window.title("screen 1")
window.geometry("1000x600")

Button(window,text="click",width=20,command=lambda : change(window)).grid()


