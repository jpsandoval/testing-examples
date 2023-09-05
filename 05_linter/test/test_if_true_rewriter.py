import unittest
from core import *
from core.rewriter import rewrite
from .linter_test import *
from core.transformers import *


class TestNoEvalRule(LinterTest):
    def test_1(self):
        result = rewrite(IfTrueRewriterCommand, 
"""if True:
  if True:
    2
  else:
    3
else:
  4""")
        print(result)
        self.assertAST(result, "2")

   

if __name__ == '__main__':
    unittest.main()
