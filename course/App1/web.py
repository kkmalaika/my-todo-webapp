import streamlit as st
from streamlit import session_state
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("Mon 1ère application : Ma Todo list")
st.subheader("Ceci est ma liste de tâches pour aujourd'hui")
st.write("Bonjour Kelly   :-)")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Ajouter une tâche : ", placeholder="Saisissez une tâche ici",
              on_change=add_todo, key='new_todo')

print("Hello")

st.session_state