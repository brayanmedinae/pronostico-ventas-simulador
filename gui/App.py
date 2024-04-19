from tkinter import ttk
from gui.WelcomeScreen import WelcomeScreen

class App(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Simulador de pronóstico de ventas")
        self.master.geometry("800x600")

        self.welcome = WelcomeScreen(self.master)