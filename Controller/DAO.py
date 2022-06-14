from lib2to3.pgen2.driver import Driver
from numpy import less
import pyodbc 

def connectDatabase():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=RITA\SQLEXPRESS; Database=FRS; UID=sa; PWD=1234')
    return conn

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=RITA\SQLEXPRESS; Database=FRS; UID=sa; PWD=1234')
# cursor = conn.cursor()
# print(conn)


# cursor.execute("insert into user_ID (ID, SDT) values ('25122001','092387930')")
# sql = "select * from user_ID"
# # # cursor.execute(sql)
# for row in cursor.execute(sql):
#     print(row.ID)
    # print(row.SDT)



