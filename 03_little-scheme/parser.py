from model import *


# Parser super sencillo y basico
def parser(stringCode):
    if isNumber(stringCode):
        return NumberNode(int(stringCode))
    elif isOperation(stringCode):
        return operation(stringCode)
    else:
        raise Exception("Expression ", stringCode, " not supported.")


def isNumber(string):
    return string.isnumeric()


def isOperation(string):
    res = False
    validOperators = {'+': 2, '-': 2}
    # Primero verificamos si tiene ambos parentesis de la sintaxis
    if string[0] == '(' and string[len(string)-1] == ')':
        # Partimos por espacios la cadena sin considerar el primer y el último parentesis
        tokens = splitArgs(string[1:len(string)-1])
        operator = tokens.pop(0)
        # Verificamos que el operador sea uno que reconocemos y que solo exista el número correcto de argumentos
        res = operator in validOperators and len(tokens) == validOperators.get(operator)
    return res


def operation(string):
    tokens = splitArgs(string[1:len(string)-1])
    operator = tokens.pop(0)
    # Creamos el nodo correspondiente segun el operador y parseamos los demás argumentos
    if operator == "+":
        return AdditionNode(parser(tokens[0]), parser(tokens[1]))
    elif operator == "-":
        return SubtractionNode(parser(tokens[0]), parser(tokens[1]))


def splitArgs(string):
    open_counter = 0
    temp = ""
    result = []
    for key in string:
        if key == ' ' and open_counter == 0:
            # adding an argument
            result.append(temp.strip())
            temp = ""
        elif key == '(':
            open_counter = open_counter + 1
        elif key == ')':
            open_counter = open_counter - 1
        else:
            pass
        temp = temp + key
    # adding last arg
    result.append(temp.strip())
    return result
