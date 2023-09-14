from src.todo_list import TodoList
from src.task import Task

import unittest

class TestTodoList(unittest.TestCase):

    def test_A(self):
        t1 = Task(1,"t1",False)
        
        self.assertEqual(t1.__str__(),"Task 1: t1 (Priority: False, Not Done)")
    

    def test_C(self):
        t1 = Task(1,"t1",False)
        self.assertEqual(t1.is_completed(),False)
    
    def test_B(self):
        t1 = Task(2,"t2")
        self.assertEqual(t1.__str__(),"Task 2: t2 (Priority: 1, Not Done)")