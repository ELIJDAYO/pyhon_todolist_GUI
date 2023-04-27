import PySimpleGUI as sg
import os
import functions as fun
import time

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")
clock = sg.Text('', key="clock")
label = sg.Text("Please type in your task")
input_box = sg.InputText(tooltip="Enter todo",
                         key="todo", )

add_button = sg.Button(size=2, image_source="add.png",
                       mouseover_colors="LightBlue2",
                       tooltip="Add Todo",
                       key="Add")
list_box = sg.Listbox(values=fun.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("Todo App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    # while loop exe every 10ms
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    # print(values["todos"])
    match event:
        case "Add":
            try:
                todos = fun.get_todos()
                new_todo = values['todo'] + "\n"
                if new_todo != "\n":
                    todos.append(new_todo)
                    fun.write_todos(todos)
                    window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Print select an item", font=("Helvetica", 20))
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = fun.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fun.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Print select an item", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = fun.get_todos()
                todos.remove(todo_to_complete)
                fun.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Print select an item", font=("Helvetica", 20))
        case "Exit:":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
            break
        case sg.WIN_CLOSED:
            break

window.close()
