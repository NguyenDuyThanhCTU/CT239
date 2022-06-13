import DAO


class UserIdDAO:
    def __init__(self) -> None:
        pass

    @property
    def ID(self):
        return self._ID
    
    @ID.setter
    def ID(self,value):
        self._ID = value

    @ID.setter
    def ID(self,value):
        self._ID = value
    def __init__(self) -> None:
        pass

    def CreateUserID(self):
        conn = DAO.connectDatabase()
        cursor = conn.cursor() 
        return

    def ReadUserID(self):
        conn = DAO.connectDatabase()
        cursor = conn.cursor() 

        for row in cursor.execute("select * from user_ID where ID = '25122001'"):
            print(row.ID)
        

    def UpdateUserID(self):
        return

    def DeleteUserID(self):
        return 


    pass

test1 = UserIdDAO()

test1.ReadUserID()


