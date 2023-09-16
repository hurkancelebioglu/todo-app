import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if (user_action.lower()).startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif (user_action.lower()).startswith("show"):
        todos = functions.get_todos()
        for index, item in enumerate(todos, 1):
            item = (item.strip("\n")).title()
            print(f"{index}-{item}")

    elif (user_action.lower()).startswith("edit"):
        try:
            number_edit = int(user_action[5:])
            print(number_edit)
            number_edit = number_edit - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number_edit] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid. Please provide an integer.")
            continue

    elif (user_action.lower()).startswith("complete"):

        try:
            number_complete = int(user_action[9:])

            todos = functions.get_todos()

            removed_todo = todos[number_complete - 1].strip("\n")
            todos.pop(number_complete - 1)

            functions.write_todos(todos)

            message = f"Todo {removed_todo} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif (user_action.lower()).startswith("exit"):
        break

    else:
        print("Command is not valid.")


print("Bye!")
