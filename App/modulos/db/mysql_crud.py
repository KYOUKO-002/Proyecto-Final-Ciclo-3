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


# ============================ ASIGNATURA ============================

def insertar_asignaturas_en_lote(asignaturas: list):
    if not asignaturas:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        sql = """
            INSERT IGNORE INTO asignatura (nombre_asignatura, nivel, id_carrera)
            VALUES (%s, %s, %s)
        """
        cursor.executemany(sql, asignaturas)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar asignaturas en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


def obtener_todas_las_asignaturas():
    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        cursor.execute("SELECT nombre_asignatura FROM asignatura")
        return set(row[0] for row in cursor.fetchall())
    except Exception as e:
        print(f"Error al obtener asignaturas: {e}")
        return set()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


# ============================ MATRICULA ============================

def insertar_matriculas_en_lote(matriculas: list):
    if not matriculas:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        sql = """
            INSERT IGNORE INTO matricula (id_estudiante, id_periodo, estado_matricula, tipo_ingreso)
            VALUES (%s, %s, %s, %s)
        """
        cursor.executemany(sql, matriculas)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar matrículas en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


def obtener_todas_las_matriculas():
    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        cursor.execute("SELECT id_estudiante, id_periodo FROM matricula")
        return set((row[0], row[1]) for row in cursor.fetchall())
    except Exception as e:
        print(f"Error al obtener matrículas: {e}")
        return set()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()

    
    # ============================ DETALLE_MATRICULA ============================

    def insertar_detalles_matricula_en_lote(detalles: list):
    if not detalles:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        sql = """
            INSERT IGNORE INTO detalle_matricula (
                id_matricula,
                id_asignatura,
                id_docente,
                asistencia,
                nota_final,
                estado_academico
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(sql, detalles)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar detalle_matricula en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()


# ============================ NOTAS ============================

def insertar_notas_en_lote(notas: list):
    if not notas:
        return

    cliente = cliente_mysql()
    try:
        cursor = cliente.cursor()
        sql = """
            INSERT IGNORE INTO notas (
                asistencia,
                nota_final,
                id_estudiante,
                id_asignatura,
                id_periodo
            )
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.executemany(sql, notas)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar notas en lote: {e}")
        cliente.rollback()
    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()



