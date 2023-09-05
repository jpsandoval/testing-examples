import unittest
from profiler import *

"""
Tests para el instrumentor profile creado en clases
"""

class TestFunctionInstrumentor(unittest.TestCase):

    def test_code1(self):
        profiler = Profiler.profile("input_code/code1.py")
        result = profiler.report_executed_functions()
        # este assertion es un test smell pero es la forma mas facil de probar
        # sin complicarlos mucho
        self.assertEqual(result, """-- Executed functions --
Function test_sum with no arguments.
Function test_sum with no arguments.
Function sum with arguments 2 3
Function sum with arguments 2 3
Function test_sum_tuple with no arguments.
Function test_sum_tuple with no arguments.
Function sum with arguments 3 7
Function sum with arguments 3 7""")

    def test_code2(self):
        profiler = Profiler.profile("input_code/code1.py")
        result = profiler.report_executed_functions()
        # este assertion es un test smell pero es la forma mas facil de probar
        # sin complicarlos mucho
        self.assertEqual(result, """-- Executed functions --
Function factorial with arguments 3
Function factorial with arguments 3
Function factorial with arguments 1
Function factorial with arguments 1
Function abs with arguments 2
Function abs with arguments 2
Function abs with arguments 4
Function abs with arguments 4""")


if __name__ == '__main__':
    unittest.main()
