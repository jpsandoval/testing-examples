from ast import *
from .rules.warning import *


class Rule:
    def __init__(self):
        self.warningsList = []
    
    def analyze(self, ast):
        pass

    @classmethod
    def name(cls):
        pass

    # Debe retornar una lista de objetos warnings
    def warnings(self):
        return self.warningsList


def analyze(rule, sourceCode):
    return analyzeAll([rule], sourceCode)


def analyzeAll(rules, sourceCode):
    # Se genera el AST (tree) segun el codigo del archivo
    tree = parse(sourceCode)
    warnings = []
    # Se analiza el AST (tree) segun las reglas definidas en rules/__init__.py
    for ruleClass in rules:
        newRule = ruleClass()
        result = newRule.analyze(tree)
        warnings.extend(result)
        warnings.sort()
    return warnings
