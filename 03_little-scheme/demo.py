import unittest
from model import *
from parser import *
from visitors import *


ast = parser("(++ 2)")
print(ast.eval())