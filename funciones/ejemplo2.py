from functools import reduce
import operator 
#------------------------------------


#------------------------------------
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def name(self):
        return self.name
    
    def score(self):
        return self.score

students = [Student("Juan",2) , Student("Pedro",2), Student("Pablo",3)]
