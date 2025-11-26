from time_management import Time
#Clase Base

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
    
class RegistroDiario:
    def __init__(self):
        self._personas = []

    @property
    def personas(self):
        return self._personas
    
    def agregar_persona(self, persona):
        #Agregar una persona (Empleado o Cliente) al registro
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
            print(">> Persona agregada correctamente.")
        else:
            print(">> Error: Solo se pueden agregar Empleados o Clientes.")
    
    def visualizar_registro(self):
        # Llama a visualizar de cada persona en el registro
        print("\n===Registro Completo ===")
        if not self._personas:
            print("Reistro vacío.")
        for i, persona in enumerate(self._personas):
            print("\n[Posición{i}]")
            persona.visualizar()
        print("===================================")

    def visualizar_empleados(self):
        # Visualiza solo los empleados en el registro
        print("\n===Empleados en el Registro===")
        empleados_encontrados = False
        for persona in self._personas:
            if isinstance(persona, Empleado):
                persona.visualizar()
                empleados_encontrados = True
        if not empleados_encontrados:
            print("No hay empleados registrados.")
        print("===================================")
    
    def es_empleado(self, persona):
        # Verifica si una persona es un empleado
        return isinstance(persona, Empleado)
    
    def __getitem__(self, index):
        # Permite acceder a las personas por índice
        if 0 <= index < len(self._personas):
            return self._personas[index]
        else:
            print("Error: Índice fuera de rango.")
            return None
    
    def __add__(self, otro_registro):
    # Permite agregar una persona usando el operador +
    #Creo un registro vacio
        nuevo_registro = RegistroDiario()
    # Añado nuevas personas copiando la referencia

        for p in self._personas:
            nuevo_registro.agregar_persona(p)
        
    # Añado la nueva persona
        if isinstance(otro_registro, RegistroDiario):
            for p in otro_registro.personas:
                nuevo_registro.agregar_persona(p)
        return nuevo_registro   

# --- Bloque de prueba ---
"""if __name__ == "__main__":
    c1 = Cliente("Ana", 25, None, "12345678A")
    c2 = Cliente("Ana", 25, None, "99999999Z") # Mismo nombre y edad, distinto DNI
    c3 = Cliente("Luis", 30, None, "87654321B")

    c1.visualizar()
    
    print("\nComparaciones:")
    print(f"¿Es c1 igual a c2?: {c1 == c2}") # Debería salir True
    print(f"¿Es c1 igual a c3?: {c1 == c3}") # Debería salir False"""