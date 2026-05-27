class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}") 
        # print(f"{cls.RAM}") # error    
       

    def get_info(self): # instance variable
         print(f"laptop has {self.RAM} & {self.storage} {self.storage_type}")   


l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb","256gb")      

Laptop.get_storage_type()
l1.get_storage_type() # valid