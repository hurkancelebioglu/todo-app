import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity.")


for t in todos:
    st.checkbox(t)

st.text_input(label="Enter a new todo:", placeholder="Waiting for new todo...", on_change=add_todo, key="new_todo")
