import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from App.modulos.db_conexion import cliente_mysql

def cargar_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'fichas_limpias.xlsx')
    df_fichas = pd.read_excel(data_path)

    data_path = os.path.join(base_dir, 'data', 'notas_limpias.xlsx')
    df_notas = pd.read_excel(data_path, dtype={'ci_estudiante': str})

    return df_fichas, df_notas


def migrar_estudiantes(df_estudiantes):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO estudiante (
            ci_pasaporte, correo_tec, nombres, sexo, genero,
            estado_civil, num_hijos, etnia, fecha_nacimiento,
            tipo_parroquia, ciudad, provincia, pais, celular,
            tiene_beca, estudio_otra_carrera, ocupacion_estudiante,
            persona_cubre_gastos, recibe_ayuda
        ) VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s,
            %s, %s
        )
    """

    valores = list(df_estudiantes.itertuples(index=False, name=None))

    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla estudiante.")

    cursor.close()
    cliente.close()


def migrar_carreras(df_carreras):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = "INSERT IGNORE INTO carrera (nombre_carrera) VALUES (%s)"

    valores = list(df_carreras.itertuples(index=False, name=None))

    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla carrera.")

    cursor.close()
    cliente.close()


def migrar_estudiantes_carreras(df_estudiantes_carreras):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO estudiante_carrera (
            id_carrera,
            id_estudiante,
            ciclo_carrera,
            razon_eleccion_carrera,
            razon_eleccion_instituto,
            periodo_academico,
            paralelo
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    datos = [
        (
            int(row['id_carrera']),
            int(row['id_estudiante']),
            str(row['ciclo_carrera']),
            str(row['razon_eleccion_carrera']),
            str(row['razon_eleccion_instituto']),
            str(row['periodo_academico']),
            str(row['paralelo'])
        )
        for _, row in df_estudiantes_carreras.iterrows()
    ]

    cursor.executemany(sql, datos)
    cliente.commit()
    print(f"{cursor.rowcount} registros insertados (ignorando duplicados).")

    cursor.close()
    cliente.close()


def preprocesar_df_estudiantes_carreras(df_fichas, df_notas):
    df_estudiantes_carreras = df_fichas[['nombre_carrera', 'ci_pasaporte', 'ciclo_carrera', 
                                         'razon_eleccion_instituto', 'razon_eleccion_carrera', 
                                         'periodo_academico']].copy()

    df_estudiantes_carreras['ci_pasaporte'] = df_estudiantes_carreras['ci_pasaporte'].astype(str).str.strip()
    df_estudiantes_carreras['nombre_carrera'] = df_estudiantes_carreras['nombre_carrera'].astype(str).str.strip().str.upper()

    df_notas['ci_estudiante'] = df_notas['ci_estudiante'].astype(str).str.strip()
    df_notas['clave'] = df_notas['ci_estudiante'] + '_' + df_notas['periodo_academico'].astype(str)
    df_estudiantes_carreras['clave'] = df_estudiantes_carreras['ci_pasaporte'] + '_' + df_estudiantes_carreras['periodo_academico'].astype(str)

    dic_paralelo = df_notas.drop_duplicates(subset='clave').set_index('clave')['paralelo'].to_dict()
    df_estudiantes_carreras['paralelo'] = df_estudiantes_carreras['clave'].map(dic_paralelo).fillna('DESCONOCIDO')
    df_estudiantes_carreras = df_estudiantes_carreras.drop(columns=['clave'])

    try:
        cliente = cliente_mysql()

        query_estudiante = "SELECT id_estudiante, ci_pasaporte FROM estudiante"
        df_estudiante = pd.read_sql(query_estudiante, cliente)
        df_estudiante['ci_pasaporte'] = df_estudiante['ci_pasaporte'].astype(str).str.strip()

        dic_id_estudiante = df_estudiante.set_index('ci_pasaporte')['id_estudiante'].to_dict()
        df_estudiantes_carreras['id_estudiante'] = df_estudiantes_carreras['ci_pasaporte'].map(dic_id_estudiante)

        query_carrera = "SELECT id_carrera, nombre_carrera FROM carrera"
        df_carrera = pd.read_sql(query_carrera, cliente)
        df_carrera['nombre_carrera'] = df_carrera['nombre_carrera'].astype(str).str.strip().str.upper()

        dic_id_carrera = df_carrera.set_index('nombre_carrera')['id_carrera'].to_dict()
        df_estudiantes_carreras['id_carrera'] = df_estudiantes_carreras['nombre_carrera'].map(dic_id_carrera)

        df_estudiantes_carreras = df_estudiantes_carreras.drop(columns=['ci_pasaporte', 'nombre_carrera'])

        print("Registros sin id_estudiante:", df_estudiantes_carreras['id_estudiante'].isna().sum())
        print("Registros sin id_carrera:", df_estudiantes_carreras['id_carrera'].isna().sum())

        df_estudiantes_carreras = df_estudiantes_carreras.dropna(subset=['id_estudiante', 'id_carrera'])
        df_estudiantes_carreras['id_estudiante'] = df_estudiantes_carreras['id_estudiante'].astype(int)
        df_estudiantes_carreras['id_carrera'] = df_estudiantes_carreras['id_carrera'].astype(int)

    finally:
        cliente.close()

    return df_estudiantes_carreras


def main():
    df_fichas, df_notas = cargar_data()

    # MIGRACIÓN DE ESTUDIANTES ------------------------------------
    """df_estudiantes = df_fichas[['ci_pasaporte', 'correo_tec', 'nombres', 'sexo','genero','estado_civil','num_hijos',
                         'etnia','fecha_nacimiento','tipo_parroquia', 'ciudad','prov','pais','celular', 'tiene_beca',
                         'estudio_otra_carrera', 'ocupacion_estudiante', 'persona_cubre_gastos', 'recibe_ayuda']]
    df_estudiantes.rename(columns={'prov': 'provincia'}, inplace=True)
    migrar_estudiantes(df_estudiantes)

    # MIGRACIÓN DE CARRERAS ---------------------------------------
    df_carreras = df_fichas[['nombre_carrera']]
    migrar_carreras(df_carreras)

    # MIGRACIÓN DE ESTUDIANTES_CARRERAS ---------------------------
    df_estudiantes_carreras = preprocesar_df_estudiantes_carreras(df_fichas, df_notas)
    migrar_estudiantes_carreras(df_estudiantes_carreras)"""

    # MIGRACIÓN DE ESTUDIANTES_CARRERAS ---------------------------
    

    
    
main()