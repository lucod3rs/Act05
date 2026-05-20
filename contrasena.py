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