# from functions import get_todos, write_todos

from course.App1 import functions
import time

now = time.strftime("%d %b, %Y %H:%M:%S")
print("Nous somme le", now)

while True:
    user_action = input("entrez ajouter, voir, modifier, faite ou sortir: ")
    user_action = user_action.strip()

    if user_action.startswith("ajouter "):
        todo = user_action[8:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("voir"):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row.title())

        # print(f'Il vous reste {index + 1} choses à faire sur votre todo liste')

        print(f'Il vous reste {len(todos)} choses à faire sur votre todo liste')
    elif user_action.startswith("modifier"):
        try:
            number = int(user_action[9:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Sasissez la nouvelle valeur : ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Attention !!! Mauvaise commande")
            continue

    elif user_action.startswith("faite"):
        try:
            faite = int(user_action[6:])
            todos = functions.get_todos()
            index = faite - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"La tâche {todo_to_remove} a été supprimée de votre todo"
            print(message)
        except IndexError:
            print("Attention!!! Numéro  de tâche inexistant")
            continue

    elif user_action.startswith("sortir"):
        break
    else:
        print("Entree non valide")

print("Au revoir")
