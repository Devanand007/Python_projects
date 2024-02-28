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

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        rw.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
