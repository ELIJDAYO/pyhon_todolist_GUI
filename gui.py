import PySimpleGUI as sg

import functions as fun

label = sg.Text("Type in")
input_box = sg.InputText(tooltip="Enter todo",
                         key="todo",)

add_button = sg.Button("Add")
list_box = sg.Listbox(values=fun.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("Todo App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["todos"])
    match event:
        case "Add":
            todos = fun.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fun.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = fun.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fun.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = fun.get_todos()
            todos.remove(todo_to_complete)
            fun.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit:":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
            break
        case sg.WIN_CLOSED:
            break

window.close()