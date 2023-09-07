from order import Order
from warehouse import Warehouse
import unittest

class TestDemoMethods(unittest.TestCase):
    # este test no evalua la clase Order en isolation
    # porque el metodo check availability depende de otra clase
    
    def test2(self):
        order = Order("iPhone 14",10)
        house = Warehouse()
        available = order.checkAvailability(house)
        self.assertTrue(available)

