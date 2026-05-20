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
