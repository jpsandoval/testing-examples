from _ast import Call
from ast import *
import ast
from typing import Any

sourceCode="""class Counter:
  def __init__(self):
    self.c = 3
  
  def increment(self):
    return self.c + 1
"""
tree = parse(sourceCode)

# otra forma utilizando match case
class AttributePrinterVisitor(NodeVisitor):
    def visit_Attribute(self, node: Attribute):
        NodeVisitor.generic_visit(self, node)
        # or super().visit_Call(node)
        print(node.attr)

visitor = AttributePrinterVisitor()
visitor.visit(tree)