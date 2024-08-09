# Importar las librerias
import json
import os

# Funcion para limpiar la panatalla
def limpiar():
    os_name = os.name
    os.system('cls' if os_name == 'nt' else 'clear')

# Funcion que leer de la BD json
def leer_bd(archivo):
    with open (archivo, 'r', encoding='utf-8') as file:
        return json.load(file)

# Funcion para guardar los datos en la BD
def guardar_bd(archivo, datos):
    with open (archivo, 'w') as file:
        json.dump(datos, file, indent=4)

# Funcion para crear usuarios
def crear_usu(archivo):
    usuarios = leer_bd(archivo)

    identificacion = input("Ingrese su ID: ")

    # Comprobar que el usuario no exista 
    if identificacion in usuarios:
        print("El usuario ya se encuentra en la BD")
        return
    
    # Usuario Ingresa los datos
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    correo = input("Ingrese su correo: ")

    #Guardo los datos en un diccionario con la ID como clave:
    usuarios[identificacion] = {
        "nombre" : nombre,
        "apellido" : apellido,
        "edad" : edad,
        "correo" : correo
    }
    
    guardar_bd(archivo, usuarios)
    print(f"El usuario {nombre} fue creado con exito")

# Funcion para mostrar usuarios
def mostrar_usu(archivo):
    usuarios = leer_bd(archivo)

    if not usuarios:
        print("No hay usuarios registrados")
    else:
        for id, datos in usuarios.items():
            print(f"ID: {id}, Nombre: {datos['nombre']}, Apellido: {datos['apellido']}, Edad: {datos['edad']}, Correo: {datos['correo']}")
    
def actualizar_usu(archivo):
    usuarios = leer_bd(archivo)

    identificacion = input("Ingrese la ID del usuario para actualizar: ")

    if identificacion not in usuarios:
        print("Usuario no Encontrado")
        return
    
    nombre = input("Ingrese nuevo nombre: ")
    apellido = input("Ingrese nuevo apellido: ")
    edad = input("Ingrese nueva edad: ")
    correo = input("Ingrese nuevo correo: ")

    usuarios[identificacion] = {
        "nombre" : nombre,
        "apellido" : apellido,
        "edad" : edad,
        "correo" : correo
    }

    guardar_bd(archivo, usuarios)
    print(f"El usuario {identificacion} fue actualizado con exito")

# Funcion para Borrar Usuario
def borrar_usu(archivo):
    usuarios = leer_bd(archivo)

    identificacion = input("Ingrese la ID del usuario para borrar: ")

    if identificacion not in usuarios:
        print("Usuario no encontrado")
        return
    
    del usuarios[identificacion]
    guardar_bd(archivo, usuarios)

#Funcion de Menu Principal
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





