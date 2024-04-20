import customtkinter as ctk
import gui.ParameterScreen
from pronostico import Pronostico
from datos_historicos import DatosHistoricos
import configparser

class VisualizationScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.db = DatosHistoricos()
        self.db.reutilizar_datos_historicos()
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        columna_tipo_producto = config['PARAMETERS']['columna_tipo_producto']
        productos = self.db.get_tipos_productos(columna_tipo_producto=columna_tipo_producto)
        label = ctk.CTkLabel(self, text="Visualización de resultados", font=("Helvetica", 24))
        label.pack()
        draw_button = ctk.CTkButton(self, text="Generar pronóstico para las ventas de un producto", command=lambda: self.draw_pronostico(combo_productos.get()))
        draw_button.pack(padx=20, pady=20)
        combo_productos = ctk.CTkComboBox(self, values=productos)
        combo_productos.pack(padx=20, pady=20)
        
        draw2_button = ctk.CTkButton(self, text="Generar pronóstico para todas las ventas", command=self.draw2_pronostico)
        draw2_button.pack(padx=20, pady=20)
        back_button = ctk.CTkButton(self, text="Volver", command=lambda: self.go_to(gui.ParameterScreen.ParameterScreen))
        back_button.pack(padx=20, pady=20)


    def draw_pronostico(self, tipo_producto):
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        columna_fecha = config['PARAMETERS']['columna_fecha']
        columna_ventas = config['PARAMETERS']['columna_ventas']
        columna_tipo_producto = config['PARAMETERS']['columna_tipo_producto']
        periods = int(config['PARAMETERS']['periods'])
        frequency = config['PARAMETERS']['frequency']

        datos_historicos = self.db.get_datos_para_pronostico(columna_fecha=columna_fecha, columna_ventas=columna_ventas, columna_tipo_producto=columna_tipo_producto, tipo_producto=tipo_producto)

        self.pronostico = Pronostico(datos_historicos=datos_historicos, columna_fecha=columna_fecha, columna_ventas=columna_ventas, periods=periods, freq=frequency)
        self.pronostico.metodo_minimos_cuadrados()
        self.pronostico.draw()

    def draw2_pronostico(self):
        db = DatosHistoricos()
        db.reutilizar_datos_historicos()

        # read parameters.ini
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        columna_fecha = config['PARAMETERS']['columna_fecha']
        columna_ventas = config['PARAMETERS']['columna_ventas']
        # columna_tipo_producto = config['PARAMETERS']['columna_tipo_producto']
        periods = int(config['PARAMETERS']['periods'])
        frequency = config['PARAMETERS']['frequency']

        datos_historicos = db.get_datos_para_pronostico_todas_ventas(columna_fecha=columna_fecha, columna_ventas=columna_ventas)

        self.pronostico = Pronostico(datos_historicos=datos_historicos, columna_fecha=columna_fecha, columna_ventas=columna_ventas, periods=periods, freq=frequency)
        self.pronostico.metodo_minimos_cuadrados()
        self.pronostico.draw()

    def go_to(self, frame):
        self.destroy()
        frame(self.master)