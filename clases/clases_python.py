# Clases:

# Clase (molde) de perros:

class Perro:
    """Esta clase crea instancias de Perros"""
    # Atributos de clase:
    # ciudad_nacimiento = Pereira

    # Constructor:
    def __init__(self, nombre, raza, edad):
        """
            Constructor de la clase Perro con tres parámetros:
            nombre, raza, edad
        """
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    # Métodos de clase:
    def ladrar(self):
        return print(f"Estoy ladrando !!")
    
    def comer(self):
        print("Estoy comiendo")


class SuperPerro(Perro):
    
    def volar(self):
        print("Hola, estoy volando")

    def telkinesis(self):
        print("Estoy leyendo tu mente. Dame comida !!!")



print("*"*64)
perro_1 = Perro(nombre="Toby", raza="Criollito", edad=2)
print(f"El perro {perro_1.nombre} es de raza {perro_1.raza} y tiene {perro_1.edad} años")
perro_1.ladrar()

print("*"*64)
perro_2 = Perro(nombre="Toki", raza="Yorkie", edad=5)
print(f"El perro {perro_2.nombre} es de raza {perro_2.raza} y tiene {perro_2.edad} años")
perro_2.comer()

# 
super_perro_1 = SuperPerro(nombre="Cerebro", raza="Golden", edad=10)
print("\n")
print("Hola, mi nombre es {}".format(super_perro_1.nombre))
super_perro_1.telkinesis()
super_perro_1.ladrar()
print("\n")


