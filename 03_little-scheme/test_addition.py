import unittest
from model import *
from parser import *
from visitors import *


class TestAddition(unittest.TestCase):
    # Testing the parser
    def test_number(self):
        ast1 = NumberNode(27)
        ast2 = parser("27")
        self.assertEqual(ast1, ast2)

    def test_sum(self):
        ast1 = AdditionNode(NumberNode(2), NumberNode(3))
        ast2 = parser("(+ 2 3)")
        self.assertEqual(ast1, ast2)

    # Testing eval
    def test_sum_eval(self):
        ast = parser("(+ 25 30)")
        result = ast.eval()
        self.assertEqual(result, 55)

    # Testing to_string
    def test_to_string(self):
        ast1 = SubtractionNode(AdditionNode(NumberNode(2), NumberNode(1)), SubtractionNode(NumberNode(3), NumberNode(2)))
        self.assertEqual(ast1.to_string(), "(- (+ 2 1) (- 3 2))")


if __name__ == '__main__':
    unittest.main()
