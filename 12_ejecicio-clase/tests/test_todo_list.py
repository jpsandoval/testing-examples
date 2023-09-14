from src.todo_list import TodoList
from src.todo_list import Task

import unittest

class TestTodoList(unittest.TestCase):

    def test_A(self):
        todo = TodoList()
        list = todo.list_tasks()
        self.assertEquals([],list)
