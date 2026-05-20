# ==========================================
# ARCHIVO: contrasena.py
# DESCRIPCIÓN: Genera una contraseña aleatoria de 8 caracteres.
# ==========================================

# Importamos el módulo random para generar números aleatorios
import random

# Definimos la clase de excepción personalizada para longitud inválida
class LongitudInvalidaError(Exception):
    """Excepción para longitudes fuera del rango permitido (8-50)."""
    pass