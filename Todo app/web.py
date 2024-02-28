import streamlit as st
import read_and_write as rw

todos = rw.get_todos()

st.title("My Todo App")
st.subheader("This my todo app")
st.write("this app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add new todo...")
