
class fileIO:
    def __init__(self) -> None:
        pass

    def readToFile(self):
        file = open('../assets/tempIO/Book1.csv',mode="r",encoding="utf-8-sig")

        header = file.readline()

        row = file.readline()
        row_list = row.split(",")

        Data_2020 = row_list[1]
        Data_2019 = row_list[2]   
        # print(row_list)
        print(row_list)
    pass


Thanh = fileIO()

Thanh.readToFile()