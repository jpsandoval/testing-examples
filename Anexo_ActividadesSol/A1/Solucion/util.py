from functools import reduce
import operator 


def select(cond, aList):
    return list(filter(cond, aList))


def reject(cond, aList):
    return select(lambda x: not cond(x), aList)


def collect(fun, aList):
    return list(map(fun, aList))


def anySatisfy(cond, aList):
    flags = map(lambda x: cond(x), aList)
    return reduce(operator.or_, flags, False)


def noneSatisfy(cond, aList):
    flags = map(lambda x: not cond(x), aList)
    return reduce(operator.and_, flags, True)


def allSatisfy(cond, aList):
    flags = map(lambda x: cond(x), aList)
    return reduce(operator.and_, flags, True)


