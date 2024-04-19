from tkinter import ttk
from tkinter import filedialog
from gui.VisualizationScreen import VisualizationScreen

class ConfigurationScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        self.label = ttk.Label(self, text="Datos históricos", font="Helvetica 16 bold")
        self.label.pack(pady=10)
        self.import_button = ttk.Button(self, text="Importar", command=self.select_file)
        self.import_button.pack(pady=10)
        self.next_button = ttk.Button(self, text="Siguiente", command=lambda: self.go_to(VisualizationScreen))
        self.next_button.pack(pady=10)
    
    def select_file(self):
        file_path = filedialog.askopenfilename()
        print(file_path)

    def go_to(self, frame):
        self.destroy()
        frame(self.master)