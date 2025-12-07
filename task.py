class Task:
    def __init__(self,title,status):
        self.title = title
        self.status = status

    def change_status(self,new_status):
        self.status = new_status

    def __str__(self):
        return f"[{self.status}] {self.title}"

