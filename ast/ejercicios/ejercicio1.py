from _ast import Call
from ast import *
import ast
from typing import Any

# escribir un programa que imprima "argument <name> is not used"
# este debe revisar que dentro de una funcion
# si existe un argumento que no se este utilizando

sourceCode1="""def demo(a,b):
  return a
""" 
# debe imprimir el mensaje
# argument b is not used


sourceCode2="""def demo(a,b):
  return a + b
""" 
# no debe imprimir nada

sourceCode3="""def demo():
  a = 3
  return a + 2
""" 
# no debe imprimir nada pq no tiene argumentos


sourceCode4="""def demo(c,x):
    return bar(c)
""" 
# debe imprimir el mensaje
# argument x is not used


tree = parse(sourceCode4)
print(ast.dump(tree,indent=3))