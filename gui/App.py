from tkinter import ttk
import gui.WelcomeScreen

class App(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Simulador de pronóstico de ventas")
        self.master.geometry("800x600")

        self.welcome = gui.WelcomeScreen.WelcomeScreen(self.master)