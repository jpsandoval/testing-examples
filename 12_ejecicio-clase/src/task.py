class Task:
    def __init__(self, task_id, description, priority=1, completed=False):
        self.task_id = task_id
        self.description = description
        self.priority = priority
        self.completed = completed
    
    def is_completed(self):
        return self.completed

    def complete_task(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Not Done"
        return f"Task {self.task_id}: {self.description} (Priority: {self.priority}, {status})"
