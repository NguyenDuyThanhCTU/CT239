
from tkinter import *
import  tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
import Controller.DAO as Conn

import Main

class Register(tk.Tk):
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

        def Signup_clicked():
            if TB_YourID.get() == ("") or TB_Phone.get() == (""):
                showwarning(title='Error', message='Vui lòng nhập ID và số điện thoại !')
            else:
                click = askyesno(title='Success', message='Tiếp tục ?')
                if click == 1:
                    # try:
                        Id = TB_YourID.get()
                        Phone = TB_Phone.get()
                        

                        conn = Conn.connectDatabase()
                        cursor = conn.cursor()
                        # sql = "select * from user_ID"
                        # for row in cursor.execute(sql):
                        #     print(row)

                        # sql_ID = """select * from user_ID where ID ='{}' and SDT = '{});'""".format(Id,Phone)
                        sql_ID = "select * from user_ID"
                        #loop 1 phat ra dinh 1 trong 3 truong hop
                        flag = True
                        for row in cursor.execute(sql_ID):
                            if Id == row.ID: 
                                showwarning(title='Error', message='ID đã tồn tại !')
                                # khong break no se tiep tuc vong lap
                                flag = False
                                break
                            elif Phone == row.SDT: 
                                showwarning(title='Error', message='Số điện thoại đã tồn tại!')
                                flag = False
                                break                                
                        if flag == True:
                            sql = "insert into user_ID (ID,SDT) values ('{}','{}');".format(Id, Phone)
                            cursor.execute(sql)
                            showinfo(title='success', message='Tạo ID thành công')
                            conn.commit()
                            TB_YourID.delete(0,'end')
                            TB_Phone.delete(0,'end')
                               
                        conn.close()         
                        
                           
                    # except:
                    #     print("Connect error !!!")
        
        img_sigup = PhotoImage(file = f"assets/img/Register/Button_Signup.png")
        button_sigup = Button(
            image = img_sigup,
            borderwidth = 0,
            highlightthickness = 0,
            command = Signup_clicked,
            relief = "flat")

        button_sigup.place(
            x = 100, y = 400,
            width = 244,
            height = 58)

        def back_clicked():
            self.destroy()
            move = Main.main()

            

        img_back = PhotoImage(file = f"assets/img/Register/back.png")
        button_back = Button(
        image = img_back,
        borderwidth = 0,
        highlightthickness = 0,
        command = back_clicked,
        relief = "flat")

        button_back.place(
        x = 10, y = 460,
        width = 29,
        height = 29)


        self.resizable(False,False)
        self.mainloop()


class Fogot(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fogot ID")

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

        background_img = PhotoImage(file = f"assets/img/Fogot/background.png")
        background = canvas.create_image(
            225, 227,
            image=background_img)

        TextBox_Phone_img = PhotoImage(file = f"assets/img/Fogot/TextBox_Phone.png")
        TextBox_Phone_bg = canvas.create_image(
            220, 262,
            image = TextBox_Phone_img)

        TextBox_Phone = Entry(
            bd = 0,
            bg = "#ffffff",
            highlightthickness = 0)

        TextBox_Phone.place(
            x = 60, y = 250,
            width = 332,
            height = 23)

        def next_clicked():
            Phone = TextBox_Phone.get()
            if Phone == (""):
                showerror(title='Error',message='Số điện thoại không được để trống !')
            else:
                conn = Conn.connectDatabase()
                cursor = conn.cursor()
                sql = "select ID from user_ID where SDT = {};".format(Phone)
                flag = True
                for row in cursor.execute(sql):
                    if row.ID != (""):
                        flag = False
                        data = row.ID
                if flag == False:
                    showinfo(title='Your ID',message='ID của bạn là: {}'.format(data))
                else:
                    showerror(title='error',message='ID hoặc số điện thoại không tồn tại!')



            

        img_next = PhotoImage(file = f"assets/img/Fogot/next.png")
        button_next = Button(
            image = img_next,
            borderwidth = 0,
            highlightthickness = 0,
            command = next_clicked,
            relief = "flat")

        button_next.place(
            x = 130, y = 400,
            width = 188,
            height = 58)

        def back_clicked():
            self.destroy()
            move = Main.main()

        img_back = PhotoImage(file = f"assets/img/Fogot/back.png")
        button_back = Button(
            image = img_back,
            borderwidth = 0,
            highlightthickness = 0,
            command = back_clicked,
            relief = "flat")

        button_back.place(
            x = 10, y = 460,
            width = 29,
            height = 29)

        self.resizable(False, False)
        self.mainloop()
    
thanh = Fogot()
















