from functools import reduce
import inspect
from util import *


# E1: verificar si una clase tiene constructor o no
def hasConstructor(cls):
    pairs = inspect.getmembers(cls, predicate=inspect.isfunction)
    # pair[0] es el nombre del método
    # pair[1] es la función
    functions = collect(lambda pair: pair[1], pairs)
    return anySatisfy(lambda fun: fun.__name__ == "__init__", functions)


# E2: nombres de métodos que contenga un substring
def methodsWith(substring, cls):
    pairs = inspect.getmembers(cls, predicate=inspect.isfunction)
    # pair[0] es el nombre del método
    # pair[1] es la función
    return collect(lambda pair: pair[0], select(lambda pair: substring in pair[0], pairs))


# E3: nombres de métodos sin documentar
def undocumentedMethods(cls):
    pass


# E4: verificar si un objeto tiene atributos
def hasAttributes(obj):
    pass


# E5: nombres de métodos que no reciben ningún argumento
def noArgMethods(cls):
    pass


# E6: todos los métodos empiezan con minúscula
def allLowerCase(cls):
    pass


# E7: todos los métodos que tengan más de k líneas
def longMethods(cls, k):
    pass


# E8: tiene la menos un atributo None
def checkNone(obj):
    pass
