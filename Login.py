
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Register import App




class main(tk.Tk):
    def __init__(self):
        super().__init__()
       
        self.title("Login")

        self.iconbitmap('../assets/img/logo/logo.ico')


        window_width = 1000
        window_height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.configure(bg = "#ffffff")


        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
            
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"../assets/img/login/background.png")
        background = canvas.create_image(
            470, 300,
            image=background_img)

        TextBox_ID_img = PhotoImage(file = '../assets/img/login/TextBox_ID.png')
        TextBox_ID_bg = canvas.create_image(
            745, 260,
            image = TextBox_ID_img)

        Tb_ID = Entry(
            bd = 0,
            bg = "#d8d8d8",
            highlightthickness = 0)

        Tb_ID.place(
            x = 570, y = 232,
            width = 350.0,
            height = 59)
        
        def btn_clicked():
            print("Button Clicked")

        Button_Start = PhotoImage(file = f"../assets/img/login/Button_Start.png")
        Bt_Start = Button(
            image = Button_Start,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        Bt_Start.place(
            x = 663, y = 418,
            width = 159,
            height = 50)

        def btn_Register():
            self.destroy()
            # Start = main()
            thanh = App()  

        Button_CreateID = PhotoImage(file = f"../assets/img/login/Button_CreateID.png")
        Bt_CreateID = Button(
            image = Button_CreateID,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_Register,
            relief = "flat")

        Bt_CreateID.place(
            x = 845.5, y = 530,
            width = 96,
            height = 16)

        Button_Fogot = PhotoImage(file = f"../assets/img/login/Button_Fogot.png")
        Bt_Fogot = Button(
            image = Button_Fogot,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        Bt_Fogot.place(
            x = 850, y = 510,
            width = 96,
            height = 16)

        self.resizable(False, False)
        self.mainloop()

Start = main()
