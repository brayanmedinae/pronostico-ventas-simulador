import customtkinter as ctk
from tkinter import filedialog
import gui.VisualizationScreen
import gui.WelcomeScreen
from datos_historicos import DatosHistoricos
from tkinter.messagebox import showinfo

class ConfigurationScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        label = ctk.CTkLabel(self, text="Datos históricos")
        label.pack(padx=20, pady=20)
        import_button = ctk.CTkButton(self, text="Importar", command=self.select_file)
        import_button.pack(padx=20, pady=20)
        back_button = ctk.CTkButton(self, text="Volver", command=lambda: self.go_to(gui.WelcomeScreen.WelcomeScreen))
        back_button.pack(padx=20, pady=20)
        self.next_button = ctk.CTkButton(self, text="Siguiente", command=lambda: self.go_to(gui.VisualizationScreen.VisualizationScreen), state="disabled")
        self.next_button.pack(padx=20, pady=20)
    
    def select_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)
        if file_path.endswith(".xlsx"):
            self.next_button.configure(state="normal")
            self.datos_historicos = DatosHistoricos()
            self.datos_historicos.crear_datos_historicos(file_path)
            showinfo("Datos históricos", "Datos históricos importados correctamente")


    def go_to(self, frame):
        self.destroy()
        frame(self.master)