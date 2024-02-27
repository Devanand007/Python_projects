import read_and_write as rw
import PySimpleGUI as Sg

label = Sg.Text("Type in a to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=rw.get_todos(), key='todos',
                      enable_events=True, size=[45, 10],)
edit_button = Sg.Button("Edit")

window = Sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20),
                   )

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = rw.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            rw.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']

            todos = rw.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo+"\n"
            rw.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case Sg.WIN_CLOSED:
            break

window.close()
