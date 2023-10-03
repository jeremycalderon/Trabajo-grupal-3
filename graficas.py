import numpy as np
import PySimpleGUI as sg

ale = [36,72,108,144,180,216,252,288,324]

def separar_curva(imagen):
    img=f'CURVAS/gamma={imagen}.png'
    return img

def hacer_curva_36():
    ly_curva_36 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[0]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_36)

def hacer_curva_72():
    ly_curva_72 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[1]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_72)

def hacer_curva_108():
    ly_curva_108 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[2]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_108)

def hacer_curva_144():
    ly_curva_144 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[3]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_144)

def hacer_curva_180():
    ly_curva_180 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[4]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_180)

def hacer_curva_216():
    ly_curva_216 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[5]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_216)

def hacer_curva_252():
    ly_curva_252 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[6]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_252)

def hacer_curva_288():
    ly_curva_288 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[7]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_288)

def hacer_curva_324():
    ly_curva_324 = [
        [sg.Text("Curva del Acoplador")],
        [sg.Image(separar_curva(ale[8]))],
        [sg.Button("Finalizar")],
        [sg.Button("Salir")]
    ]
    return sg.Window("Curva del Acoplador", ly_curva_324)
