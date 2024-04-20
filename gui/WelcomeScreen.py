import customtkinter as ctk
import gui.ConfigurationScreen
from PIL import Image, ImageTk

class WelcomeScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand=True, fill="both")
        self.create_widgets()

    def create_widgets(self):
        label = ctk.CTkLabel(self, text="Bienvenido", font=("Helvetica", 24))
        label.pack(padx=20, pady=20)
        start_button = ctk.CTkButton(self, text="Iniciar simulación", command=lambda: self.go_to(gui.ConfigurationScreen.ConfigurationScreen))
        logo = Image.open("logo.png").resize((100, 100))
        logo = ImageTk.PhotoImage(logo)
        logo_label = ctk.CTkLabel(self, image=logo, text="")
        logo_label.pack(padx=20, pady=20)
        start_button.pack(padx=20, pady=20)
        help_button = ctk.CTkButton(self, text="Ayuda", command=lambda: print("Ayuda"))
        help_button.pack(padx=20, pady=20)
        about_button = ctk.CTkButton(self, text="Acerca de", command=lambda: print("Acerca de"))
        about_button.pack(padx=20, pady=20)

    def go_to(self, frame):
        self.destroy()
        frame(self.master)