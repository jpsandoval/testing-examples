# Sintaxis concreta usada para escribir expresiones aritmeticas:
# <expr> = <num>
#        | (+ <expr> <expr>)
#        | (- <expr> <expr>)


class Node:
    # Formatea la expresion en un string
    def to_string(self):
        pass

    # Evalua la expresion
    def eval(self):
        pass

    # Acepta la visita de un visitor
    def accept(self, visitor):
        pass

    # Verifica si un nodo es igual a otro
    def __eq__(self, other):
        return self.__class__ == other.__class__

    def readability(self):
        return 1


# Nodos literales normalmente son los valores primitivos (string, entero, boolean)
# En este caso solo consideramos un número entero
class LiteralNode(Node):
    def __init__(self, val):
        self.value = val

    def to_string(self):
        pass

    def eval(self):
        return self.value

    def accept(self, visitor):
        visitor.visit_Literal(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.value == other.value
    

# Numero
class NumberNode(LiteralNode):
    def accept(self, visitor):
        visitor.visit_Number(self)

    def to_string(self):
        return "" + str(self.value)


# Operadores
class OperatorNode(Node):
    def __init__(self, sym):
        self.symbol = sym

    def accept(self, visitor):
        visitor.visit_Operator(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.symbol == other.symbol
    
    
# Operador binario
class BinaryOperatorNode(OperatorNode):
    def __init__(self, leftNode, rightNode, sym):
        super().__init__(sym)
        self.leftNode = leftNode
        self.rightNode = rightNode

    def to_string(self):
        return "(" + self.symbol + " " + self.leftNode.to_string() + " " + self.rightNode.to_string() + ")"

    def accept(self, visitor):
        visitor.visit_BinaryOperator(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.leftNode == other.leftNode and self.symbol == other.symbol and self.rightNode == other.rightNode
    

# Operador suma
class AdditionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(AdditionNode, self).__init__(leftNode, rightNode, "+")

    def eval(self):
        return self.leftNode.eval() + self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Addition(self)


# Operador resta
class SubtractionNode(BinaryOperatorNode):
    def __init__(self, leftNode, rightNode):
        super(SubtractionNode, self).__init__(leftNode, rightNode, "-")

    def eval(self):
        return self.leftNode.eval() - self.rightNode.eval()

    def accept(self, visitor):
        visitor.visit_Subtract(self)


#If0
class If0Node(OperatorNode):
    def __init__(self, condNode, ifNode, elseNode):
        super(If0Node, self).__init__('if0')
        self.condNode = condNode
        self.ifNode = ifNode
        self.elseNode = elseNode
        
    def eval(self):
        if self.condNode.eval() == 0 :
            return self.ifNode.eval()
        else:
            return self.elseNode.eval()

    def accept(self, visitor):
        visitor.visit_If0(self)
    
    def readability(self):
        result = self.condNode.eval()
        if result == 0:
            return 1 + self.ifNode.readability()
        else:
            return 2 + self.elseNode.readability()
