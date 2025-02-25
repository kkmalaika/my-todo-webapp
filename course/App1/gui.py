import FreeSimpleGUI  as sg
import functions
#from course.App1.cli.py import new_todo

label = sg.Text("Veuillez saisir une tâche")
input_box = sg.InputText(tooltip="Saisir une tâche", key="todo")
add_button = sg.Button("Ajouter")

window = sg.Window('Bonjour Kelly, Voici vos tâches du jour',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Ajouter":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()


