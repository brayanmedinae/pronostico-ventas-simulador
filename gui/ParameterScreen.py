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
        self.restore_parameters()
        self.pack(expand=True, fill="both")


    def create_widgets(self):
        db = DatosHistoricos()
        columnas = db.get_todas_las_columnas()
        label = ctk.CTkLabel(self, text="Parámetros de pronóstico", font=("Helvetica", 24))
        label.pack(padx=10, pady=10)
        label_fecha = ctk.CTkLabel(self, text="Columna de fecha:")
        label_fecha.pack()
        self.combo_box_fecha = ctk.CTkComboBox(self, values=columnas)
        self.combo_box_fecha.pack(padx=10, pady=10)
        label_ventas = ctk.CTkLabel(self, text="Columna de ventas:")
        label_ventas.pack()
        self.combo_box_ventas = ctk.CTkComboBox(self, values=columnas)
        self.combo_box_ventas.pack(padx=10, pady=10)
        label_tipo_producto = ctk.CTkLabel(self, text="Columna de tipo de producto:")
        label_tipo_producto.pack()
        self.combo_box_tipo_producto = ctk.CTkComboBox(self, values=columnas)
        self.combo_box_tipo_producto.pack(padx=10, pady=10)
        period_label = ctk.CTkLabel(self, text="Periodos:")
        period_label.pack()
        self.period_entry = CTkSpinbox(self, start_value=1, min_value=1, max_value=30, scroll_value=1)
        self.period_entry.pack(padx=10, pady=10)
        frequency_label = ctk.CTkLabel(self, text="Frecuencia:")
        frequency_label.pack()
        self.frequency_combo = ctk.CTkComboBox(self, values=["Años", "Meses"])
        self.frequency_combo.pack(padx=10, pady=10)

        back_button = ctk.CTkButton(self, text="Volver", command=lambda: self.go_to(gui.WelcomeScreen.WelcomeScreen))
        back_button.pack(padx=10, pady=10)
        self.next_button = ctk.CTkButton(self, text="Siguiente", command=lambda: self.next_window(self.combo_box_fecha.get(), self.combo_box_ventas.get(), self.combo_box_tipo_producto.get(), self.period_entry.get(), "YE" if self.frequency_combo.get() == "Años" else "MS"))
        self.next_button.pack(padx=10, pady=10)


    def restore_parameters(self):
        config = configparser.ConfigParser()
        config.read('parameters.ini')
        self.combo_box_fecha.set(config['PARAMETERS']['columna_fecha'])
        self.combo_box_ventas.set(config['PARAMETERS']['columna_ventas'])
        self.combo_box_tipo_producto.set(config['PARAMETERS']['columna_tipo_producto'])
        self.period_entry.set(int(config['PARAMETERS']['periods']))
        if config['PARAMETERS']['frequency'] == 'YE':
            self.frequency_combo.set("Años")
        else:
            self.frequency_combo.set("Meses")


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