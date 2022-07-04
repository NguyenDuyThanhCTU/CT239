from datetime import date
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import style

def thisyear():
    YEAR = date.today()
    return YEAR.year
def lastyear():
    YEAR = date.today()
    result = YEAR.year
    return result -1

def Option1(self):

    df = pd.read_csv(self)
    df.head()

    Tsan = df['TÀI SẢN']
    This_year = df['ThisYear']

    fig = plt.figure(figsize=(15,10))
    if(self == "Data/DataFinal.csv"):
        plt.bar(Tsan,This_year,color ='blue')
    else:
        plt.barh(Tsan,This_year,color ='blue')
    plt.xlabel('Tsan')
    plt.ylabel(thisyear())
    plt.title('tittle')
    plt.show()


def Option2(self):
    df = pd.read_csv(self)
    df.head()

    Tsan = df['TÀI SẢN']
    last_year = df['LastYear']

    fig = plt.figure(figsize=(15,10))
    if(self == "Data/DataFinal.csv"):
        plt.bar(Tsan,last_year,color ='red')
    else:
        plt.barh(Tsan,last_year,color ='red')
    plt.xlabel('Tsan')
    plt.ylabel(lastyear())
    plt.title('tittle')
    plt.show()

def Option3(self):
    df = pd.read_csv(self)
    df.head()

    this_year = df['ThisYear']
    last_year = df['LastYear']
    Tsan = df['TÀI SẢN']

    xpos = np.arange(len(Tsan))
    xpos

    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.title('BIỂU ĐỒ SO SÁNH SỰ CHÊNH LỆCH GIÁ TRỊ CỦA TÀI SẢN')
    if(self == "Data/DataFinal.csv"):
        plt.bar(xpos,this_year, color ='blue',width= barWidth, label= 'this year')
        plt.bar(xpos,last_year, color ='red',width= barWidth, label= 'last year')
        plt.xlabel('Tài sản')
        plt.ylabel('')
        plt.legend()
        plt.xticks(xpos,('Tài sản ngắn hạn','Tài sản dài hạn','Tổng cộng tài sản','Nợ phải trả','Tổng cộng nguồn vốn'))
    else:
        plt.barh(xpos,this_year, color ='blue', label= 'this year')
        plt.barh(xpos,last_year, color ='red', label= 'last year')
        plt.yticks(xpos,('Tiền và các khoản tương đương tiền','Các khoản đầu tư tài chính ngắn hạn','Các khoản phải thu','Hàng tồn kho','Tài sản ngắn hạn khác','Phải thu dài hạn','Tài sản cố định','Bất động sản đầu tư','Tài sản dở dang dài hạn','Đầu tư tài chính dài hạn','Tài sản dài hạn khác','Nợ ngắn hạn','Nợ dài hạn','Vốn chủ sở hữu'))
        plt.xlabel('')
        plt.ylabel('Tài sản')
        plt.legend()
    plt.show()

def center_window_on_screen1(root):

    window_width = 300
    window_height = 100

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    screen = (f'{window_width}x{window_height}+{center_x}+{center_y}')
    return screen

