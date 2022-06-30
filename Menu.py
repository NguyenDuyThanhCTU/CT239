
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showwarning
from tkinter.messagebox import *
from PIL import Image, ImageTk
from numpy import size
from pip import main
import Controller.DAO as Conn
# import Menu
# import User_ID 
from Controller.FinancialLeverage import * 
from Controller.fileIO import *
from Controller.Predictions import *
import matplotlib.pyplot as plt




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



##########################################################################################################
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
        
        self.resizable(False, False)
        self.mainloop()
    


##########################################################################################################
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
            row_list = row.split(",")
            c1 = float(row_list[3])
            c2 = float(row_list[4])
            if(c1 >0):
                TSNN = "Tài sản ngắn hạn của năm hiện tại tăng {}(tỷ) tương đương ({}%) so với năm trước đó".format(c1,c2)
            else:
                TSNN = "Tài sản ngắn hạn của năm hiện tại giảm {}(tỷ) tương đương ({}%) so với năm trước đó".format(c1,c2)
            
            row1 = file.readline()
            row_list1 = row1.split(",")
            c3 = float(row_list1[3])
            c4 = float(row_list1[4])
            if(c3 >0):
                TSDH = "Tài sản dài hạn năm hiện tại tăng {}(tỷ) tương đương ({}%) so với với năm trước đó".format(c3,c4)
            else:
                TSDH = "Tài sản dài hạn năm hiện tại giảm {}(tỷ) tương đương ({}%) so với với năm trước đó".format(c3,c4)        

            row2 = file.readline() 
            row_list2 = row2.split(",")
            c5 = float(row_list2[3])
            c6 = float(row_list2[4])
            if(c5 >0):
                TongCongtaisan = "Tổng cộng tài sản năm hiện tại tăng {}(tỷ) ương đương ({}%) so với với năm trước đó".format(c5,c6)
            else:
                TongCongtaisan = "Tổng cộng tài sản năm hiện tại giảm {}(tỷ) ương đương ({}%) so với với năm trước đó".format(c5,c6)

            row3 = file.readline()
            row_list3 = row3.split(",")
            c7 = float(row_list3[3])
            c8 = float(row_list3[4])
            if(c7 >0):
                NoPhaiTra = "Nợ phải trả năm hiện tại tăng {}(tỷ) tương đương ({}%) so với với năm trước đó".format(c7,c8)
            else:
                NoPhaiTra = "Nợ phải trả năm hiện tại giảm {}(tỷ) tương đương ({}%) so với với năm trước đó".format(c7,c8)

            row4 = file.readline()
            row_list4 = row4.split(",")
            c9 = float(row_list4[3])
            c10 = float(row_list4[4])
            if(c9 >0):
                TongNguonVon = "Tổng nguồn vốn năm hiện tại tăng {}(tỷ) tương đương ({}%) so với với năm trước đó".format(c9,c10)
            else:
                TongNguonVon = "Tổng nguồn vốn năm hiện tại giảm {}(tỷ) tương đương ({}%) so với với năm trước đó".format(c9,c10)

            file.close()
            
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
            file = open("Data/DataFinal.csv",mode="r",encoding="utf-8-sig")

            header = file.readline()

            row = file.readline()
            row_list = row.split(",")
            c1 = float(row_list[2])
            TSNN = "Tài sản ngắn hạn của năm trước đó là: {}(tỷ)".format(c1)
            
            row1 = file.readline()
            row_list1 = row1.split(",")
            c2 = float(row_list1[2])
            TSDH = "Tài sản dài hạn năm của năm trước đó là: {}(tỷ)".format(c2)      

            row2 = file.readline() 
            row_list2 = row2.split(",")
            c3 = float(row_list2[2])
            TongCongtaisan = "Tổng cộng tài sản của năm trước đó là: {}(tỷ)".format(c3)

            row3 = file.readline()
            row_list3 = row3.split(",")
            c4 = float(row_list3[2])
            NoPhaiTra = "Nợ phải trả của năm trước đó là: {}(tỷ)".format(c4)

            row4 = file.readline()
            row_list4 = row4.split(",")
            c5 = float(row_list4[2])
            TongNguonVon = "Tổng nguồn vốn của năm trước đó là: {}(tỷ)".format(c5)
           
            file.close()
            
            label1.configure(text=TSNN+"\n"+TSDH+"\n"+ TongCongtaisan+"\n"+NoPhaiTra+"\n"+TongNguonVon)

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


##########################################################################################################
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


        def ThanhToanNo():
            Option5('Data/DataFinal.csv','Data/Data_new.csv',1)

        def ThanhKhoan():
            Option5('Data/DataFinal.csv','Data/Data_new.csv',2)

        def ChooseChartOption5():
            root = Tk()
            screen = center_window_on_screen1(root)
            data = "{}".format(screen)
            root.title("chọn loại biểu đồ")
            root.geometry(data)
            background = "#FFFFFF"
            Button(root, text='thanh toán nợ ', command=ThanhToanNo).pack(
                ipadx=10,
                ipady=10,
                side='left',
                padx=20
            )
            Button(root, text='thanh khoảng', command=ThanhKhoan).pack(
                ipadx=10,
                ipady=10,
                side='right',
                padx=20
            )
            root.mainloop()
        Button_KhaNangThanhToan = PhotoImage(file = f"assets/img/C1/Button_KhaNangThanhToan.png")
        bt_KhaNangThanhToan = Button(
            image = Button_KhaNangThanhToan,
            borderwidth = 0,
            highlightthickness = 0,
            command = ChooseChartOption5,
            relief = "flat")

        bt_KhaNangThanhToan.place(
            x = 690, y = 98,
            width = 274,
            height = 50)
        
        def HoatDong_clicked():
            Option6()

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
            Option7()

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
            Option8()

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


##########################################################################################################
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

        background_img = PhotoImage(file = f"assets/img/C2/background.png")
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
        
        def DuDoan_clicked():
            DuDoan('Data/DataFinal.csv')

        Button_DuDoan = PhotoImage(file = f"assets/img/C2/Button_DuDoan.png")
        bt_DuDoan = Button(
            image = Button_DuDoan,
            borderwidth = 0,
            highlightthickness = 0,
            command = DuDoan_clicked,
            relief = "flat")

        bt_DuDoan.place(
            x = 667+30, y =336,
            width = 200,
            height = 50)
        
        def KiemTra_clicked():
            Option1('Data/DataFinal.csv')

        Button_KiemTra = PhotoImage(file = f"assets/img/C2/Button_KiemTra.png")
        bt_KiemTra = Button(
            image = Button_KiemTra,
            borderwidth = 0,
            highlightthickness = 0,
            command = KiemTra_clicked,
            relief = "flat")

        bt_KiemTra.place(
            x = 240+30, y = 336,
            width = 200,
            height = 50)

        self.resizable(False, False)
        self.mainloop()

##########################################################################################################
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



    

