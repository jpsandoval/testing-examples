import unittest
from model import *
from parser import *
from visitors import *


class TestCounterVisitor(unittest.TestCase):
    
    # testing visitor
    def test_addition_counter(self):
        visitor = AdditionCounter()
        ast = parser("(+ (+ 1 1) 2)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 2)


if __name__ == '__main__':
    unittest.main()
