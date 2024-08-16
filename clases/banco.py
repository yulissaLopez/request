import json


class Banco:
    """
    Clase para crear bancos con sus respectivos métodos de
    operación.
    """
    def __init__(
        self, nombre, direccion,
        dinero, trabajadores, sucursales
        ):

        self.nombre = nombre
        self.direccion = direccion
        self.dinero = dinero
        self.trabajadores = trabajadores
        self.sucursales = sucursales



class AdministrarBanco:

    def invertir_bolsa(self):
        print("Todo el dinero del banco esta siendo invertido !!")

    def cobrar_intereses(self, nombre_cliente, deuda, interes):
        valor_pagar = deuda + (deuda*interes)

        print(f"Estimado {nombre_cliente} ahora tiene que pagar {valor_pagar}")

    def entregar_dinero(self, nombre_cliente, cantidad):
        print(f"El usuario {nombre_cliente}, retiró {cantidad} pesos")
        
        datos = {
            "nombre_cliente": nombre_cliente,
            "cantidad_retirada": cantidad
        }
        lista_clientes = []
        try:
            with open("clientes.json", "r") as archivo:
                lista_clientes = archivo.load()
                lista_clientes.append(datos)
            
                with open("clientes.json", "w") as archivo2:
                    json.dump(lista_clientes, archivo2)
        except:
            # clientes = []
            with open("clientes.json", "w") as archivo:
                lista_clientes.append(datos)
                json.dump(lista_clientes, archivo)

    def recibir_dinero(self, nombre_cliente, cantidad, fecha):
        print(f"El usuario {nombre_cliente}, consignó {cantidad} pesos")


banco1 = Banco("Banco ADSO", "Calle 20 Cra 6", 500000000, 50, 10)
print(f"Bienvenido al {banco1.nombre}")
print("\n")

admin_banco = AdministrarBanco()
admin_banco.cobrar_intereses("Juana De Arco", 100000000, 0.05)
admin_banco.entregar_dinero("Ana Maria", 2000000)
admin_banco.entregar_dinero("Valeria", 5000000)

