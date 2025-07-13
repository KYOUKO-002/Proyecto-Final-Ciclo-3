from db_conexion import obtener_cliente_mysql


def obtener_id_ci_estudiante():
    cliente=obtener_cliente_mysql()
    cursor=cliente.cursor(dictionary=True)
    cursor.execute("SELECT id_estudiante, ci_pasaporte FROM estudiante")
    resultado = cursor.fetchall()
    cursor.close()
    cliente.close()

    return {fila["ci_pasaporte"]: fila["id_estudiante"] for fila in resultado}


def obtener_id_codigo_carrera():
    cliente=obtener_cliente_mysql()
    cursor=cliente.cursor(dictionary=True)
    cursor.execute("SELECT id_carrera, codigo_carrera FROM carrera")
    resultado = cursor.fetchall()
    cursor.close()
    cliente.close()

    return {fila["codigo_carrera"]: fila["id_carrera"] for fila in resultado}


def obtener_id_nombre_asignaturas():
    cliente=obtener_cliente_mysql()
    cursor=cliente.cursor(dictionary=True)
    cursor.execute("SELECT id_asignatura, nombre_asignatura FROM asignatura")
    resultado = cursor.fetchall()
    cursor.close()
    cliente.close()

    return {fila["nombre_asignatura"]: fila["id_asignatura"] for fila in resultado}


def obtener_id_por_columnas_aux_estudiante_carrera():
    cliente=obtener_cliente_mysql()
    cursor=cliente.cursor(dictionary=True)
    cursor.execute("SELECT id_estudiante_carrera, id_carrera, id_estudiante, periodo_academico FROM estudiante_carrera")
    resultado = cursor.fetchall()
    cursor.close()
    cliente.close()

    return {f'{fila["id_carrera"]}-{fila["id_estudiante"]}-{fila["periodo_academico"]}': fila["id_estudiante_carrera"] for fila in resultado}    