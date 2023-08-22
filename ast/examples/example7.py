from _ast import Call
from ast import *
import ast
from typing import Any

sourceCode="""self.foo(2)
(lambda x: x +1)(3)
zoo(5)
"""
tree = parse(sourceCode)

#imprime los nombres de las funciones llamadas
#considerando que fue atributo o q la funcion tiene nombre
class FunCallVisitor(NodeVisitor):
    def visit_Call(self, node: Call):
        if isinstance(node.func,Name):
                print(node.func.id)
        elif isinstance(node.func,Attribute):
                print(node.func.attr)


visitor = FunCallVisitor()
visitor.visit(tree)