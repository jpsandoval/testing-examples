from ast import *
import ast

sourceCode="""foo(2)
bar(3)
zoo(5)
"""
tree = parse(sourceCode)

#print(ast.dump(tree,indent=3))

# imprime todos los nombres de las funciones
for expr in tree.body:
    match expr:
        case Expr(value=Call(
                func=Name(id=fun_name, ctx=Load()),
                args=arg_list,keywords=[])):
              print(fun_name)

# aqui se puede ver que match case te ayuda a extraer data
# de la estructura lo cual es super util