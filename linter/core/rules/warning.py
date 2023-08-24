from ast import *


class Warning:
    def __init__(self, name, line, description):
        self.name = name
        self.lineNumber = line
        self.description = description

    # Sobreescribimos el metodo __str__ para dar una representacion de cadena de una instancia de Warning
    def __str__(self):
        return "[ Line " + str(self.lineNumber) + " ] " + self.name + " - " + self.description

    def __repr__(self):
        return "[ Line " + str(self.lineNumber) + " ] " + self.name + " - " + self.description

    # Sobreescribimos el metodo __eq__ para personalizar como se comparan dos instancias
    def __eq__(self, other):
        if isinstance(other, Warning):
            return self.name == other.name and self.lineNumber == other.lineNumber and self.description == other.description
        else:
            return False

    # Sobreescribimos el metodo __gt__ para personalizar el comportamiento del operador >
    def __gt__(self, other):
        if self.lineNumber == other.lineNumber:
            return self.name > other.name
        return self.lineNumber > other.lineNumber


class WarningNodeVisitor(NodeVisitor):
    def __init__(self):
        self.warnings = []
    
    def addWarning(self, name, lineo, description):
        self.warnings.append(Warning(name, lineo, description))

    def warningsList(self):
        return self.warnings
    

