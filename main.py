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