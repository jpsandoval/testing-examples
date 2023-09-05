import unittest
from model import *
from parser import *
from visitors import *


class TestPlusPlus(unittest.TestCase):
    # Tests para el ejercicio 1
    def test_parser_1(self):
        ast1 = AdditionNode(NumberNode(0), NumberNode(1))
        ast2 = parser("(++ 0)")
        self.assertEqual(ast1, ast2)

    def test_plusplus_eval(self):
        ast = parser("(++ 1)")
        result = ast.eval()
        self.assertEqual(result, 2)

    def test_plusplus_eval_2(self):
        ast = parser("(++ (++ 1))")
        result = ast.eval()
        self.assertEqual(result, 3)

    def test_plusplus_eval_3(self):
        ast = parser("(++ (++ (++ 19)))")
        result = ast.eval()
        self.assertEqual(result, 22)
    

if __name__ == '__main__':
    unittest.main()
