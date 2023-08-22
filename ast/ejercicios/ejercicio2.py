from _ast import Call
from ast import *
import ast
from typing import Any

# escribir un programa que imprima "super init is not called"
# este debe revisar que dentro de la clase
# el metodo __init__() ... llama al super().__init__()
# en la primera linea
# puede asumir que el input siempre sera una clase

sourceCode1="""class A(B):
  def __init__(self):
    self.c = 3
""" 
# debe imprimir el mensaje

sourceCode2="""class A:
  def __init__(self):
    self.c = 3
""" 
# no debe imprimir el mensaje

sourceCode3="""class A(B):
  def __init__(self):
    super().__init__()
    self.c = 3
""" 
# no debe imprimir el mensaje

sourceCode4="""class A(B):
  def __init__(self, other_c):
    self.c = other_c
""" 
# debe imprimir el mensaje

tree = parse(sourceCode4)
print(ast.dump(tree,indent=3))