# ==========================================
# ARCHIVO: contrasena.py
# DESCRIPCIÓN: Genera una contraseña aleatoria de 8 caracteres.
# ==========================================

# Importamos el módulo random para generar números aleatorios
import random

# Definimos la clase de excepción personalizada para longitud inválida
class LongitudInvalidaError(Exception):
    #Excepción para longitudes fuera del rango permitido (8-50).
    pass

#Definimos la clase Contrasena para generar contraseñas aleatorias
class Contrasena:
    # Bancos de caracteres para la generación
    MAYUSCULAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    MINUSCULAS = "abcdefghijklmnopqrstuvwxyz"
    NUMEROS = "0123456789"
    ESPECIALES = "i?=)(/**+-%&$#!."

    # Constructor de la clase Contrasena
    def __init__(self, longitud):
        self.longitud = longitud
        self.valor = ""

    # Método para generar la contraseña
    def validar_longitud(self):
        #Verifica que la longitud esté en el rango permitido (8-50).
        if self.longitud < 8:
            raise LongitudInvalidaError("La longitud debe ser de mínimo 8 caracteres.")
        if self.longitud > 50:
            raise LongitudInvalidaError("La longitud no puede superar los 50 caracteres.")