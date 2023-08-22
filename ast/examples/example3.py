from ast import *
import ast

sourceCode="""self.foo(2)
eval('1+1')
add(2,3)
"""
tree = parse(sourceCode)

#print(ast.dump(tree,indent=3))

# puedo ir filtrando las expresiones dependiendo a su tipo
# el problema que este código sigue siendo poco flexible
for expr in tree.body:
    if(isinstance(expr.value,Call)):
        if(isinstance(expr.value.func,Name)):
            if(expr.value.func.id=='eval'):
              print("warning at line "+ str(expr.lineno))