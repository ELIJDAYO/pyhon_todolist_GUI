import PySimpleGUI as sg

label = sg.Text("Type in")
input_box = sg.InputText(tooltip="Enter todo")

window = sg.Window("Todo App", layout=[[label, input_box]])
window.read()
window.close()