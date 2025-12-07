from task import Task 

class ToDoController:

    def __init__(self):
        self.tasks = []
        

    def add_task(self, task,status):
        new_task = Task(task,status)
        self.tasks.append(new_task)

    def afficher_taches(self):
        for task in self.tasks:
            print(task)