from tkinter import ttk
from gui.ConfigurationScreen import ConfigurationScreen

class WelcomeScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill="both")
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="Bienvenido", font="Helvetica 16 bold")
        self.label.pack(pady=10)
        self.start_button = ttk.Button(self, text="Iniciar simulación", command=lambda: self.go_to(ConfigurationScreen))
        self.start_button.pack(pady=10)
        self.help_button = ttk.Button(self, text="Ayuda", command=lambda: print("Ayuda"))
        self.help_button.pack(pady=10)
        self.about_button = ttk.Button(self, text="Acerca de", command=lambda: print("Acerca de"))
        self.about_button.pack(pady=10)

    def go_to(self, frame):
        self.destroy()
        frame(self.master)