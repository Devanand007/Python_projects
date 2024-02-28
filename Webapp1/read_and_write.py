FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as get_file:
        get_todo = get_file.readlines()
    return get_todo


def write_todos(todos_arg, filepath=FILEPATH):
    """
        Write a list of to-do items to a text file.
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())