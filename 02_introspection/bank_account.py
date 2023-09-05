
class BankAccount:
    def __init__(self):
        """ Constructor Documentacion """
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount
 
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("\n Insufficient balance  ")
    
    def getBalance(self):
        return self.balance
    
    def display(self):
        print("\n Net Available Balance=", self.balance)
