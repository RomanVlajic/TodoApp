#from functions import get_todos, write_todos
from GUI import functionsGui
import time

now = time.strftime("%b %d %Y %H:%M:%S")
print("It is", now)


while True:

    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()


    if  user_action.startswith("add"): # OVO MORA BITI TRUE
        todo = user_action[4:]

        todos = functionsGui.get_todos() # = filepath = "todos.txt"

        todos.append(todo + '\n')

        functionsGui.write_todos(todos)


    elif user_action.startswith("show"):

        todos = functionsGui.get_todos() # = filepath = "todos.txt"

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functionsGui.get_todos()  # = filepath = "todos.txt"

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functionsGui.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functionsGui.get_todos()  # = filepath = "todos.txt"
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functionsGui.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("BYE")