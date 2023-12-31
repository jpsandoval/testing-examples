from unittest.mock import MagicMock
from unittest.mock import patch
from order import Order
#from warehouse import Warehouse
import unittest

class TestDemoMethods(unittest.TestCase):
    # este test evalua la clase Order
    # sin depender de la implementacion original de MailService
    
    @patch('warehouse.Warehouse')
    def test2(self,Warehouse):
        order = Order("iPhone 14",10)
        house = Warehouse()
        house.quantityOnStock = MagicMock(return_value=6)
        available = order.checkAvailability(house)
        self.assertFalse(available)

