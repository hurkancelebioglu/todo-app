import functions
import PySimpleGUI as Sg

label = Sg.Text("Type to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos_list",
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")

window = Sg.Window("My To-do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", "20"))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos_list"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos_list"][0]
            new_todo = values["todo"]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos_list"].update(values=todos)
        case "todos_list":
            window["todo"].update(value=values["todos_list"][0])

        case Sg.WIN_CLOSED:
            break

window.close()
