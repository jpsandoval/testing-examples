from .task import Task


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        task = Task(task_id, description)
        self.tasks.append(task)
        return task

    def remove_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return f"Task {task_id} removed."
        return f"Task {task_id} not found."

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.complete_task()
                return f"Task {task_id} marked as done."
        return f"Task {task_id} not found."

    def find_high_priority_tasks(self, threshold):
        high_priority_tasks = []
        for task in self.tasks:
            if task.priority > threshold:
                high_priority_tasks.append(task)
        return high_priority_tasks

    def list_tasks(self):
        return [str(task) for task in self.tasks]