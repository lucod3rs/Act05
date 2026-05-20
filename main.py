# ==========================================
# main.py
# archivo principal del proyecto
#======================================

# Importar las librerías necesarias
import tkinter as tk
from tkinter import messagebox

# Conectamos los módulos cofre y contrasena
from contrasena import Contrasena, LongitudInvalidaError
from cofre import Cofre


# Clase principal del juego
class JuegoCazador:
    #Inicialización de la clase
    def __init__(self):
        self.puntaje = 0
        self.nombre_jugador = ""

       # Variables para la interfaz gráfica 
        self.ventana = None
        self.entrada_nombre = None
        self.entrada_longitud = None
        self.etiqueta_marcador = None

    # Método para iniciar el juego
    def mostrar_recompensa(self, cofre, clave=""):
        #Crea una ventana emergente para mostrar la recompensa al jugador
        top = tk.Toplevel(self.ventana)
        top.title("¡RECOMPENSA!")
        top.geometry("320x280")
        top.resizable(False, False)
        
        top.transient(self.ventana) 
        top.grab_set()


        # Mostrar el nombre del cofre y los puntos obtenidos
        tk.Label(top, text=f"COFRE {cofre.nombre.upper()}", font=("Arial", 16)).pack(pady=15)
        tk.Label(top, text="").pack() 

        # Mostrar la clave correcta si el jugador no adivinó correctamente
        puntos_txt = f"{cofre.puntos} puntos" if cofre.puntos < 0 else f"+{cofre.puntos} puntos"
        tk.Label(top, text=puntos_txt, font=("Arial", 14)).pack(pady=5)

        # Si se proporcionó una clave, mostrarla en la ventana
        if clave: 
            tk.Label(top, text="Contraseña Cazada:", font=("Arial", 10, "italic")).pack(pady=(10,0))
            tk.Label(top, text=clave, font=("Courier", 12, "bold"), relief="ridge", padx=10, pady=5).pack(pady=5)
        
        # Botón Aceptar para cerrar la ventana de recompensa
        tk.Button(top, text="ACEPTAR", command=top.destroy, width=20, font=("Arial", 9)).pack(pady=15)

   
    # Método para iniciar la partida del juego, solicitando el nombre del jugador y mostrando el marcador inicial
    def iniciar_partida(self):
        nombre = self.entrada_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Atención", "Cazador, ingresa tu nombre.")
            return
        
        # Guardar el nombre del jugador y actualizar el marcador en la interfaz
        self.nombre_jugador = nombre
        self.etiqueta_marcador.config(text=f"CAZADOR: {self.nombre_jugador.upper()}  |  PUNTAJE: {self.puntaje}")
        messagebox.showinfo("Caza Iniciada", f"¡Bienvenido, {self.nombre_jugador}!")