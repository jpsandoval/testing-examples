import importlib

module = importlib.import_module('bank_account')

# obteniendo la clase en si
clase_account = getattr(module, "BankAccount")

# creando una instancia de la clase
objeto = clase_account()
print(objeto)
objeto.deposit(100)
objeto.withdraw(50)
print(objeto.getBalance())

