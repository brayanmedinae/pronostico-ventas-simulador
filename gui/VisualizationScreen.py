import customtkinter as ctk
import gui.ConfigurationScreen
from pronostico import Pronostico

class VisualizationScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        label = ctk.CTkLabel(self, text="Visualización de resultados")
        label.pack()
        back_button = ctk.CTkButton(self, text="Volver", command=lambda: self.go_to(gui.ConfigurationScreen.ConfigurationScreen))
        back_button.pack()

    def configurar_pronostico(self, datos_historicos):
        self.pronostico = Pronostico(datos_historicos, 'fecha', 'ventas', 10, 'D')
        self.pronostico.metodo_minimos_cuadrados()
        self.pronostico.draw()

    def go_to(self, frame):
        self.destroy()
        frame(self.master)