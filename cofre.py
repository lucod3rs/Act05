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

   #Definimos un método de clase para generar un cofre aleatorio
    @classmethod
    def generar_cofre_aleatorio(cls):
        #Elige al azar un cofre, cada uno con un nombre y una cantidad de puntos diferente
        opciones = [
            ("Comun", 10),      
            ("Raro", 25),       
            ("Legendario", 50)   
        ]
        nombre, puntos = random.choice(opciones)
        return cls(nombre, puntos)