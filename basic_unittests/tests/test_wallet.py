import unittest
from src.wallet import *

class TestWalletMethods(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet("juampi")

    def test_deposit(self):
        self.wallet.deposit(10)
        balance = self.wallet.totalBalance()
        self.assertEqual(10, balance)
    
    @unittest.expectedFailure
    def test_withdraw(self):
        self.wallet.deposit(100)
        self.wallet.withdraw(110)

    def test_print(self):
        self.wallet.printInfo(Printer())


    def test_print(self):
        stub = PrinterStub()
        self.wallet.printInfo(stub)
        self.assertEqual(stub.printedString(),"juampi0")


    def tearDown(self):
        # restauración limpieza
        pass

if __name__ == '__main__':
    unittest.main()