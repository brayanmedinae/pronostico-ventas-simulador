import customtkinter as ctk
import gui.ParameterScreen
from pronostico import Pronostico
from datos_historicos import DatosHistoricos
import configparser
from CTkTable import CTkTable

class VisualizationScreen(ctk.CTkTabview):
    def __init__(self, parent):
        super().__init__(parent)
        # datos
        self.db = DatosHistoricos()
        self.db.reutilizar_datos_historicos()

        # read parameters.ini
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        self.columna_fecha = config['PARAMETERS']['columna_fecha']
        self.columna_ventas = config['PARAMETERS']['columna_ventas']
        self.columna_tipo_producto = config['PARAMETERS']['columna_tipo_producto']
        self.periods = int(config['PARAMETERS']['periods'])
        self.frequency = config['PARAMETERS']['frequency']

        # create tabs
        self.graphicsTab = self.add("Gráfica")
        self.tableTab = self.add("Tabla")

        self.create_widgets_for_graphicsTab()
        self.create_widgets_for_tableTab()
        self.pack(expand=True, fill="both")

    def create_widgets_for_graphicsTab(self):
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        columna_tipo_producto = config['PARAMETERS']['columna_tipo_producto']
        productos = self.db.get_tipos_productos(columna_tipo_producto=columna_tipo_producto)
        label = ctk.CTkLabel(self.graphicsTab, text="Visualización de resultados con gráficos", font=("Helvetica", 24))
        label.pack()
        draw_product_sales_button = ctk.CTkButton(self.graphicsTab, text="Generar pronóstico para las ventas de un producto", command=lambda: self.graphic_forecast_one_product(combo_productos.get()))
        draw_product_sales_button.pack(padx=20, pady=20)
        combo_productos = ctk.CTkComboBox(self.graphicsTab, values=productos)
        combo_productos.pack(padx=20, pady=20)
        draw_all_sales_button = ctk.CTkButton(self.graphicsTab, text="Generar pronóstico para todas las ventas", command=self.graphic_forecast_all_product)
        draw_all_sales_button.pack(padx=20, pady=20)
        back_button = ctk.CTkButton(self.graphicsTab, text="Volver", command=lambda: self.go_to(gui.ParameterScreen.ParameterScreen))
        back_button.pack(padx=20, pady=20)

    def graphic_forecast_one_product(self, tipo_producto):
        datos_historicos = self.db.get_datos_para_pronostico(self.columna_fecha, self.columna_ventas, self.columna_tipo_producto, tipo_producto)

        self.pronostico = Pronostico(datos_historicos, self.columna_fecha, self.columna_ventas, self.periods, self.frequency)
        self.pronostico.metodo_minimos_cuadrados()
        self.pronostico.draw()

    def graphic_forecast_all_product(self):
        datos_historicos = self.db.get_datos_para_pronostico_todas_ventas(self.columna_fecha, self.columna_ventas)

        self.pronostico = Pronostico(datos_historicos, self.columna_fecha, self.columna_ventas, self.periods, self.frequency)
        self.pronostico.metodo_minimos_cuadrados()
        self.pronostico.draw()

    def create_widgets_for_tableTab(self):
        label = ctk.CTkLabel(self.tableTab, text="Visualización de resultados con tablas", font=("Helvetica", 24))
        label.pack()
        draw_product_sales_button = ctk.CTkButton(self.tableTab, text="Generar pronóstico para las ventas de un producto", command=lambda: self.table_forecast_one_product(combo_productos.get()))
        draw_product_sales_button.pack(padx=20, pady=20)
        combo_productos = ctk.CTkComboBox(self.tableTab, values=self.db.get_tipos_productos(columna_tipo_producto=self.columna_tipo_producto))
        combo_productos.pack(padx=20, pady=20)
        draw_all_sales_button = ctk.CTkButton(self.tableTab, text="Generar pronóstico para todas las ventas", command=self.table_forecast_all_product)
        draw_all_sales_button.pack(padx=20, pady=20)
        back_button = ctk.CTkButton(self.tableTab, text="Volver", command=lambda: self.go_to(gui.ParameterScreen.ParameterScreen))
        back_button.pack(padx=20, pady=20)

    def table_forecast_one_product(self, tipo_producto):
        window = ctk.CTkToplevel(self)
        window.geometry("700x500")
        scrollable_frame = ctk.CTkScrollableFrame(window)
        scrollable_frame.pack(expand=True, fill="both")
        datos_historicos = self.db.get_datos_para_pronostico(self.columna_fecha, self.columna_ventas, self.columna_tipo_producto, tipo_producto)

        self.pronostico = Pronostico(datos_historicos, self.columna_fecha, self.columna_ventas, self.periods, self.frequency)
        self.pronostico.metodo_minimos_cuadrados()

        value = self.pronostico.table()

        export_button = ctk.CTkButton(scrollable_frame, text="Exportar", command=lambda: print("Exportar"))
        export_button.pack()
        self.table = CTkTable(scrollable_frame, values=value)
        window.title("Pronóstico para las ventas de un producto")

        self.table.pack(expand=True, fill="both")

    def table_forecast_all_product(self):
        window = ctk.CTkToplevel(self)
        window.geometry("700x500")
        scrollable_frame = ctk.CTkScrollableFrame(window)
        scrollable_frame.pack(expand=True, fill="both")
        datos_historicos = self.db.get_datos_para_pronostico_todas_ventas(self.columna_fecha, self.columna_ventas)

        self.pronostico = Pronostico(datos_historicos, self.columna_fecha, self.columna_ventas, self.periods, self.frequency)
        self.pronostico.metodo_minimos_cuadrados()

        value = self.pronostico.table()
        
        export_button = ctk.CTkButton(scrollable_frame, text="Exportar", command=lambda: print("Exportar"))
        export_button.pack()
        self.table = CTkTable(scrollable_frame, values=value)
        window.title("Pronóstico para todas las ventas")

        self.table.pack(expand=True, fill="both")

    def go_to(self, frame):
        self.destroy()
        frame(self.master)
