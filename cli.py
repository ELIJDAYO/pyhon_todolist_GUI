from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todos = get_todos()
        todo = user_action[4:] + '\n'

        todos.append(todo)

        write_todos(todos, r"todos.txt")

    elif user_action.startswith("show"):
        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):
            print(f"{index + 1}--{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos, r"todos.txt")

        except ValueError:
            print("Invalid edit command")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            removed_todo = todos.pop(number - 1).strip('\n')

            write_todos(todos, r"todos.txt")

            print(f"{removed_todo} is removed from the list")
        except IndexError:
            print("Invalid index")
            continue
        except ValueError:
            print("Invalid complete command")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command")

print("Bye")
