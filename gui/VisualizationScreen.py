from tkinter import ttk

class VisualizationScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        self.label = ttk.Label(self, text="Visualización de resultados", font="Helvetica 16 bold")
        self.label.pack(pady=10)
    
    def go_to(self, frame):
        self.destroy()
        frame(self.master)