import unittest
from model import *
from parser import *
from visitors import *


class TestCounterVisitor(unittest.TestCase):
    
    # testing visitor
    def test_node_counter(self):
        visitor = NodeCounter()
        ast = parser("(+ (+ 145 12) 2789)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 5)

    # testing visitor
    def test_node_counter2(self):
        visitor = NodeCounter()
        ast = parser("(- 145 12)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 3)

    def test_node_counter3(self):
        visitor = NodeCounter()
        ast = parser("(if0 1 2 3)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 4)

    def test_node_counter4(self):
        visitor = NodeCounter()
        ast = parser("(+ (+ (- 45 24) (+ 3 (- 34 25))) 5)")
        ast.accept(visitor)
        self.assertEqual(visitor.total(), 11)


if __name__ == '__main__':
    unittest.main()
