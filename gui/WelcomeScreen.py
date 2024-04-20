from tkinter import ttk
import gui.ConfigurationScreen

class WelcomeScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill="both")
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Bienvenido", font="Helvetica 16 bold")
        label.pack(pady=10)
        start_button = ttk.Button(self, text="Iniciar simulación", command=lambda: self.go_to(gui.ConfigurationScreen.ConfigurationScreen))
        start_button.pack(pady=10)
        help_button = ttk.Button(self, text="Ayuda", command=lambda: print("Ayuda"))
        help_button.pack(pady=10)
        about_button = ttk.Button(self, text="Acerca de", command=lambda: print("Acerca de"))
        about_button.pack(pady=10)

    def go_to(self, frame):
        self.destroy()
        frame(self.master)