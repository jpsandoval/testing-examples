from _ast import Call
from ast import *
import ast
from typing import Any

sourceCode="""foo(2)
bar(3)
zoo(5)
"""
tree = parse(sourceCode)

class FunCallVisitor(NodeVisitor):
    def visit_Call(self, node: Call):
        print(node.func.id)

visitor = FunCallVisitor()
visitor.visit(tree)

# funciona pero estamos asumiendo que la funcion invocada tiene un nombre
# podria ser una funcion anonima
# o un atributo