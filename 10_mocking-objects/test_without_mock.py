from order import Order
from warehouse import Warehouse
import unittest

class TestDemoMethods(unittest.TestCase):

    
    def test2(self):
        order = Order("iPhone 14",10)
        house = Warehouse()
        available = order.checkAvailability(house)
        self.assertTrue(available)

