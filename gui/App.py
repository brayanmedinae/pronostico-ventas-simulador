import customtkinter as ctk
import gui.WelcomeScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.root = self
        self.root.title("Simulador de pronóstico de ventas")
        self.root.geometry("800x600")
        
        self.welcome = gui.WelcomeScreen.WelcomeScreen(self.master)