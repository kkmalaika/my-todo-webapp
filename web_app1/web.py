import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Ma 1ère application : Ma Todo list")
st.subheader("Ceci est ma liste de tâches pour aujourd'hui")
st.write("Hotep :-)")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]




st.text_input(label="Ajouter une tâche : ", placeholder="Saisissez une tâche ici",
              on_change=add_todo, key='new_todo')

print("Hello")