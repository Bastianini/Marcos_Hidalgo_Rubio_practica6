from registro import RegistroDiario, Cliente, Empleado
import utils2

def main():

    registro_diario = RegistroDiario() #registro vacío al empezar el programa
    while True: #opciones del menú
        opciones = [
            "Introducir empleado"
            "Introducir cliente"
            "Buscar por nombre (y edad)"
            "Mostrar registro diario"
            "Mostrar empleados"
            "Visualizar persona por índice"
            "Combinar registros diarios"
            "Salir"
        ]

    while True:
        opcion = utils2.crear_menu(opciones)
    
        #opción 1 introducir empleado

        if opcion == 1:
            print("-----Nuevo Empleado-----")

            #Recogida de empleado
            nombre = utils2.leer_cadena("Nombre: ")
            edad = utils2.leer_int("Edad: ")
            cat = utils2.leer_cadena("Categoría: ")
            ant  = utils2.leer_int("Antigüedad(en años): ")

            emp = Empleado(nombre, edad, None, cat, ant)
            registro.agregar_persona(emp)

        elif opcion == 2:
            print("-----Nuevo Cliente-----")

            #recogida de cliente

            nombre = utils2.leer_cadena("Nombre: ")
            edad = utils2.leer_int("Edad: ")
            dni = utils2.leer_cadena("DNI: ")

            cli = Cliente(nombre, edad, None, dni)
            registro.agregar_persona(cli)

        elif opcion == 3:
            busc_nom = utils2.leer_cadena("Nombre: ")
            busc_edad = utils2.leer_int("Edad: ")

            encontrado = False

            for p in registro.personas:
                if p.nombre == nom_busc and p.edad == edad_busc:
                    print("\n>> ¡Persona Encontrada!")
                    # Usamos tu método es_empleado para saber qué es
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
        elif opcion == 6:
            idx = utils2.leer_int("Introduce el índice (empieza en 0): ")
            
            # Esto funciona gracias al método __getitem__ corregido
            persona = registro[idx] 
            
            if persona: # Si devuelve None es que falló el índice
                print(f"\nDatos en la posición {idx}:")                
                persona.visualizar()

        # --- OPCIÓN 7: Combinar (Prueba del operador +) ---
        elif opcion == 7:
            print("\nGenerando un registro temporal automático...")
            otro_registro = RegistroDiario()
            
            # Añadimos datos "falsos" para probar que se suman
            e_extra = Empleado("EmpleadoTest", 99, None, "Prueba", 1)
            c_extra = Cliente("ClienteTest", 99, None, "0000X")
            otro_registro.agregar_persona(e_extra)
            otro_registro.agregar_persona(c_extra)
            
            print(f"Registro temporal creado con {len(otro_registro.personas)} personas.")
            
            # AQUÍ OCURRE LA MAGIA DEL MÉTODO __add__
            # Estamos sumando dos objetos: registro = registro + otro_registro
            registro = registro + otro_registro
            
            print("¡Fusión completada! Ahora el registro principal tiene más gente.")
            print("(Usa la opción 4 para verlos)")

        # --- OPCIÓN 8: Salir ---
        elif opcion == 8:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()    


