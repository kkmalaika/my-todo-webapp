import FreeSimpleGUI as sg
import functions

label = sg.Text("Veuillez saisir une tâche")
input_box = sg.InputText(tooltip="Saisir une tâche")
add_button = sg.Button("Ajouter")

window = sg.Window('Bonjour Kelly, Voici vos tâches du jour', layout=[[label], [input_box, add_button] ])
window.read()
print("Coucou")
window.close()


