import PySimpleGUI as sg
from numpy import pi, sin, cos, sqrt, absolute, arccos, arctan, sign
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import graficas

class Interface:

    def hacer_saludo():
        ly_saludo = [
            [sg.Text("Universidad Nacional de Trujillo", text_color="red")],
            [sg.Text("Ingeniería Mecatrónica", text_color="red")],
            [sg.Text("Teoría de Máquinas y Mecanismos", text_color="red")],
            [sg.Image("unt.png")], [sg.Image("mecatronica.png")],
            [sg.Text("Integrantes:", text_color="black")],
            [sg.Text("Calderón Alvarado, Jeremy Lorenzo", text_color="black")],
            [sg.Text("Carrillo Guevara, Abigail Bibiana", text_color="black")],
            [sg.Button("Iniciar")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Interfaz gráfica: Curva del Acoplador", ly_saludo)

    def hacer_inicio1():
        ly_inicio1 = [
            [sg.Text("Indique el valor de alfa")],
            [sg.Text("Alfa (Valores de 0 a 360)")], [sg.InputText('',key='input_height1')],
            [sg.Text("Gamma (Valores: 36, 72, 108, 144, 180, 216, 252, 288, 324)")], [sg.InputText('',key='input_height2')],
            [sg.Button("Graficar")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Menú Inicio", ly_inicio1)
    
    def hacer_inicio2():
        ly_inicio2 = [
            [sg.Text("Vuelva a indicar el valor de gamma")],
            [sg.Text("Gamma (Valores: 36, 72, 108, 144, 180, 216, 252, 288, 324)")], [sg.InputText('',key='input_height3')],
            [sg.Button("Graficar")],
            [sg.Button("Salir")]
        ]
        return sg.Window("Menú Inicio", ly_inicio2)
    
    def hacer_mecanismo(alfa, gamma):
        a = 0.6667 # L2
        b = 1.6667 # L3
        c = 1.6667 # L4
        d = 1 # L1
        p = 1.6667 # BP 
        
        x1 = 0
        y1 = 0

        x4 = d
        y4 = 0

        theta1 = alfa*pi/180
        x2 = a * cos(theta1)
        y2 = a * sin(theta1)
        e = sqrt((x2 - d) ** 2 + (y2 ** 2))
        phi2 = arccos((e ** 2 + c ** 2 - b ** 2) / (2 * e * c))
        phi1 = arctan(y2 / (x2 - d)) + (1 - sign(x2 - d)) * pi / 2
        theta3 = phi1 - phi2
        x3 = c * cos(theta3) + d
        y3 = c * sin(theta3)
        theta2 = arctan((y3 - y2) / (x3 - x2)) + (1 - sign(x3 - x2)) * pi / 2
        beta = theta2 + pi/2 - gamma*pi/360
        x5 = x2 + p * cos(beta)
        y5 = y2 + p * sin(beta)

        x_points = [x1, x2, x3, x4, x1]
        y_points = [y1, y2, y3, y4, y1]
        
        x2_points = [x2, x5, x3]
        y2_points = [y2, y5, y3]

        plt.plot(x_points, y_points, color="red")
        plt.plot(x2_points, y2_points, color="red")
        plt.show()
    
ejecuta = True

while ejecuta:

    sg.theme("LightBlue1")
    saludo = Interface.hacer_saludo()
    inicio1 = Interface.hacer_inicio1()
    inicio2 = Interface.hacer_inicio2()
    curva_36 = graficas.hacer_curva_36()
    curva_72 = graficas.hacer_curva_72()
    curva_108 = graficas.hacer_curva_108()
    curva_144 = graficas.hacer_curva_144()
    curva_180 = graficas.hacer_curva_180()
    curva_216 = graficas.hacer_curva_216()
    curva_252 = graficas.hacer_curva_252()
    curva_288 = graficas.hacer_curva_288()
    curva_324 = graficas.hacer_curva_324()

    try:
        while True:
            event, values = saludo.read()
            if event == "Salir"  or event == sg.WIN_CLOSED:
                break
            if event == "Iniciar":
                sg.popup_ok("¿Estás listo/a para graficar?")
                saludo.close()
                while True:
                    event, values = inicio1.read()
                    if event == "Salir"  or event == sg.WIN_CLOSED:
                        break
                    if event == 'Graficar':
                        Interface.hacer_mecanismo(int(values['input_height1']),int(values['input_height2']))
                        inicio1.close()
                        while True:
                            event, values = inicio2.read()
                            if event == "Salir" or event == sg.WIN_CLOSED:
                                break
                            if event == "Graficar":
                                if values['input_height3'] == "36":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_36.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_36.close()
                                elif values['input_height3'] == "72":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_72.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_72.close()
                                elif values['input_height3'] == "108":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_108.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_108.close()
                                elif values['input_height3'] == "144":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_144.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_144.close()
                                elif values['input_height3'] == "180":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_180.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_180.close()
                                elif values['input_height3'] == "216":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_216.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_216.close()
                                elif values['input_height3'] == "252":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_252.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_252.close()
                                elif values['input_height3'] == "288":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_288.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_288.close()
                                elif values['input_height3'] == "324":
                                    inicio2.close()
                                    while True:
                                        event,values = curva_324.read()
                                        if event == "Salir" or event == sg.WIN_CLOSED:
                                            break
                                        if event == "Finalizar":
                                            curva_324.close()


    except:
        print("Ocurrió algún error")
    finally:
        saludo.close()
        inicio1.close()
        inicio2.close()
        curva_36.close()
        curva_72.close()
        curva_108.close()
        curva_144.close()
        curva_180.close()
        curva_216.close()
        curva_252.close()
        curva_288.close()
        curva_324.close()
        print("Todo cerrado")

