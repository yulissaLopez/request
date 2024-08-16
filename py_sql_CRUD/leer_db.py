import mysql.connector

conexion_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_viernes"
)

cursor = conexion_db.cursor()

#query = """SELECT * FROM estudiantes"""
query = """SELECT * FROM estudiantes WHERE id = (%s)"""

value = (1087, )

cursor.execute(query, value)

# Eempaqueta los datos de la consulta en una tupla
estudiantes = cursor.fetchall()

# Trabajar con la informacion
print("Informacion obtenida con SELECT a la tabla estudiantes ")

for estudiante in estudiantes:
    print(f"id = {estudiante[0]}")
    print(f"nombre = {estudiante[1]}")
    print(f"apellido = {estudiante[2]}")
    print(f"correo = {estudiante[3]}")
    print(f"edad = {estudiante[4]}")