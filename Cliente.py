from Ficha import Ficha

class Cliente(Ficha):
    def __init__(self, nombre= "", edad = 0, nacio = None, dni = ""):
        super().__init__(nombre, edad, nacio)
        self._dni = dni
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, valor):
        self._dni = valor

    def visualizar(self):
        super().visualizar()
        print(f"DNI: {self._dni}")

    def __eq__(self, otro_cliente):
        #Verificar que el otro objeto sea una instancia de Cliente
        es_cliente = isinstance(otro_cliente, Cliente)
        
        if not es_cliente:
            return False
        
        #La comparación real
        mismo_nombre = (self.nombre == otro_cliente.nombre)
        misma_edad = (self.edad == otro_cliente.edad)
        
        return mismo_nombre and misma_edad