from modulos.db.conexion import cliente_mysql
from modulos.db.modelos import Estudiante

# ============================ ESTUDIANTE ============================
def insertar_estudiantes_en_lote(estudiantes: list):
    if not estudiantes:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        sql = "INSERT IGNORE INTO estudiante (identificacion, nombres_estudiante) VALUES (%s, %s)"
        cursor.executemany(sql, estudiantes)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar estudiantes en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


def obtener_todas_las_identificaciones():
    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        cursor.execute("SELECT identificacion FROM estudiante")
        return set(row[0] for row in cursor.fetchall())
    except Exception as e:
        print(f"Error al obtener identificaciones: {e}")
        return set()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()

# ============================ CARRERA ============================

def insertar_carreras_en_lote(carreras:list):
    if not carreras:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente_cursor()
        sql = "INSERT IGNORE INTO carrera (nombre_carrera) VALUES (%s)"
        cursor.executemany(sql, [(nombre,) for nombre in carreras])
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar carreras en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


def obtener_todas_las_carreras():
    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        cursor.execute("SELECT nombre_carrera FROM carrera")
        return set(row[0] for row in cursor.fetchall())
    except Exception as e:
        print(f"Error al obtener carreras: {e}")
        return set()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()



# ============================ DOCENTE ============================

def insertar_docentes_en_lote(docentes: list):
    if not docentes:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        sql = "INSERT IGNORE INTO docente (cedula_docente, nombre_docente) VALUES (%s, %s)"
        cursor.executemany(sql, docentes)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar docentes en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


def obtener_todas_las_cedulas_docentes():
    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        cursor.execute("SELECT cedula_docente FROM docente")
        return set(row[0] for row in cursor.fetchall())
    except Exception as e:
        print(f"Error al obtener cédulas de docentes: {e}")
        return set()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


