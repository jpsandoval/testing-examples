import ast
import unittest
from ast import *


class LinterTest(unittest.TestCase):

    def asssertWarning(self, warningsA, warningsB):
        self.assertEqual(len(warningsA), len(warningsB), 'The number of warnings do not match')
        for x, y in zip(warningsA, warningsB):
            self.assertEqual(x.__str__(), y.__str__())

    def assertAST(self, codeA, codeB):
        self.assertEqual(ast.dump(parse(codeA)), ast.dump(parse(codeB)))
