from functools import reduce
import operator 
#------------------------------------
def collect(fun, aList):
    return list(map(fun,aList))
def select(cond, aList):
    return list(filter(cond,aList))


#------------------------------------
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def getName(self):
        return self.name
    
    def getScore(self):
        return self.score

students = [Student("Juan",2) , Student("Pedro",2), Student("Pablo",3)]
scores = collect(lambda std: std.getScore, students)
print(scores)