import unittest
from model import *
from parser import *
from visitors import *


class TestCounterVisitor(unittest.TestCase):
    
    # testing visitor

    def test_number_counter(self):
        visitor = NumberCounter()
        ast = parser("2789")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 1)

    def test_number_counter2(self):
        visitor = NumberCounter()
        ast = parser("(+ (+ 145 12) 2789)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)


if __name__ == '__main__':
    unittest.main()
