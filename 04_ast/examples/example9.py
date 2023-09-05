from _ast import Call
from ast import *
import ast
from typing import Any

sourceCode="""foo(bar(zoo(3)))
"""
tree = parse(sourceCode)

# otra forma utilizando match case
class FunCallVisitor(NodeVisitor):
    def visit_Call(self, node: Call):
        NodeVisitor.generic_visit(self, node)
        # or super().visit_Call(node)
        match node.func:
            case Name(id=func_name, ctx=Load()):
                print(func_name)

visitor = FunCallVisitor()
visitor.visit(tree)