def Option5(self,self1,self2):
    # self = final
    # self1 = new
    Data = 0
    Data1 = 0
    Data2 = 0
    Data3 = 0
    Data4 = 0
    Data5 = 0
    file = open(self,mode="r",encoding="utf-8-sig")
    header = file.readline()
    row = file.readline()
    flag = 0

    while row != "":
        row_list = row.split(",")

        ThisYear = float(row_list[1])
        LastYear = float(row_list[2])
        if(flag == 0):
            Data = Data + ThisYear
            Data1 = Data1 + LastYear
            break
        row = file.readline()
        flag = flag + 1
    
    

    file1 = open(self1,mode="r",encoding="utf-8-sig")
    header = file1.readline()
    
    row1 = file1.readline()
    flag1 = 0

    while row1 != "":
        row_list1 = row1.split(",")

        ThisYear1 = float(row_list1[1])
        LastYear1 = float(row_list1[2])

        if(flag1 == 3):
            Data4 = Data4 + ThisYear1
            Data5 = Data5 + LastYear1

        elif(flag1 == 11):
            Data2 = Data2 + ThisYear1
            Data3 = Data3 + LastYear1
            break

        row1 = file1.readline()
        flag1 = flag1 + 1
    
    
    if(self2 == 1):
        Rc_ThisYear = round((Data/Data2),3)
        Rc_LasYear = round((Data1 / Data3),3)

        this_yearRc = (Rc_ThisYear,Rc_LasYear)
        defaultRc = (1, 1)
        year = (2020,2019)

        xpos = np.arange(len(year))
        xpos
        style.use('ggplot')
        plt.figure(figsize=(10,7))
        barWidth = 0.2
        plt.title('KHẢ NĂNG THANH TOÁN NỢ CỦA DOANH NGHIỆP ')
        plt.bar(xpos,this_yearRc, color ='blue',width= barWidth, label= 'Khả năng thanh toán hiện thời')
        plt.bar(xpos,defaultRc, color ='red',width= barWidth, label= 'Default')
        if(Rc_ThisYear > 0.5 and Rc_LasYear> 0.5):
            plt.xlabel('khả năng thanh toán nợ đến hạn năm 2020 được đảm bảo \n khả năng thanh toán nợ đến hạn năm 2019 được đảm bảo')
        elif(Rc_ThisYear < 0.5 and Rc_LasYear> 0.5):
            plt.xlabel('khả năng thanh toán nợ đến hạn năm 2020 không được đảm bảo\n khả năng thanh toán nợ đến hạn năm 2019 được đảm bảo')
        elif(Rc_ThisYear >0.5 and Rc_LasYear< 0.5):
            plt.xlabel('khả năng thanh toán nợ đến hạn năm 2020 được đảm bảo\n khả năng thanh toán nợ đến hạn năm 2019 không được đảm bảo')
        else:
            plt.xlabel('khả năng thanh toán nợ đến hạn năm 2020 không được đảm bảo\n khả năng thanh toán nợ đến hạn năm 2019 không được đảm bảo')

        plt.ylabel('Tỷ (VNĐ)')
        plt.legend()
        plt.xticks(xpos,('2020','2019'))
        plt.show()

    elif(self2 == 2):
        Rq_ThisYear = round(((Data - Data4)/ Data2),3)
        Rq_LastYear = round(((Data - Data5)/ Data2),3)

        this_yearRc = (Rq_ThisYear,Rq_LastYear)
        defaultRc = (0.5, 0.5)
        year = (2020,2019)

        xpos = np.arange(len(year))
        xpos
        style.use('ggplot')
        plt.figure(figsize=(10,7))
        barWidth = 0.2
        plt.title('THANH KHOẢNG CỦA DOANH NGHIỆP ')
        plt.bar(xpos,this_yearRc, color ='blue',width= barWidth, label= 'Khả năng thanh toán hiện thời')
        plt.bar(xpos,defaultRc, color ='red',width= barWidth, label= 'Default')
        if(Rq_ThisYear > 0.5 and Rq_LastYear> 0.5):
            plt.xlabel('thanh khoản của doanh nghiệp vào năm 2020 TỐT\n thanh khoản của doanh nghiệp vào năm 2019 TỐT')
        elif(Rq_ThisYear < 0.5 and Rq_LastYear> 0.5):
            plt.xlabel('thanh khoản của doanh nghiệp vào năm 2020 KHÔNG TỐT\n thanh khoản của doanh nghiệp vào năm 2019 TỐT')
        elif(Rq_ThisYear >0.5 and Rq_LastYear< 0.5):
            plt.xlabel('thanh khoản của doanh nghiệp vào năm 2020 TỐT\n thanh khoản của doanh nghiệp vào năm 2019 KHÔNG TỐT')
        else:
            plt.xlabel('thanh khoản của doanh nghiệp vào năm 2020 KHÔNG TỐT\n thanh khoản của doanh nghiệp vào năm 2019 KHÔNG TỐT')
        
        plt.ylabel('Tỷ (VNĐ)')
        plt.legend()
        plt.xticks(xpos,('2020','2019'))
        plt.show()

    # 
    file1.close()
    file.close()  

