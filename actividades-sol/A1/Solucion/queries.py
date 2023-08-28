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
    pairs = inspect.getmembers(cls, predicate=inspect.isfunction)
    # pair[0] es el nombre del método
    # pair[1] es la función
    pairs = select(lambda pair: pair[1].__doc__ is None, pairs)
    functions = collect(lambda pair: pair[1], pairs)
    return collect(lambda f: f.__name__, functions)


# E4: verificar si un objeto tiene atributos
def hasAttributes(obj):
    return len(obj.__dict__.keys()) > 0


# E5: nombres de métodos que no reciben ningún argumento
def noArgs(fun):
    args = inspect.getfullargspec(fun).args
    return len(args) <= 1


def noArgMethods(cls):
    pairs = inspect.getmembers(cls, predicate=inspect.isfunction)
    functions = collect(lambda pair: pair[1], pairs)
    return collect(lambda f: f.__name__, select(noArgs, functions))


# E6: todos los métodos empiezan con minúscula
def starts_with_lowercase(input_string):
    return len(input_string) > 0 and (input_string[0].islower() or (input_string[0] == '_'))


def allLowerCase(cls):
    pairs = inspect.getmembers(cls, predicate=inspect.isfunction)
    functionsNames = map(lambda p: p[0], pairs)
    return reject(starts_with_lowercase, functionsNames) == []


# E7: todos los métodos que tengan más de k líneas
def isLongMethod(fun, k):
    return len(inspect.getsourcelines(fun)[0]) > k


def longMethods(cls,k):
    pairs = inspect.getmembers(cls, predicate=inspect.isfunction)
    functions = map(lambda p: p[1], pairs)
    return collect(lambda f: f.__name__, select(lambda f: isLongMethod(f, k), functions))


# E8: tiene la menos un atributo None
def checkNone(obj):
    return anySatisfy(lambda v: v is None, obj.__dict__.values())