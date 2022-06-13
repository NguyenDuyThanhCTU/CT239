class Model:
    def __init__(self,Id,Phone):
        self.Id = Id
        self.Phone = Phone
    
    @property
    def Id(self):
        return self.__Id
    
    @property
    def Phone(self):
        return self.__Phone
    
    @Id.setter
    def Id(self,value):
        


    