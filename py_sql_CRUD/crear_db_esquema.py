import mysql.connector

conexion_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_viernes"
    # Si el puerto da error se debe configurar el puerto
    # port = 3307
)

cursor = conexion_db.cursor()

query = """ CREATE TABLE estudiantes (id INT PRIMARY KEY, nombre_estudiante VARCHAR(25), apellido_estudiante VARCHAR(25), correo VARCHAR(25), edad INT)"""
cursor.execute(query)

query = """CREATE TABLE asignaturas (cod_asignatura INT PRIMARY KEY, nombre_asignatura VARCHAR(50), horario VARCHAR(50), id_estudiante INT, FOREIGN KEY(id_estudiante) REFERENCES estudiantes(id))"""
cursor.execute(query)


# Ejecutar el query
cursor.execute(query)

# Actualizando cambios en la base de datos
conexion_db.commit()

# Cerrar conexion
cursor.close()  
conexion_db.close()
