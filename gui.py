import PySimpleGUI as sg

import functions as fun

label = sg.Text("Type in")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("Todo App",
                   layout=[[label, input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fun.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fun.write_todos(todos)
        case sg.WIN_CLOSED: break

window.close()