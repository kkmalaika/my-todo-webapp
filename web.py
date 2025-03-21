import streamlit as st
import functions

# Get the current to-do list
todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()  # Remove extra spaces/newlines

    if not todo:  # Prevent empty tasks
        st.warning("Veuillez entrer une tâche valide.")
        return

    if todo + "\n" in todos:  # Check for duplicates
        st.warning("Cette tâche existe déjà dans la liste ! Veuillez entrer une tâche différente.")
    else:
        todos.append(todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input after adding


st.title("Ma 1ère application : Ma Todo list")
st.subheader("Ceci est ma liste de tâches pour aujourd'hui")
st.write("Hotep :-)")

# Display the list of tasks
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo.strip(), key=f"todo_{index}")  # Unique key
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.rerun()

# Input field for adding new tasks
st.text_input(
    label="Ajouter une tâche :",
    placeholder="Saisissez une tâche ici",
    on_change=add_todo,
    key="new_todo"
)
