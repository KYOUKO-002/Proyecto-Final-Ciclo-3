from db_conexion import obtener_cliente_mysql


def obtener_id_ci_estudiante():
    cliente=obtener_cliente_mysql()
    cursor=cliente.cursor(dictionary=True)
    cursor.execute("SELECT id_estudiante, ci_pasaporte FROM estudiante")
    resultado = cursor.fetchall()
    cursor.close()
    cliente.close()

    return {fila["ci_pasaporte"]: fila["id_estudiante"] for fila in resultado}


