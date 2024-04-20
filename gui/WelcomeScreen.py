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
        about_button = ctk.CTkButton(self, text="Acerca de", command=self.about_window)
        about_button.pack(padx=20, pady=20)

    def help_window(self):
        help_window = ctk.CTkToplevel(self.master)
        help_window.focus_force()
        help_window.title("Ayuda")
        help_window.geometry("600x500")
        help_window_label = ctk.CTkLabel(help_window, text="Ayuda del simulador de pronóstico de ventas", font=("Helvetica", 16))
        help_window_label.pack()
        help_window_text = ctk.CTkTextbox(help_window, font=("Helvetica", 12))
        help_window_text.insert("1.0", "Este simulador de pronóstico de ventas le permitirá realizar un pronóstico de ventas a partir de datos históricos. Para ello, siga los siguientes pasos:\n\n1. Importe los datos históricos en formato Excel (.xlsx) haciendo clic en el botón 'Importar'.\n\n2. Seleccione la columna de fecha, la columna de ventas y la columna de tipo de producto.\n\n3. Ingrese la cantidad de años a pronosticar y seleccione la frecuencia del pronóstico (años o meses).\n\n4. Haga clic en el botón 'Siguiente' para visualizar los resultados del pronóstico.")
        help_window_text.pack(expand=True, fill="both")

    def about_window(self):
        about_window = ctk.CTkToplevel(self.master)
        about_window.focus_force()
        about_window.title("Acerca de")
        about_window.geometry("600x500")
        about_window_label = ctk.CTkLabel(about_window, text="Acerca de", font=("Helvetica", 16))
        about_window_label.pack()
        about_window_text = ctk.CTkTextbox(about_window, font=("Helvetica", 12), height=400, width=500)
        about_window_text.insert("1.0", "Simulador de pronóstico de ventas\n\nVersión 1.0\n\nDesarrollado por: Equipo 5\n\n2024")
        about_window_text.pack(expand=True, fill="both")


    def go_to(self, frame):
        self.destroy()
        frame(self.master)