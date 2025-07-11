from db_conexion import obtener_cliente_mysql

def crear_estudiantes(df_estudiantes):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "ci_pasaporte", "correo_tec", "nombres", "sexo", "genero", "estado_civil",
        "num_hijos", "etnia", "fecha_nacimiento", "tipo_parroqui", "ciudad",
        "provincia", "pais", "celular", "tiene_beca", "estudio_otra_carrera",
        "ocupacion_estudiante", "persona_cubre_gastos", "recibe_ayuda"
    ]

    sql= f"INSERT IGNORE INTO estudiante({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_estudiantes[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de clientes: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()