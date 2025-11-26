from Empleado import Empleado
from Cliente import Cliente

class RegistroDiario:
    def __init__(self):
        self._personas = []

    @property
    def personas(self):
        return self._personas
    
    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
            print(">> Persona agregada correctamente.")
        else:
            print(">> Error: Solo se pueden agregar Empleados o Clientes.")
    
    def visualizar_registro(self):
        print("\n===Registro Completo ===")
        if not self._personas:
            print("Registro vacío.")
        for i, persona in enumerate(self._personas):
            # Aquí está el arreglo del índice visual
            print(f"\n[Posición {i + 1}]")
            persona.visualizar()
        print("===================================")

    def visualizar_empleados(self):
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
        return isinstance(persona, Empleado)
    
    def __getitem__(self, index):
        # Permite acceder a las personas por índice
        if 0 <= index < len(self._personas):
            return self._personas[index]
        else:
            print("Error: Índice fuera de rango.")
            return None
    
    def __add__(self, otro_registro):
        nuevo_registro = RegistroDiario()
        
        for p in self._personas:
            nuevo_registro.agregar_persona(p)
        
        if isinstance(otro_registro, RegistroDiario):
            for p in otro_registro.personas:
                nuevo_registro.agregar_persona(p)
        return nuevo_registro