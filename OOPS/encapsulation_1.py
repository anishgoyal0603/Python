class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self._balance = balance

acc1 = BankAccount("Rahul Kumar",100_000)

print(acc1._balance)