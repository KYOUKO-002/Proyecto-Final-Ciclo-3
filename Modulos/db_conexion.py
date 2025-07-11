import mysql.connector
from mysql.connector import Error

def obtener_cliente_mysql():
    """Establece una conexión a la base de datos MySQL y devuelve el objeto de conexión."""
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='FichasNotasDB',
            user='root',
            password='1234'
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos MySQL")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos MySQL: {e}")
        return None



