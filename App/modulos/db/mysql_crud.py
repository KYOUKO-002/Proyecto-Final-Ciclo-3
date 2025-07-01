from modulos.db.conexion import cliente_mysql
from modulos.db.modelos import Estudiante

# ============================ ESTUDIANTE ============================
def crear_estudiante(estudiante: Estudiante):
    cliente = cliente_mysql()
    
    try:
        cursor = cliente.cursor()
        sql = "INSERT INTO estudiante (identificacion, nombres_estudiante) VALUES (%s, %s)"
        cursor.execute(sql, (estudiante.identificacion, estudiante.nombres))
        cliente.commit()

        estudiante.id = cursor.lastrowid
        return estudiante

    except Exception as e:
        print(f"Error al crear el estudiante: {e}")
        cliente.rollback()
        return None

    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()



def existe_estudiante_por_identificacion(identificacion):
    cliente = cliente_mysql()
    
    try:
        
        cursor = cliente.cursor()
        sql = "SELECT 1 FROM estudiante WHERE identificacion = %s LIMIT 1"
        cursor.execute(sql, (identificacion,))
        resultado = cursor.fetchone()
        return resultado is not None

    except Exception as e:
        print(f"Error al verificar existencia del estudiante: {e}")
        return False

    finally:
        if 'cursor' in locals(): cursor.close()
        if cliente: cliente.close()
