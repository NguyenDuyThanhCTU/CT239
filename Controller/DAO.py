from lib2to3.pgen2.driver import Driver
from numpy import less
import pyodbc 

# def connectDatabase(self):
#     conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=RITA\SQLEXPRESS; Database=FRS; UID=sa; PWD=1234')
#     return conn

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=RITA\SQLEXPRESS; Database=FRS; UID=sa; PWD=1234')
cursor = conn.cursor()

sql = "select * from user_ID"

for row in cursor.execute(sql):
    print(row)



