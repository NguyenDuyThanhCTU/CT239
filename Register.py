from tkinter import *
import  tkinter as tk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import Controller.DAO as Conn


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sign Up")

        self.iconbitmap('assets/img/logo/logo.ico')

        window_width = 450
        window_height = 500

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.configure(bg = "#ffffff")
        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 500,
            width = 450,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")

        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"assets/img/Register/background.png")
        background = canvas.create_image(
            225, 230,
            image=background_img)

        TB_YourID_img = PhotoImage(file = f"assets/img/Register/TextBox_YourID.png")
        TB_YourID_bg = canvas.create_image(
            212, 265,
            image = TB_YourID_img)

        TB_YourID = Entry(
            self,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        TB_YourID.place(
            x = 60, y = 218,
            width = 332,
            height = 23)

        TB_Phone_img = PhotoImage(file = f"assets/img/Register/TextBox_Phone.png")
        TB_Phone_bg = canvas.create_image(
            59, 318,
            image = TB_Phone_img)

        TB_Phone = Entry(
            self,
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        TB_Phone.place(
            x = 59, y = 318,
            width = 332,
            height = 23)

        def btn_clicked():
            if TB_YourID.get() == ("") and TB_Phone.get() == (""):
                showwarning(title='Error', message='Vui lòng nhập ID và số điện thoại !')
            else:
                click = askyesno(title='Success', message='Tiếp tục ?')
                if click == 1:
                    try:
                        
                        Id = TB_YourID.get()
                        Phone = TB_Phone.get()
                        

                        conn = Conn.connectDatabase()
                        showwarning(title='Error', message='Vui lòng nhập ID và số điện thoại !')
                        cursor = conn.cursor()
                        

                        # sql_ID = """select * from user_ID where ID ='{}' and SDT = '{});'""".format(Id,Phone)
                        sql_ID = "select * from user_ID"
                        
                        for row in cursor.execute(sql_ID):
                            if Id == row.ID: 
                                showwarning(title='Error', message='ID đã tồn tại !')
                            elif Phone == row.SDT:
                                showwarning(title='Error', message='Số điện thoại đã tồn tại!')
                            else:
                                # sql = """insert user_ID value ('{}','{}');""".format(Id, Phone)
                                cursor.execute("insert user_ID value ('"+Id+"','"+Phone+"');")
                                showinfo(title='success', message='Tạo ID thành công')
                        
                        conn.close()    
                    except:
                        print("Connect error !!!")
        
        img0 = PhotoImage(file = f"assets/img/Register/Button_Signup.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 100, y = 400,
            width = 244,
            height = 58)




        self.resizable(False,False)
        self.mainloop()


thanh = App()











