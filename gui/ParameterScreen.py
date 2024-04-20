import customtkinter as ctk
import gui.WelcomeScreen
import gui.VisualizationScreen
from datos_historicos import DatosHistoricos
from CTkSpinbox import CTkSpinbox
import configparser


class ParameterScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        db = DatosHistoricos()
        columnas = db.get_todas_las_columnas()
        label = ctk.CTkLabel(self, text="Parámetros de pronóstico", font=("Helvetica", 24))
        label.pack(padx=10, pady=10)
        label_fecha = ctk.CTkLabel(self, text="Columna de fecha:")
        label_fecha.pack()
        combo_box_fecha = ctk.CTkComboBox(self, values=columnas)
        combo_box_fecha.pack(padx=10, pady=10)
        label_ventas = ctk.CTkLabel(self, text="Columna de ventas:")
        label_ventas.pack()
        combo_box_ventas = ctk.CTkComboBox(self, values=columnas)
        combo_box_ventas.pack(padx=10, pady=10)
        label_tipo_producto = ctk.CTkLabel(self, text="Columna de tipo de producto:")
        label_tipo_producto.pack()
        combo_box_tipo_producto = ctk.CTkComboBox(self, values=columnas)
        combo_box_tipo_producto.pack(padx=10, pady=10)
        period_label = ctk.CTkLabel(self, text="Años:")
        period_label.pack()
        period_entry = CTkSpinbox(self, start_value=1, min_value=1, max_value=10, scroll_value=1)
        period_entry.pack(padx=10, pady=10)
        frequency_label = ctk.CTkLabel(self, text="Frecuencia:")
        frequency_label.pack()
        frequency_combo = ctk.CTkComboBox(self, values=["Años", "Meses"])
        frequency_combo.pack(padx=10, pady=10)

        back_button = ctk.CTkButton(self, text="Volver", command=lambda: self.go_to(gui.WelcomeScreen.WelcomeScreen))
        back_button.pack(padx=10, pady=10)
        self.next_button = ctk.CTkButton(self, text="Siguiente", command=lambda: self.next_window(combo_box_fecha.get(), combo_box_ventas.get(), combo_box_tipo_producto.get(), period_entry.get(), "YE" if frequency_combo.get() == "Años" else "MS"))
        self.next_button.pack(padx=10, pady=10)
        
    def next_window(self, fecha, ventas, tipo_producto, periods, frequency):
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        config['PARAMETERS'] = {
            'columna_fecha': fecha,
            'columna_ventas': ventas,
            'columna_tipo_producto': tipo_producto,
            'periods': periods,
            'frequency': frequency
        }
        with open('parameters.ini', 'w') as configfile:
            config.write(configfile)
        self.go_to(gui.VisualizationScreen.VisualizationScreen)

    def go_to(self, frame):
        self.destroy()
        frame(self.master)