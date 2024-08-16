import mysql.connector

# Conexion al cliente de la base de datos
conexion_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

# Creamos un cursor para intercambiar informacion entre python y Mysql
# Conecta a python con mysql 
cursor = conexion_db.cursor()

# Definir el query(consulta) que queremos realizar
db_query = "CREATE DATABASE db_viernes"

# Ejecutar el query/consulta
cursor.execute(db_query)

# Cerrar conexion
cursor.close()
conexion_db.close()

