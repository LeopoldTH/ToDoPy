from todo_controller import ToDoController

app = ToDoController()

while True:
    print("TO-DO-LIST")
    print()
    print("1. Saisir une nouvelle tâche")
    print("2. Voir toutes les tâches")
    print("3. Supprimer une tâche")
    print("4. Changer le statut d'une tâche")
    print("5. Fin")

    choice = int(input("Choisir une option: \n"))

    if choice == 1:
        task_title = str(input("Saisir un titre pour votre tâche: \n"))
        task_priority = int(input("Saisir la priorité de la tâche: \n"))
        app.add_task(task_title,task_priority)

    elif choice == 2:
        app.afficher_taches()

    elif choice == 3:
        task_to_remove = str(input("Saisir le titre de la tâche à supprimer: \n"))
        app.remove_tasks(task_to_remove)

    elif choice == 4:
        task_to_complete = str(input("Saisir le titre la tâche à marquer comme 'Faite'"))
        app.complete_task(task_to_complete)

    elif choice == 5:
        break
    
    else:
        print("Il semble y avoir eu une erreur\n")

