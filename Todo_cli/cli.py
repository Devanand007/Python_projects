# from read_and_write import get_todos, write_todos
import read_and_write as rw
import time

now = time.strftime("%B %d, %Y %H:%M:%S")
print("The time is below:")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = rw.get_todos()

        todos.append(todo + "\n")

        rw.write_todos(todos)

    elif user_action.startswith("show"):

        todos = rw.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = rw.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            rw.write_todos(todos)
        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = rw.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            rw.write_todos(todos)

            message = f"todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")
print("Bye!")