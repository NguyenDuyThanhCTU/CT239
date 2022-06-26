from numpy import number
from FinancialLeverage import *
import array as arr

def createNewExcelFile():
    file = open("Data.csv",mode="r",encoding="utf-8-sig")
    file_new = open("Data_new.csv", mode="w",encoding="utf-8-sig")

    header = file.readline()

    file_new.write(header.strip() + ",Chênh lệch" + ",Phần trăm\n")

    row = file.readline()
    while row != "":
        row_list = row.split(",")

        last_year = float(row_list[2])
        this_year = float(row_list[1])

        chenhlech = this_year - last_year
        chenhlech1 = ((this_year - last_year)/last_year) * 100
        # bổ sung

        Round = round(chenhlech1,2)

        row_new = row.strip() + "," + str(chenhlech)+ "," + str(Round)+"\n"
        # print(row_list)

        file_new.write(row_new)
        row = file.readline()
    file.close()
    file_new.close()


def tinhtoan():
    file = open("Data_new.csv",mode="r",encoding="utf-8-sig")
    file_new = open("DataFinal.csv", mode="w",encoding="utf-8-sig")
    header = file.readline()
    file_new.write(header.strip()+"\n")
    row = file.readline()
    flag = 0
    data1 = 0
    data2 = 0
    data3 = 0
    data4 = 0
    data5 = 0
    data6 = 0
    data7 = 0
    data8 = 0
    data9 = 0
    data10 = 0
    data11 = 0
    data12 = 0
    data13 = 0
    data14 = 0
    data15 = 0
    data16 = 0
    while row != "":
        row_list = row.split(",")
        c1 = int(row_list[1])
        c2 = int(row_list[2])
        c3 = float(row_list[3])
        c4 = float(row_list[4])

        if(flag <= 4):
            # có thể dùng mảng global nhưng đọc ra nó cũng nhiều như vậy thôi nên dùng mảng local
            a = arr.array('d',[c1])
            b = arr.array('d',[c2])
            c = arr.array('d',[c3])
            d = arr.array('d',[c4])
            data1 = round(data1 + a[0],3) 
            data2 = round(data2 + b[0],3)
            data3 = round(data3 + c[0],3)
            data4 = round(((data1-data2) / data2) *100,3)
            
            # print("thanh dep trai") 
        elif(4 < flag <= 10):
            a = arr.array('d',[c1])
            b = arr.array('d',[c2])
            c = arr.array('d',[c3])
            d = arr.array('d',[c4])

            data5 = round(data5 + a[0],3)
            data6 = round(data6 + b[0],3)
            data7 = round(data7 + c[0],3)
            data8 = round(((data5-data6) / data6) *100,3)
            
        elif(10 < flag <=12):
            a = arr.array('d',[c1])
            b = arr.array('d',[c2])
            c = arr.array('d',[c3])
            d = arr.array('d',[c4])

            data9 = round(data9 + a[0],3)
            data10 = round(data10 + b[0],3)
            data11 = round(data11 + c[0],3)
            data12 = round(((data9-data10) / data10) *100,3)
        else:
            a = arr.array('d',[c1])
            b = arr.array('d',[c2])
            c = arr.array('d',[c3])
            d = arr.array('d',[c4])

            data13 = round(data13 + a[0],3)
            data14 = round(data14 + b[0],3)
            data15 = round(data15 + c[0],3)
            data16 = round(((data13-data14) / data14) *100,3)


        flag += 1
        row = file.readline()

    row_new = row.strip() + "Tài sản ngắn hạn" + "," + str(data1)+ "," + str(data2)+ "," + str(data3)+ "," + str(data4)+"\n"
    file_new.write(row_new)

    row_new1 = row.strip() + "Tài sản dài hạn" + "," + str(data5)+ "," + str(data6)+ "," + str(data7)+ "," + str(data8)+"\n"
    file_new.write(row_new1)

    row_new2 = row.strip() + "Tổng cộng tài sản" + "," + str(data5+data1)+ "," + str(data6+data2)+ "," + str(data7+data3)+ "," + str(data8+data4)+"\n"
    file_new.write(row_new2)

    row_new3 = row.strip() + "Nợ phải trả" + "," + str(data9)+ "," + str(data10)+ "," + str(data11)+ "," + str(data12)+"\n" 
    file_new.write(row_new3)

    row_new4 = row.strip() + "Tổng cộng nguồn vốn" + "," + str(data9+data13)+ "," + str(data10+data14)+ "," + str(data11+data15)+ "," + str(data12+data16)+"\n"  
    file_new.write(row_new4)  


        
    

    

    
    

if __name__ == "__main__":
    start = tinhtoan()

