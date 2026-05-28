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

    @staticmethod
    def calc_discount(price,discount):
        final_price = price - (discount * price / 100)
        print(f" discounted price = {final_price}")     


l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb","256gb")      

l1.calc_discount(40000,10) # valid
Laptop.calc_discount(40000,10) # valid