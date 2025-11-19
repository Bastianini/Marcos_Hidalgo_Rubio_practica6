"""
utils.py
Funciones de utilidad para el sistema de gestión de biblioteca.
"""

from uuid import uuid4
from typing import List


def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Valor no válido. Debes introducir un número entero.")


def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Valor no válido. Debes introducir un número decimal.")


def crear_menu(opciones_menu: List[str]) -> int:
    if not opciones_menu:
        raise ValueError("La lista de opciones del menú no puede estar vacía.")
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    while True:
        opcion = leer_int("Selecciona una opción: ")
        if 1 <= opcion <= len(opciones_menu):
            return opcion
        print("⚠️  Opción no válida, inténtalo de nuevo.")


def generar_id() -> str:
    """Genera un ID único de 8 caracteres."""
    return str(uuid4())[:8]
