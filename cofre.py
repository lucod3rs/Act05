# ==========================================
# ARCHIVO: cofre.py
# DESCRIPCIÓN: Implementación de la clase Cofre
# Que representa un cofre del tesoro en un juego de aventuras.
# ==========================================

#Importamos el módulo random para generar números aleatorios
import random

#Definimos la clase Cofre
class Cofre:
    def __init__(self, nombre, puntos): #El método __init__ es el constructor de la clase Cofre. Recibe dos parámetros: nombre y puntos.
        self.nombre = nombre
        self.puntos = puntos