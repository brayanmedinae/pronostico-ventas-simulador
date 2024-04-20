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
        help_button = ctk.CTkButton(self, text="Ayuda", command=self.help_window)
        help_button.pack(padx=20, pady=20)
        about_button = ctk.CTkButton(self, text="Acerca de simulador", command=self.about_window)
        about_button.pack(padx=20, pady=20)

    def help_window(self):
        help_text = open("help.txt", "r", encoding='utf-8').read()
        help_window = ctk.CTkToplevel(self.master)
        help_window.focus_force()
        help_window.title("Ayuda")
        help_window.geometry("600x500")
        help_window_label = ctk.CTkLabel(help_window, text="Ayuda del simulador de pronóstico de ventas", font=("Helvetica", 16))
        help_window_label.pack()
        help_window_text = ctk.CTkTextbox(help_window, font=("Helvetica", 12), wrap="word")
        help_window_text.insert("1.0", help_text)
        help_window_text.pack(expand=True, fill="both")

    def about_window(self):
        about_txt = open("about.txt", "r", encoding='utf-8').read()
        about_window = ctk.CTkToplevel(self.master)
        about_window.focus_force()
        about_window.title("Acerca de")
        about_window.geometry("600x500")
        about_window_label = ctk.CTkLabel(about_window, text="Acerca de", font=("Helvetica", 16))
        about_window_label.pack()
        about_window_text = ctk.CTkTextbox(about_window, font=("Helvetica", 12), wrap="word")
        about_window_text.insert("1.0", about_txt)
        about_window_text.pack(expand=True, fill="both")


    def go_to(self, frame):
        self.destroy()
        frame(self.master)