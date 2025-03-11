import FreeSimpleGUI  as sg
import functions
import time
import os

if not os.path.exists("Ma_Todo_Quotidienne.txt"):
    with open("Ma_Todo_Quotidienne.txt", "w") as file:
        pass

#from course.App1.cli.py import new_todo                                                                      ²  

#sg.theme("Purple")
sg.theme("DarkTeal")

clock = sg.Text('', key='clock')
label = sg.Text("Veuillez saisir une tâche")
input_box = sg.InputText(tooltip="Saisir une tâche", key="todo")
add_button = sg.Button("Ajouter")
#add_button = sg.Button(size=10, image_source="Ajouter.PNG", mouseover_colors="LightBlue2",
 #                      tooltip="Ajouter tâche", key="Ajouter")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[50, 16])
edit_button = sg.Button("Modifier")
complete_button = sg.Button("Faite")
exit_button = sg.Button("Sortir")

#layout=[[label], [input_box, add_button], [list_box, edit_button]]

window = sg.Window('Bonjour Kelly, Voici vos tâches du jour',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10 ))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b, %Y %H:%M:%S"))
    match event:
        case "Ajouter":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Modifier":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Selectionner d'abord un élément de la liste", font=('Helvetica', 10 ))
                print("Selectionner d'abord un élément de la liste")
        case "Faite":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)

                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Selectionner d'abord un élément de la liste", font=('Helvetica', 10 ))
        case "Sortir":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            exit()
print("bye")

window.close()


