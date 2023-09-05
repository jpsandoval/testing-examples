from ast import *
import ast

sourceCode="""self.foo(2)
eval('1+1')
add(2,3)
"""
tree = parse(sourceCode)

#print(ast.dump(tree,indent=3))

# ejemplo de el operador match case
for expr in tree.body:
    match expr:
        case Expr(value=Call(
                func=Name(id='eval', ctx=Load()),
                args=arg_list,keywords=[])):
              print("warning at line "+ str(expr.lineno))

# match case
# mapea un objeto con un patron