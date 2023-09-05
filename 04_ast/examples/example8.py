from _ast import Call
from ast import *
import ast
from typing import Any

sourceCode="""self.foo(2)
(lambda x: x +1)(3)
zoo(5)
"""
tree = parse(sourceCode)

# otra forma utilizando match case
class FunCallVisitor(NodeVisitor):
    def visit_Call(self, node: Call):
        match node.func:
            case Name(id=func_name, ctx=Load()):
                print(func_name)

visitor = FunCallVisitor()
visitor.visit(tree)
