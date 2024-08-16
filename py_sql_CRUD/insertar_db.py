import mysql.connector

conexion_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_viernes"
)

cursor = conexion_db.cursor()

# query = """INSERT INTO estudiantes (id , nombre_estudiante , apellido_estudiante , correo , edad ) VALUES ( %s,%s,%s,%s,%s)"""

# datos_estudiante = (123, "Maria", "Lopez", "ml@correo.com", 20)
# cursor.execute(query, datos_estudiante)

# ids = [1087, 1258, 2563, 3654]
# nombres = ["sofia", "juan", "pepe", "sandra"]
# apellidos = ["osorio", "lopez", "aguilar", "hurtado"]
# correos = ["so@gmail.com","jl@gmail.com", "pa@gmail.com", "sh@gmail.com"]
# edades = [18, 20, 29, 17]

# for i in range(len(nombres)):
#     datos_estudiantes = (ids[i], nombres[i], apellidos[i], correos[i], edades[i])
#     cursor.execute(query, datos_estudiantes)

# query = """INSERT INTO asignaturas (cod_asignatura, nombre_asignatura ,horario, id_estudiante ) VALUES ( %s,%s,%s,%s)"""

# cod_asignatura= [358, 698, 785, 256]
# nombre_asignatura = ["Fisica", "Matematicas", "Español", "Ingles"]
# horario = ["7 p.m", "8 a.m", "7 p.m", "6 a.m"]
# id_estudiante = [1087, 1258, 2563, 3654]


# for i in range(len(horario)):
#     datos_asignatura = (cod_asignatura[i], nombre_asignatura[i], horario[i], id_estudiante[i])
#     cursor.execute(query, datos_asignatura)

conexion_db.commit()

cursor.close()
conexion_db.close()