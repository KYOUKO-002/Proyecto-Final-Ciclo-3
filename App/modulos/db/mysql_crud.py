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
