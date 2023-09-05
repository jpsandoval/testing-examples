from ast import *
import ast

sourceCode="""foo(2)
add(2,3)
eval('1+1')
"""
tree = parse(sourceCode)

#print(ast.dump(tree,indent=3))

# accediendo directamente al nodo que yo quiero
# utilizando los accesores de cada nodo
for expr in tree.body:
    if(expr.value.func.id=='eval'):
        print("warning at line "+ str(expr.lineno))

# el problema es que asumo que el código cierta estructura