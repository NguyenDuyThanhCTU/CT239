from tkinter import *
import tkinter


def btn_clicked():
    print("Button Clicked")


window = Tk()
window.title("Login")
window.iconbitmap('../assets/img/logo/logo.ico')

window_width = 1000
window_height = 600


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


# window.geometry("1000x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = '../assets/img/login/background.png')
background = canvas.create_image(
    470.0, 300,
    image=background_img)

entry0_img = PhotoImage(file = '../assets/img/login/img_textBox0.png')
entry0_bg = canvas.create_image(
    750, 260,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d8d8d8",
    highlightthickness = 0)

entry0.place(
    x = 570, y = 232,
    width = 350.0,
    height = 59)

img0 = PhotoImage(file = '../assets/img/login/img0.png')
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 663, y = 418,
    width = 159,
    height = 50)

window.resizable(False, False)



window.mainloop()
