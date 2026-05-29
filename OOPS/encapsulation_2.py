class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance # private - data mangling

    def get_balance(self):
        return self.__balance    

    def set_balance(self,new_balance):
        self.__balance = new_balance   

acc1 = BankAccount("Rahul Kumar",100_000)
acc1.set_balance(200_000)
print(acc1.get_balance())

#print(acc1.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'

print(acc1._BankAccount__balance)
