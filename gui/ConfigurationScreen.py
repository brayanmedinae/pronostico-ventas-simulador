from tkinter import ttk
from tkinter import filedialog
import gui.VisualizationScreen
import gui.WelcomeScreen

class ConfigurationScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        label = ttk.Label(self, text="Datos históricos", font="Helvetica 16 bold")
        label.pack(pady=10)
        import_button = ttk.Button(self, text="Importar", command=self.select_file)
        import_button.pack(pady=10)
        back_button = ttk.Button(self, text="Volver", command=lambda: self.go_to(gui.WelcomeScreen.WelcomeScreen))
        back_button.pack(pady=10)
        next_button = ttk.Button(self, text="Siguiente", command=lambda: self.go_to(gui.VisualizationScreen.VisualizationScreen))
        next_button.pack(pady=10)
    
    def select_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)


    def go_to(self, frame):
        self.destroy()
        frame(self.master)