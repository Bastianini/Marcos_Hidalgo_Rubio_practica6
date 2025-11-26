from time_management import Time

class Ficha:
    def __init__(self, nombre = "", edad = 0, nacio = None):
        # Atributos potegidos
        self._nombre = nombre
        self._edad = edad
        
        if nacio is None:
            t = Time()
            t.set_time(12, 0, 0, "AM")
            self._nacio = t
        else:
            self._nacio = nacio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def nacio(self):
        return self._nacio

    @nacio.setter
    def nacio(self, valor):
        self._nacio = valor

    def visualizar(self):
        print(f"Nombre: {self._nombre}")
        print(f"Edad: {self._edad}")
        if self._nacio:
            print(f"Nacio: {self._nacio.get_time()}") 