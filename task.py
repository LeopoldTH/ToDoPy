class Task:
    def __init__(self,title, priority):
        self.title = title
        self.isCompleted = False
        self.priority = priority

    def __str__(self):
        status = ""
        if self.isCompleted:
            status = "Fait"
        else: status = "A faire"
        return f"[{status}] {self.title} : {self.priority}"

