from functools import reduce
import operator 
#------------------------------------
# funciones
def addOne(n):
    return n + 1

print(addOne(1)) # imprime 2

#------------------------------------
# evaluación temprana
def one():
    return 1

print(addOne(addOne(one()))) # imprime 3
#------------------------------------
# funciones que reciben funciones
def add(a,b):
    return a + b

def multiply(a,b):
    return a*b

def operate(operation,a,b):
    return operation(a,b)

print(operate(add,2,3))      #imprime 5
print(operate(multiply,2,3)) #imprime 6

#------------------------------------
# funciones anonimas

operate( lambda a,b : a+b, 2 ,3 )
#imprime 5

substract = lambda a,b: a-b
operate(substract,3,2) #imprime 1

#------------------------------------
# dynamic scope
k = 3
def addK(n):
    return n + k

print(addK(2)) # imprime 5
k = 10
print(addK(2)) # imprime 12
#------------------------------------
# funciones que devuelven funciones
def addFactor(factor):
    return lambda n : n + factor

add2 = addFactor(2)
add4 = addFactor(4)
print((add2(2))) # imprime 4
print((add4(2))) # imprime 6


#------------------------------------
# implementing foldr
numbers = [1,2,3,4,5,6,7,8,9,10]

def foldr(acc,list,val):
    if list:
        return acc(
            foldr(acc,list[1:],val),
            list[0])
    else:
        return val

print(foldr(operator.add,numbers,0))

#------------------------------------
# implementing foldl
def foldl(acc,list,val):
    if list:
        return acc(
            val,
            foldl(acc,list[1:],list[0]))
    else:
        return val

print(foldr(operator.add,numbers,0))

#------------------------------------
# reduce
sum = reduce(add, numbers,0)
print(sum)

#------------------------------------
# reduce

numbers = [1,2,3,4,5,6,7,8,9,10]
result = reduce(operator.mul, numbers,0)
print(result) 

#------------------------------------
# concatenar dos listas

numbers2 = [1,2,3,4,5,6,7,8,9,10]
numbers3 = numbers2 + [11]
print(list(numbers2))
print(list(numbers3))