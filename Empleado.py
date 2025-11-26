from Ficha import Ficha

class Empleado(Ficha):
    def __init__(self, nombre = "", edad = 0, nacio = None, categoria = "", antiguedad = 0):
        super().__init__(nombre, edad, nacio)
        
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, valor):
        self._antiguedad = valor

    def visualizar(self):
        super().visualizar()
        print(f"Categoria: {self._categoria}")
        print(f"Antiguedad: {self._antiguedad} años")