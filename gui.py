import functions
import PySimpleGUI as Sg

label = Sg.Text("Type to-do")
input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")

window = Sg.Window("My To-do App",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", "20"))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break

window.close()
