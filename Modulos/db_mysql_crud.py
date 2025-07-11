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
        print(f"Error al insertar datos de estudiantes: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_estudiantes_colegio(df_colegios):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "nombre_colegio", "tipo_colegio", "titulo_bachiller", "anio_graduacion"
    ]


    sql= f"INSERT IGNORE INTO colegio_graduacion({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_colegios[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de colegios: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()



def crear_propiedades_extra(df_propiedades):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "num_propiedades", "valor_propiedades", "num_vehiculos", "valor_vehiculos"
    ]

    sql= f"INSERT IGNORE INTO propiedades_extra({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_propiedades[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de propiedades: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_economia_estudiante(df_economia):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "total_ingresos", "total_egresos"
    ]

    sql= f"INSERT IGNORE INTO economia_estudiante({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_economia[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de economia: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_contacto_emergencia(df_contacto_emergencia):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "nombre_contacto", "telefono_contacto"
    ]

    sql= f"INSERT IGNORE INTO contacto_emergencia({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_contacto_emergencia[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de contacto emergencia: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_datos_salud(df_datos_salud):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "tipo_sangre", "semanas_embarazo", "porcentaje_discapacidad", "nombre_discapacidad", 
        "nombre_enfermedades", "vacuna_covid", "antecedentes_patologicos_fam"
    ]

    sql= f"INSERT IGNORE INTO datos_salud({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_datos_salud[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de salud: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_familia(df_familia):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "integrantes_familia", "integrantes_aporte_economico", "cabezas_familia"
    ]

    sql= f"INSERT IGNORE INTO familia({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_familia[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de familia: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_vivienda(df_vivienda):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "tipo_vivienda", "condicion_vivienda", "servicios_vivienda"
    ]

    sql= f"INSERT IGNORE INTO vivienda({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_vivienda[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de vivienda: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_carreras(df_carreras):
    cliente = obtener_cliente_mysql()
    cursor = cliente.cursor()
    
    columnas = [
        "id_estudiante", "tipo_vivienda", "condicion_vivienda", "servicios_vivienda"
    ]

    sql= f"INSERT IGNORE INTO vivienda({','.join(columnas)}) VALUES ({','.join(['%s'] * len(columnas))})"
    valores = df_vivienda[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de vivienda: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()
