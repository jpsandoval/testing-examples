from ast import *
import ast

tree = parse("2+3")

print(ast.dump(tree,indent=3))
