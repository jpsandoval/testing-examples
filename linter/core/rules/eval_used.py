from ..rule import *
from core.rules.warning import *


# Clases que permiten detectar el uso de la funcion 'eval' para desalentar su uso.
# A veces se usa la funcion 'eval' con expresiones de fuentes poco fiables y esto es poco seguro.

class EvalVisitor(WarningNodeVisitor):
    def visit_Call(self, node):
        if node.func.id == 'eval':
            self.addWarning('EvalWarning', node.lineno, 'eval should not be used!!')
        NodeVisitor.generic_visit(self, node)


class EvalUsedRule(Rule):

    def analyze(self, ast):
        visitor = EvalVisitor()
        visitor.visit(ast)
        return visitor.warningsList()
    
    @classmethod
    def name(cls):
        return 'eval-used'
