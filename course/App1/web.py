import streamlit as st
import functions

todos = functions.get_todos()
st.title("Mon 1ère application : Ma Todo list")
st.subheader("Ceci est ma liste de tâches pour aujourd'hui")
st.write("Bonjour Kelly   :-)")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Ajouter une tâche : ", placeholder="Saisissez une tâche ici")

print("Hello")