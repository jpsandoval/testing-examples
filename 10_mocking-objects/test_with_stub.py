from order import Order
from mail_service import MailService
#from warehouse import Warehouse
import unittest

class MailServiceStub(MailService):
    def __init__(self):
        self.messages =[]
    def sendOrder(self, message):
        self.messages.append(message)
    def numberOfMessages(self):
        return len(self.messages)

class TestDemoMethods(unittest.TestCase):
    # este test evalua la clase Order
    # sin depender de la implementacion original de MailService
    
    def test(self):
        order = Order("iPhone 14",10)
        stub = MailServiceStub()
        order.setEmailService(stub)
        order.sendByEmail()
        self.assertEqual(stub.numberOfMessages(),1)