def Option6():

    VQHTK_Thisyear = round(7.210/1.052,3)
    VQHTK_Lastyear = round((8.324/1.060),3)

    SNTK_Thisyear = round(365/VQHTK_Thisyear,0)
    SNTK_Lastyear =round(365/VQHTK_Lastyear,0)

    VQHTK = (VQHTK_Thisyear,SNTK_Thisyear)
    SNTK = (VQHTK_Lastyear, SNTK_Lastyear)
    year = (2020,2019)

    xpos = np.arange(len(year))
    xpos
    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.title('TỶ SỐ VỀ HOẠT ĐỘNG ')
    plt.bar(xpos,VQHTK, color ='blue',width= barWidth, label= '2020')
    plt.bar(xpos+0.2,SNTK, color ='red',width= barWidth, label= '2019')
    comment = "Năm 2020 Hàng tồn kho quay được {} vòng một năm để tạo ra doanh thu và như vậy bình quân hàng tồn kho mất hết {} ngày.\nNăm 2019 Hàng tồn kho quay được {} vòng một năm để tạo ra doanh thu và như vậy bình quân hàng tồn kho mất hết {} ngày.".format(VQHTK_Thisyear,SNTK_Thisyear,VQHTK_Lastyear,SNTK_Lastyear)
    plt.xlabel(comment)


    plt.ylabel('Tỷ (VNĐ)')
    plt.legend()
    plt.xticks(xpos,('Vòng quay hàng tồn kho ','Số ngày tồn kho '))
    plt.show()

def Option7():
    TS_thisyear = round((3.777/11.932),3)
    VCSH_thisyear = round((3.777/8.156 ),3)
    Rp_thisyear = round((283+153/153),3)

    TS_lastyear = round((4.650/12.349 ),3)
    VCSH_lastyear = round((4.650/7.699 ),3)
    Rp_lastyear = round((416 + 124/124 ),3)


    VQHTK = (TS_thisyear,VCSH_thisyear,Rp_thisyear)
    SNTK = (TS_lastyear, VCSH_lastyear,Rp_lastyear)
    year = (0,1,2)

    xpos = np.arange(len(year))
    xpos
    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.title('TỶ SỐ VỀ CƠ CẤU TÀI CHÍNH')
    plt.bar(xpos,VQHTK, color ='blue',width= barWidth, label= '2020')
    plt.bar(xpos+0.2,SNTK, color ='red',width= barWidth, label= '2019')
    if(TS_thisyear >0 and VCSH_thisyear > 0 and Rp_thisyear> 0):
        plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2020 cao ít sử dụng nợ")
    else:
        plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2020 thấp còn sử dụng nợ")
    
    if(TS_lastyear >0 and VCSH_lastyear > 0 and Rp_lastyear> 0):
        plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2019 cao ít sử dụng nợ")
    else:
        plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2019 thấp còn sử dụng nợ")
    

    plt.ylabel('Tỷ (VNĐ)')
    plt.legend()
    plt.xticks(xpos,('Tỷ số nợ/ Tổng TS','Tỷ số nợ/Vốn chủ sở hữu  ','Khả năng thanh toán lãi vay '))
    plt.show()



def Option8():
    ROS_thisyear = round((207/7.210),3)
    ROA_thisyear = round((207/ ((11.932+12.534)/2)),3)
    ROE_thisyear = round((207/ ((8.156+8.358)/2)),3)

    ROS_lastyear = round((330/8.324  ),3)
    ROA_thisyear= round((330/ ((12.349 + 11.932)/2) ),3)
    ROE_lastyear = round(330/ ((7.699+8.156)/2),3)


    VQHTK = (ROS_thisyear,ROA_thisyear,ROE_thisyear)
    SNTK = (ROS_lastyear, ROA_thisyear,ROE_lastyear)
    year = (0,1,2)

    xpos = np.arange(len(year))
    xpos
    style.use('ggplot')
    plt.figure(figsize=(10,7))
    barWidth = 0.2
    plt.title('TỶ SỐ VỀ DOANH LỢI ')
    plt.bar(xpos,VQHTK, color ='blue',width= barWidth, label= '2020')
    plt.bar(xpos+0.2,SNTK, color ='red',width= barWidth, label= '2019')
    # if(TS_thisyear >0 and VCSH_thisyear > 0 and Rp_thisyear> 0):
    #     plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2020 cao ít sử dụng nợ")
    # else:
    #     plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2020 thấp còn sử dụng nợ")
    
    # if(TS_lastyear >0 and VCSH_lastyear > 0 and Rp_lastyear> 0):
    #     plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2019 cao ít sử dụng nợ")
    # else:
    #     plt.xlabel("Khả năng tự chủ tài chính của công ty năm 2019 thấp còn sử dụng nợ")
    

    plt.ylabel('Tỷ (VNĐ)')
    plt.legend()
    plt.xticks(xpos,('Doanh lợi tiêu thụ ','Doanh lợi tài sản ','Doanh lợi vốn chủ sở hữu'))
    plt.show()



