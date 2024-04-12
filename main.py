from pronostico import Pronostico
from datos_historicos import DatosHistoricos
import PySimpleGUI as sg


layout = [
    [sg.Text("Seleccione el archivo de datos históricos")],
    [sg.Input(key="filename"), sg.FileBrowse()],
    [sg.Button("Siguiente")]
]

window = sg.Window("Pronóstico de ventas", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Siguiente":
        filename = values["filename"]
        window.close()
        break

db = DatosHistoricos()
db.crear_datos_historicos(filename)

columnas = db.get_todas_las_columnas()

layout = [
    [sg.Text("Seleccione las columnas")],
    [sg.Text("Columna de fecha"), sg.Combo(columnas, key="columna_fecha")],
    [sg.Text("Columna de ventas"), sg.Combo(columnas, key="columna_ventas")],
    [sg.Text("Columna de tipo de producto"), sg.Combo(columnas, key="columna_tipo_producto")],
    [sg.Text("Periodos de pronóstico"), sg.Spin([i for i in range(1, 100)], key="periodos_pronostico")],
    [sg.Text("Frecuencia de pronóstico"), sg.Combo(["Años", "Meses"], key="frecuencia_pronostico")],
    [sg.Button("Siguiente")]
]

window = sg.Window("Pronóstico de ventas", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Siguiente":
        columna_fecha = values["columna_fecha"]
        columna_ventas = values["columna_ventas"]
        columna_tipo_producto = values["columna_tipo_producto"]
        periodos_pronostico = int(values["periodos_pronostico"])
        frecuencia_pronostico = "YE" if values["frecuencia_pronostico"] == "Años" else "ME"
        window.close()
        break



layout = [
    [sg.Text("Seleccione el tipo de producto")],
    [sg.Combo(db.get_tipos_productos(columna_tipo_producto), key="tipo_producto")],
    [sg.Button("Siguiente")]
]

window = sg.Window("Pronóstico de ventas", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Siguiente":
        tipo_producto = values["tipo_producto"]
        window.close()
        break


datos_historicos = db.get_datos_para_pronostico(columna_fecha, columna_ventas, columna_tipo_producto, tipo_producto)

p = Pronostico(datos_historicos, columna_fecha, columna_ventas, periodos_pronostico, frecuencia_pronostico)

p.metodo_minimos_cuadrados()

p.draw()
