import read_and_write as rw
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")

window = Sg.Window("My To-Do App",
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 20),
                   )

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = rw.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            rw.write_todos(todos)
        case Sg.WIN_CLOSED:
            break

window.close()
