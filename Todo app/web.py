import streamlit as st
import read_and_write as rw

todos = rw.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    todos.append(todo_local)
    rw.write_todos(todos)


st.title("My Todo App")
st.subheader("This my todo app")
st.write("this app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
