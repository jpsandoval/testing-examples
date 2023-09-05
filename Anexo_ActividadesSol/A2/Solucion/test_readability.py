import unittest
from model import *
from parser import *
from visitors import *


class TestCounterVisitor(unittest.TestCase):
    
    # testing visitor
    def test_number_readability(self):
        ast = parser("2")
        self.assertEqual(ast.readability(), 1)

    def test_addition_readability(self):
        ast = parser("(+ 1 2)")
        self.assertEqual(ast.readability(), 1)
    
    def test_addition_readability2(self):
        ast = parser("(+ 1 (+ 1 2))")
        self.assertEqual(ast.readability(), 1)

    def test_if0_true(self):
        ast = parser("(if0 0 1 2)")

        self.assertEqual(ast.readability(), 2)

    def test_if0_false(self):
        ast = parser("(if0 1 2 3)")
        self.assertEqual(ast.readability(), 3)

    def test_if0_2(self):
        ast = parser("(if0 1 2 (if0 0 1 2))")
        self.assertEqual(ast.readability(), 4)

    def test_if0_3(self):
        ast = parser("(if0 1 (if0 0 1 2) 2)")
        self.assertEqual(ast.readability(), 3)

    def test_if0_4(self):
        ast = parser("(if0 0 (if0 0 1 2) 2)")
        self.assertEqual(ast.readability(), 3)


if __name__ == '__main__':
    unittest.main()
