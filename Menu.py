from tkinter import *
import tkinter as tk
from tkinter import font  as tkfon


class menu(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Menu")
        
        self.iconbitmap('assets/img/logo/logo.ico')
        

        window_width = 1000
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') 

        # vùng chứa là nơi chúng ta sẽ xếp chồng lên nhau nhiều khung
         # chồng lên nhau, rồi đến thứ chúng ta muốn hiển thị
         # sẽ được nâng lên trên những cái khác
        container = tk.Frame(self)
        # container.pack(side="top", fill="both", expand=True)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
 
        self.frames = {}
        for F in (HomePage, C1Page, C2Page):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
 
            # đặt tất cả các trang ở cùng một vị trí;
            # cái ở trên cùng của thứ tự xếp chồng
            # sẽ là một trong những hiển thị.
            frame.grid(row=0, column=0, sticky="nsew")
 
        self.show_frame("HomePage")

        self.mainloop()
 
    def show_frame(self, page_name):
        '''Hiển thị khung cho tên trang đã cho'''
        frame = self.frames[page_name]
        frame.tkraise()



class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
             
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
        
        # def C1_clicked():
        #     print("Button Clicked")

        img_C1 = PhotoImage(file = f"assets/img/Option/Button_C1.png")
        button_C1 = Button(
            image = img_C1,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: controller.show_frame("C1Page"),
            relief = "flat")

        button_C1.place(
            x = -3, y = 264,
            width = 207,
            height = 64)

        button_C1.pack()

        # def C2_clicked():
        #     print("Button Clicked")

        img_C2 = PhotoImage(file = f"assets/img/Option/Button_C2.png")
        button_C2 = Button(
            image = img_C2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: controller.show_frame("C2Page"),
            relief = "flat")

        button_C2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)

        button_C2.pack()

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

        def Option_clicked():
            print("Button Clicked")

        img_Option = PhotoImage(file = f"assets/img/Menu/Button_Option.png")
        button_Option = Button(
            image = img_Option,
            borderwidth=0,
            highlightthickness=0,
            command=Option_clicked,
            relief = "flat"
        )
        button_Option.place(
            x = 811, y=134,
            width=40,
            height=40
        )

        
        self.mainloop()
        
# Start = Menu()


class C1Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
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

        # def Home_clicked():
        #     print("Button Clicked")

        img_Home = PhotoImage(file = f"assets/img/Option/Button_Home.png")
        button_Home = Button(
            image = img_Home,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: controller.show_frame("HomePage"),
            relief = "flat")

        button_Home.place(
            x = 0, y = 200,
            width = 200,
            height = 64)

        button_Home.pack()

        def C1_clicked():
            return

        img_C1 = PhotoImage(file = f"assets/img/C1/Button_C1.png")
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

        # def C2_clicked():
        #     print("Button Clicked")

        img_C2 = PhotoImage(file = f"assets/img/Option/Button_C2.png")
        button_C2 = Button(
            image = img_C2,
            borderwidth = 0,
            highlightthickness = 0,
            command = lambda: controller.show_frame("C2Page"),
            relief = "flat")

        button_C2.place(
            x = -3, y = 328,
            width = 207,
            height = 64)
        
        button_C2.pack()
        
        def Upload_clicked():
            print("Button Clicked")

        img3 = PhotoImage(file = f"assets/img/C1/Button_Upload.png")
        b3 = Button(
            image = img3,
            borderwidth = 0,
            highlightthickness = 0,
            command = Upload_clicked,
            relief = "flat")

        b3.place(
            x = 493, y =508,
            width = 221,
            height = 50)

        self.mainloop()



class C2Page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
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
            print("Button Clicked")

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
            print("Button Clicked")

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
            print("Button Clicked")

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
        
        def Upload_clicked():
            print("Button Clicked")

        self.mainloop()

def go():
    app = menu()
    app.mainloop()
    app.resizable(False,False)        

go()

