from model import *


# Modulo que contiene los visitors creados y cada uno computa una metrica
# Visitor
class Visitor:
    # Los nodos compuestos deben propagar la visita a los subnodos
    def visit_Addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Subtract(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)

    def visit_Number(self, node):
        pass


# Visitador que cuenta la cantidad de nodos de tipo NumberNode que existen en el arbol
class NumberCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_Number(self, node):
        self.counter = self.counter + 1

    def total(self):
        return self.counter

    

# Visitador que mide la legibilidad
class NodeCounter(Visitor):
    # ---- Implementar Clase ---- #
    def __init__(self):
        pass