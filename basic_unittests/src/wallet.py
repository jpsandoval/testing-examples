from sre_constants import SUCCESS

class Printer:
    def print(self, string):
        print(string)

class PrinterStub(Printer):
    def __init__(self):
        self.result =""
    def print(self, string):
        self.result += string
    def printedString(self):
        return self.result

class Wallet:
    def __init__(self, owner):
        self.balance = 0
        self.ownerName = owner

    def deposit(self, amount):
        self.balance += amount

    def totalBalance(self):
        return self.balance

    def printInfo(self,printer):
        printer.print(self.ownerName)
        printer.print(str(self.balance))



    def withdraw(self, amount): 
        if amount < self.balance:
            self.balance -= amount
        else:
            raise Exception("not enough minerals")    