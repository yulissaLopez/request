from funciones import limpiar, leer_bd, guardar_bd, crear_usu, mostrar_usu, actualizar_usu

def menu():
    archivo = "BD.json"

    while True:
        #limpiar()
        print("-" * 64)
        print("CRUD para Usuarios")
        print("1. Crear usuario")
        print("2. Mostrar usuarios")
        print("3. Actualizar usuario")
        print("4. Borrar usuario")
        print("5. Salir")

        opcion = input("Elija la opcion deseada: ")

        if opcion == "1":
            limpiar()
            crear_usu(archivo)
        elif opcion == "2":
            limpiar()
            mostrar_usu(archivo)
        elif opcion == "3":
            limpiar()
            actualizar_usu(archivo)
        elif opcion == "4":
            limpiar()
            borrar_usu(archivo)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
