class Account:
    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = balance
      
    def deposit(self,deposit_amount):
        self.balance += deposit_amount
        print(f"Balance after deposit is:{self.balance}")
    
    def withdraw(self,withdraw_amount):
        self.balance -= withdraw_amount
        print(f"Balance after withdraw is:{self.balance}")
    
    def showInfo(self):
       print(f"Accno:{self.accno}\nName:{self.name}\nBalance:{self.balance}")
   
    