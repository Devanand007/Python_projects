import read_and_write as rw
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo")
add_button = Sg.Button("Add")

window = Sg.Window("My To-Do App", layout=[[label], [input_box], [add_button]])
window.read()
window.close()
