from registro import RegistroDiario, Cliente, Empleado
import utils2
from time_management import Time #Para usar la fecha de nacimiento

def main():
    # Creamos el registro. Lo llamaremos 'registro' para usarlo igual en todo el código
    registro = RegistroDiario() 

    # Definimos la lista de opciones (¡Fíjate en las comas al final!)
    opciones = [
        "Introducir empleado",
        "Introducir cliente",
        "Buscar por nombre (y edad)",
        "Mostrar registro diario",
        "Mostrar empleados",
        "Visualizar persona por índice",
        "Combinar registros diarios",
        "Salir"
    ]

    while True:
        # Mostramos el menú y pedimos opción
        print("\n--- MENÚ PRINCIPAL ---")
        opcion = utils2.crear_menu(opciones)
    
        # --- OPCIÓN 1: Introducir Empleado ---
        if opcion == 1:
            print("\n-----Nuevo Empleado-----")
            nombre = utils2.leer_cadena("Nombre: ")
            edad = utils2.leer_int("Edad: ")
            
            # --- NUEVA LÓGICA DE HORA ---
            print("Formato de hora: HH:MM:SS AM/PM (Ej: 08:30:00 AM)")
            hora_str = utils2.leer_cadena("Hora de entrada: ")
            # Convertimos el texto a objeto Time
            hora_objeto = Time.from_string(hora_str)
            # -----------------------------

            cat = utils2.leer_cadena("Categoría: ")
            ant  = utils2.leer_int("Antigüedad (en años): ")

            # Pasamos 'hora_objeto' en lugar de None
            emp = Empleado(nombre, edad, hora_objeto, cat, ant)
            registro.agregar_persona(emp)

        # --- OPCIÓN 2: Introducir Cliente ---
        elif opcion == 2:
            print("\n-----Nuevo Cliente-----")
            nombre = utils2.leer_cadena("Nombre: ")
            edad = utils2.leer_int("Edad: ")
            
            # --- NUEVA LÓGICA DE HORA ---
            print("Formato de hora: HH:MM:SS AM/PM (Ej: 10:45:00 AM)")
            hora_str = utils2.leer_cadena("Hora de visita: ")
            hora_objeto = Time.from_string(hora_str)
            # -----------------------------

            dni = utils2.leer_cadena("DNI: ")

            # Pasamos 'hora_objeto' en lugar de None
            cli = Cliente(nombre, edad, hora_objeto, dni)
            registro.agregar_persona(cli)

        # --- OPCIÓN 3: Buscar ---
        elif opcion == 3:
            # Corregido: Nombres de variables coincidentes
            nom_busc = utils2.leer_cadena("Nombre a buscar: ")
            edad_busc = utils2.leer_int("Edad a buscar: ")

            encontrado = False

            for p in registro.personas:
                if p.nombre == nom_busc and p.edad == edad_busc:
                    print("\n>> ¡Persona Encontrada!")
                    tipo = "Empleado" if registro.es_empleado(p) else "Cliente"
                    print(f"Tipo: {tipo}")
                    p.visualizar()
                    encontrado = True
            
            if not encontrado:
                print("No se ha encontrado a nadie con esos datos.")

        # --- OPCIÓN 4: Mostrar todo ---
        elif opcion == 4:
            registro.visualizar_registro()

        # --- OPCIÓN 5: Mostrar solo empleados ---
        elif opcion == 5:
            registro.visualizar_empleados()

        # --- OPCIÓN 6: Por índice ---
       # En main.py - OPCIÓN 6
        elif opcion == 6:
            # Pedimos el número "humano"
            idx_usuario = utils2.leer_int("Introduce el número de la lista (empieza en 1): ")
            
            # Convertimos a índice de Python (restamos 1)
            idx_interno = idx_usuario - 1
            
            # Usamos el índice interno para buscar
            persona = registro[idx_interno] 
            
            if persona: 
                print(f"\nDatos en la posición {idx_usuario}:")                
                persona.visualizar()

        # --- OPCIÓN 7: Combinar ---
        elif opcion == 7:
            print("\nGenerando un registro temporal automático...")
            otro_registro = RegistroDiario()
            
            # Datos de prueba
            e_extra = Empleado("EmpleadoTest", 99, None, "Prueba", 1)
            c_extra = Cliente("ClienteTest", 99, None, "0000X")
            otro_registro.agregar_persona(e_extra)
            otro_registro.agregar_persona(c_extra)
            
            # Sumamos los registros y actualizamos la variable principal
            registro = registro + otro_registro
            
            print("¡Fusión completada! (Usa la opción 4 para ver el resultado)")

        # --- OPCIÓN 8: Salir ---
        elif opcion == 8:
            print("Saliendo del programa...")
            return # 'return' termina la función main y cierra el programa

if __name__ == "__main__":
    main()
