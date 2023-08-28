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

    def visit_If0(self, node):
        node.condNode.accept(self)
        node.ifNode.accept(self)
        node.elseNode.accept(self)

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


# Visitador que cuenta la cantidad de nodos de tipo AdditionNode que existen en el arbol
class AdditionCounter(Visitor):
    def __init__(self):
        self.counter = 0

    # Los nodos compuestos deben propagar la visita
    def visit_Addition(self, node):
        node.leftNode.accept(self)
        node.rightNode.accept(self)
        self.counter = self.counter + 1

    def total(self):
        return self.counter


# Visitador que mide la legibilidad
class NodeCounter(Visitor):
    def __init__(self):
        self.counter = 0

    def visit_Addition(self, node):
        super().visit_Addition(node)
        self.counter = self.counter + 1

    def visit_Subtract(self, node):
        super().visit_Subtract(node)
        self.counter = self.counter + 1

    def visit_If0(self, node):
        super().visit_If0(node)
        self.counter = self.counter + 1

    def visit_Number(self, node):
        self.counter = self.counter + 1
    
    def total(self):
        return self.counter
