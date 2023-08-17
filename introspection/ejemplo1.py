import inspect
from bank_account import BankAccount

account = BankAccount()
# ---------------------------------------------
# dir: It returns a list of attributes and methods belonging to an object.

data = dir(account)
#print(data)

# ---------------------------------------------
# type: The type function returns the type of an object. 
print(type(account))
# Output: <class '__main__.BankAccount'>

print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>

# ---------------------------------------------
# inspect: The inspect module also provides several useful functions to get information about live objects.

print("-------------------------")
print(inspect.getmembers(account))
print("-------------------------")


# ---------------------------------------------
# obtener nombres de atributos y valores de un objeto
print("atributos de la clase Bank Account")
print(account.__dict__.keys())
print(account.__dict__.values())

# ---------------------------------------------
# obtener metodos de una clase
list_of_methods = inspect.getmembers(BankAccount, predicate=inspect.isfunction)
print("---- * ---- ")
print(list_of_methods)
print("---- * ---- ")
# ---------------------------------------------
# un metodo en una clase es una instancia de funcion
# list_of_methods es una lista de pares (nombre, funcion)
# obtenemos la funcion del primer metodo
funcion = list_of_methods[0][1]

# ---------------------------------------------
# se puede obtener el nombre de la funcion
print("funcion: ",funcion.__name__)

# ---------------------------------------------
# se puede obtener el codigo dentro de una funcion
codeLines = inspect.getsourcelines(funcion)[0]
print("codigo fuente")
for line in codeLines:
    print(line)

# ---------------------------------------------
# la documentacion """ la documentacion va entre 3 comillas dobles """
doc = funcion.__doc__
print("documentacion")
print(doc)

# ---------------------------------------------
# los argumentos de una funcion
print("argumentos")
print(inspect.getfullargspec(list_of_methods[1][1]).args)

# ---------------------------------------------
# obtener el valor de un atributo basado en un string
funcion_deposit = list_of_methods[1][1]
# ejecutando un metodo de forma distinta
funcion_deposit(account, 200)
# obteniendo el valor de un atribudo de forma ad hoc
print("el balance es:", getattr(account, "balance"))
