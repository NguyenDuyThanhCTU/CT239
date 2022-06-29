
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter.messagebox import *
from PIL import Image, ImageTk
from numpy import size
import Controller.DAO as Conn
# import Menu
# import User_ID 
from Controller.FinancialLeverage import * 
from Controller.fileIO import *
import matplotlib.pyplot as plt
import pandas as pd

# def change_to_Home(self):
#     self.forget()
#     # them pack sau
#     go = HomePage()

# def change_to_C1(self):
#     self.forget()
#     go = C1Page()

# def change_to_C2(self):
#     self.forget()
#     go = C2Page()




def center_window_on_screen(root):

    window_width = 1000
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    screen = (f'{window_width}x{window_height}+{center_x}+{center_y}')
    return screen

def center_window_on_screen1(root):

    window_width = 300
    window_height = 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    screen = (f'{window_width}x{window_height}+{center_x}+{center_y}')
    return screen




class HomePage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

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

        background_img = PhotoImage(file = f"assets/img/Menu/background.png")
        background = canvas.create_image(
            500, 300,
            image=background_img)

        def Home_clicked():
            return

        img_Home = PhotoImage(file = f"assets/img/Menu/Button_Home.png")
        button_home = Button(
            image = img_Home,
            borderwidth = 0,
            highlightthickness = 0,
            command = Home_clicked,
            relief = "flat")

        button_home.place(
            x = 0, y = 200,
            width = 200,
            height = 64)
        
        def C1_clicked():
            self.destroy()
            go = C1Page()

        img_C1 = PhotoImage(file = f"assets/img/Option/Button_C1.png")
        button_C1 = Button(
            image = img_C1,
            borderwidth = 0,
            highlightthickness = 0,
            command = C1_clicked,
            relief = "flat")

        button_C1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        def C2_clicked():
            self.destroy()
            go = C2Page()

        img_C2 = PhotoImage(file = f"assets/img/Option/Button_C2.png")
        button_C2 = Button(
            image = img_C2,
            borderwidth = 0,
            highlightthickness = 0,
            command = C2_clicked,
            relief = "flat")

        button_C2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)

        def Date_clicked():
            print("Button Clicked")

        img_Date = PhotoImage(file = f"assets/img/Menu/Button_Date.png")
        button_Date = Button(
            image = img_Date,
            borderwidth=0,
            highlightthickness=0,
            command=Date_clicked,
            relief = "flat"
        )

        button_Date.place(
            x = 939, y=538,
            width=40,
            height=40
        )
        img_ID = PhotoImage(file = f"assets/img/Menu/1.png")
        label_ID = Label(
            image=img_ID,
            highlightthickness=0,
        )

        label_ID.place(
            x=650, y= 89,
            width=170,
            height=41
        )
        

        self.resizable(False, False)
        self.mainloop()

