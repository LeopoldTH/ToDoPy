from todo_controller import ToDoController

app = ToDoController()

print("test")

app.add_task("Faire à manger", 1)
app.add_task("Programmer",2)

app.afficher_taches()

app.complete_task("Faire à manger")
app.complete_task("test")
app.remove_tasks("Programmer")


app.afficher_taches()