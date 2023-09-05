from functools import reduce
import operator

def collect(fun, aList):
    return list(map(fun,aList))
def select(cond, aList):
    return list(filter(cond,aList))


numbers = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda n: n> 9,numbers)))
result = reduce(operator.or_,map(lambda n: n>0,numbers),False)
print(result)

strings = ["a","b","c"]

print(reduce(lambda a,s: a+s,strings,""))