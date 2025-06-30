# ============================ ESTUDIANTE ============================
import modulos.db.conexion as db


def crear_estudiante(estudiante):
    cliente = db.cliente_mysql()


def existe_estudiante_por_identificacion(identificacion):
    cliente = db.cliente_mysql()

    cursor = cliente.cursor()
    query = "SELECT 1 FROM estudiante WHERE identificacion = %s LIMIT 1"
    cursor.execute(query, (identificacion,))
    
    resultado = cursor.fetchone()

    cursor.close()
    cliente.close()

    return resultado is not None