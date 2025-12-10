from task import Task 

class ToDoController:

    def __init__(self):
        self.tasks = []
        

    def add_task(self, task, priority):
        new_task = Task(task, priority)
        self.tasks.append(new_task)
        print(f"Nouvelle tâche ajoutée: {task.title}")

    def remove_tasks(self,task_to_remove):
        for task in self.tasks:
            if task.title == task_to_remove:
                self.tasks.remove(task)
                print(f"Tâche supprimée :{task_to_remove} ")
                return
        print("Tâche non trouvée")

    def complete_task(self,task_completed):
        for task in self.tasks:
            if task.title == task_completed:
                task.isCompleted = True
                print(f"La tâche '{task_completed}' a été faite")
                return
        print("Tâche non trouvée")

    


    def afficher_taches(self):
        self.sorted_by_priority()
        for task in self.tasks:
            print(task)

    def sorted_by_priority(self):
        self.tasks.sort(key=lambda task: task.priority)

        
            