class Nhanxet(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)
        
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

        background_img = PhotoImage(file = f"assets/img/Nhanxet/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)

        def Exit_clicked():
            self.destroy()
            start = HomePage()

        img0 = PhotoImage(file = f"assets/img/Nhanxet/Button_Exit.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Exit_clicked,
            relief = "flat")

        b0.place(
            x = 817, y = 516,
            width = 159,
            height = 50)
            
        # df = pd.read_csv(self)
        # df.head()

        label1 = Label(
            bg="#E8E8E8",
            anchor=CENTER,
            # fontsize = 50
        )

        label1.place(
            x=28, y=100,
            width=580,height=450,
        )
        # label1.configure(text="File: ")

        def thisyear_clicked():
            file = open("Data/DataFinal.csv",mode="r",encoding="utf-8-sig")

            header = file.readline()
            row = file.readline()

            while row != "":
                row_list = row.split(",")
                c1 = float(row_list[3])
                c2 = float(row_list[4])

                row = file.readline()

            file.close()
            TSNN = "Năm 2020 tăng 564 tỷ (11,48%) so với Tài sản ngắn hạn năm 2019"
            TongCongtaisan = "Năm 2020 tăng 417 tỷ tương đương (3,49%) so với với năm 2019"
            TongNguonVon = "Năm 2020 tổng nguồn vốn tăng 417 tỷ (3,49%) so với 2019"
            NoPhaiTra = "Năm 2020 nợ phải trả tăng 874 tỷ (23,15%)"
            TSDH = "Năm 2020 giảm -147 tỷ (-2.094%) so với Tài sản dài hạn năm 2019"

            label1.configure(text=TSNN+"\n"+TSDH+"\n"+ TongCongtaisan+"\n"+NoPhaiTra+"\n"+TongNguonVon)

        Button_thisyear = PhotoImage(file = f"assets/img/Nhanxet/Button_thisyear.png")

        bt_thisyear = Button(
            image = Button_thisyear,
            borderwidth = 0,
            highlightthickness = 0,
            command = thisyear_clicked,
            relief = "flat")

        bt_thisyear.place(
            x = 634, y = 90,
            width = 254,
            height = 50)

        def lastyear_clicked():
            return

        Button_lastyear = PhotoImage(file = f"assets/img/Nhanxet/Button_lastyear.png")
        bt_lastyear = Button(
            image = Button_lastyear,
            borderwidth = 0,
            highlightthickness = 0,
            command = lastyear_clicked,
            relief = "flat")

        bt_lastyear.place(
            x = 634, y = 182,
            width = 254,
            height = 50)

        self.resizable(False, False)
        self.mainloop()

class C1Page(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

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

        background_img = PhotoImage(file = f"assets/img/C1/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)

        def Home_clicked():
            self.destroy()
            go = HomePage()

        img0 = PhotoImage(file = f"assets/img/Option/Button_Home.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Home_clicked,
            relief = "flat")

        b0.place(
            x = 0, y = 200,
            width = 200,
            height = 64)

        def C1_clicked():
            return

        img1 = PhotoImage(file = f"assets/img/C1/Button_C1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = C1_clicked,
            relief = "flat")

        b1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        def C2_clicked():
            self.destroy()
            go = C2Page()

        img2 = PhotoImage(file = f"assets/img/Option/Button_C2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = C2_clicked,
            relief = "flat")

        b2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)
        
        def Upload_clicked():
            self.destroy()
            go = Upload()

        img3 = PhotoImage(file = f"assets/img/C1/Button_Upload.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = Upload_clicked,
            relief = "flat")

        b3.place(
            x = 493, y =528,
            width = 221,
            height = 50)
        
        def Nhanxet_clicked():
            self.destroy()
            go = Nhanxet()

        Button_nhanxet = PhotoImage(file = f"assets/img/C1/Button_Nhanxet.png")
        bt_nhanxet = Button(
            image = Button_nhanxet,
            borderwidth = 0,
            highlightthickness = 0,
            command = Nhanxet_clicked,
            relief = "flat")

        bt_nhanxet.place(
            x = 226, y = 438,
            width = 274,
            height = 50)

        def DonGianOption1():
            Option1('Data/DataFinal.csv')
        
        def PhucTapOption1():
            Option1('Data/Data_new.csv')

        def ChooseChartOption1():
            root = Tk()
            screen = center_window_on_screen1(root)
            data = "{}".format(screen)
            root.title("chọn loại biểu đồ")
            root.geometry(data)
            Button(root, text='Đơn giản', command=DonGianOption1).pack(
                ipadx=10,
                ipady=10,
                side='left',
                padx=50
            )
            Button(root, text='Phức tạp', command=PhucTapOption1).pack(
                ipadx=10,
                ipady=10,
                side='right',
                padx=20
            )
            root.mainloop()

        Button_Namhientai = PhotoImage(file = f"assets/img/C1/Button_Namhientai.png")
        Bt_Namhientai = Button(
            image = Button_Namhientai,
            borderwidth = 0,
            highlightthickness = 0,
            command = ChooseChartOption1,
            relief = "flat")

        Bt_Namhientai.place(
            x = 226, y = 98,
            width = 274,
            height = 50)

        def DonGianOption2():
            Option2('Data/DataFinal.csv')
        
        def PhucTapOption2():
            Option2('Data/Data_new.csv')

        def ChooseChartOption2():
            root = Tk()
            screen = center_window_on_screen1(root)
            data = "{}".format(screen)
            root.title("chọn loại biểu đồ")
            root.geometry(data)
            Button(root, text='Đơn giản', command=DonGianOption2).pack(
                ipadx=10,
                ipady=10,
                side='left',
                padx=50
            )
            Button(root, text='Phức tạp', command=PhucTapOption2).pack(
                ipadx=10,
                ipady=10,
                side='right',
                padx=20
            )
            root.mainloop()

        Button_Namtruoc = PhotoImage(file = f"assets/img/C1/Button_Namtruoc.png")
        bt_namtruoc = Button(
            image = Button_Namtruoc,
            borderwidth = 0,
            highlightthickness = 0,
            command = ChooseChartOption2,
            relief = "flat")

        bt_namtruoc.place(
            x = 226, y = 215,
            width = 274,
            height = 50)

        def DonGianOption3():
            Option3('Data/DataFinal.csv')
        
        def PhucTapOption3():
            Option3('Data/Data_new.csv')

        def ChooseChartOption3():
            root = Tk()
            screen = center_window_on_screen1(root)
            data = "{}".format(screen)
            root.title("chọn loại biểu đồ")
            root.geometry(data)
            Button(root, text='Đơn giản', command=DonGianOption3).pack(
                ipadx=10,
                ipady=10,
                side='left',
                padx=50
            )
            Button(root, text='Phức tạp', command=PhucTapOption3).pack(
                ipadx=10,
                ipady=10,
                side='right',
                padx=20
            )
            root.mainloop()

        Button_Sosanh = PhotoImage(file = f"assets/img/C1/Button_Sosanh.png")
        bt_sosanh = Button(
            image = Button_Sosanh,
            borderwidth = 0,
            highlightthickness = 0,
            command = ChooseChartOption3,
            relief = "flat")

        bt_sosanh.place(
            x = 226, y = 331,
            width = 274,
            height = 50)


        def KhaNangThanhToan_clicked():
            return

        Button_KhaNangThanhToan = PhotoImage(file = f"assets/img/C1/Button_KhaNangThanhToan.png")
        bt_KhaNangThanhToan = Button(
            image = Button_KhaNangThanhToan,
            borderwidth = 0,
            highlightthickness = 0,
            command = KhaNangThanhToan_clicked,
            relief = "flat")

        bt_KhaNangThanhToan.place(
            x = 690, y = 98,
            width = 274,
            height = 50)
        
        def HoatDong_clicked():
            return

        Button_HoatDong = PhotoImage(file = f"assets/img/C1/Button_HoatDong.png")
        bt_HoatDong = Button(
            image = Button_HoatDong,
            borderwidth = 0,
            highlightthickness = 0,
            command = HoatDong_clicked,
            relief = "flat")

        bt_HoatDong.place(
            x = 690, y = 215,
            width = 274,
            height = 50)
        
        def CoCauTaiChinh_clicked():
            return

        Button_CoCauTaiChinh = PhotoImage(file = f"assets/img/C1/Button_CoCauTaiChinh.png")
        bt_CoCauTaiChinh = Button(
            image = Button_CoCauTaiChinh,
            borderwidth = 0,
            highlightthickness = 0,
            command = CoCauTaiChinh_clicked,
            relief = "flat")

        bt_CoCauTaiChinh.place(
            x = 690, y = 331,
            width = 274,
            height = 50)

        def Doanhloi_clicked():
            return

        Button_DoanhLoi = PhotoImage(file = f"assets/img/C1/Button_Doanhloi.png")
        bt_DoanhLoi = Button(
            image = Button_DoanhLoi,
            borderwidth = 0,
            highlightthickness = 0,
            command = Doanhloi_clicked,
            relief = "flat")

        bt_DoanhLoi.place(
            x = 690, y = 438,
            width = 274,
            height = 50)

        self.resizable(False, False)
        self.mainloop()


class C2Page(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

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

        background_img = PhotoImage(file = f"assets/img/Option/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)

        def Home_clicked():
            self.destroy()
            go = HomePage()

        img0 = PhotoImage(file = f"assets/img/Option/Button_Home.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Home_clicked,
            relief = "flat")

        b0.place(
            x = 0, y = 200,
            width = 200,
            height = 64)

        def C1_clicked():
            self.destroy()
            go = C1Page()

        img1 = PhotoImage(file = f"assets/img/Option/Button_C1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = C1_clicked,
            relief = "flat")

        b1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        def C2_clicked():
            return
        img2 = PhotoImage(file = f"assets/img/C2/Button_C2.png")
        b2 = Button(
            image = img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = C2_clicked,
            relief = "flat")

        b2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)

        self.resizable(False, False)
        self.mainloop()

class Upload(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu")
        self.iconbitmap('assets/img/logo/logo.ico')

        screen = center_window_on_screen(self)
        data = "{}".format(screen)
        self.geometry(data)

        canvas = Canvas(
            self,
            bg = "#ffffff",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"assets/img/Upload/background.png")
        background = canvas.create_image(
            500, 302,
            image=background_img)

        label_showfile = Label(
            bg="#E8E8E8"
        )

        label_showfile.place(
            x=37, y=210,
            width=486,height=258,
        )

        def Select_clicked():
            filepath = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))
            label_showfile.configure(text="File: "+filepath)
            createNewExcelFile(filepath)
            tinhtoan('Data/Data_new.csv')

            


             

        img0 = PhotoImage(file = f"assets/img/Upload/Button_Select.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = Select_clicked,
            relief = "flat")

        b0.place(
            x = 181, y = 504,
            width = 159,
            height = 50)

        def Continue_clicked():
            self.destroy()
            back = HomePage()



        img1 = PhotoImage(file = f"assets/img/Upload/Button_Continue.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = Continue_clicked,
            relief = "flat")

        b1.place(
            x = 763, y = 504,
            width = 159,
            height = 50)
        


        self.resizable(False, False)
        self.mainloop()


if __name__ == "__main__":
    start = HomePage()

    

