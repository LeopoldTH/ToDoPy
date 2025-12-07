from todo_controller import ToDoController

app = ToDoController()

print("test")

app.add_task("Faire à manger","A faire")
app.add_task("Programmer","En cours")


app.afficher_taches()