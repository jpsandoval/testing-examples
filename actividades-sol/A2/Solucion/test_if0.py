import unittest
from model import *
from parser import *
from visitors import *


class TestIf0(unittest.TestCase):
    # Tests para la tarea 1
    # Deben agregar las clases y modificar los metodos necesarios
    # para que los siguientes tests compilen y pasen
    # usted puede agregar más tests

    # Tests para el ejercicio 1
    def test_if0_parser_1(self):
        ast1 = If0Node(NumberNode(0), NumberNode(5), NumberNode(2))
        ast2 = parser("(if0 0 5 2)")
        self.assertEqual(ast1, ast2)

    def test_if0_eval_true(self):
        ast = parser("(if0 0 5 2)")
        result = ast.eval()
        self.assertEqual(result, 5)

    def test_if0_eval_false(self):
        ast = parser("(if0 1 5 2)")
        result = ast.eval()
        self.assertEqual(result, 2)

    def test_if0_eval_recursive(self):
        ast = parser("(if0 0 (if0 0 2 3) 4)")
        result = ast.eval()
        self.assertEqual(result, 2)
    
    def test_if0_eval_recursive_3(self):
        ast = parser("(if0 (- 1 1) (+ 1 1) (+ 1 1))")
        result = ast.eval()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
