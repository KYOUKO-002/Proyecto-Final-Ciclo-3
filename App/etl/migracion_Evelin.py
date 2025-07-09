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

def migrar_colegios(df_colegios):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO colegio_graduacion (
        id_estudiante,
        nombre_colegio,
        tipo_colegio,
        titulo_bachiller,
        anio_graduacion
    
            
        ) VALUES (
            %s, %s, %s, %s, %s
        )
    """

    valores = list(df_colegios.itertuples(index=False, name=None))

    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla colegio.")

    cursor.close()
    cliente.close()

def main():
    df_fichas, df_notas = cargar_data()

    # MIGRACIÓN DE COLEGIOS ---------------------------
    df_colegios= df_fichas [[ 'ci_pasaporte', 'colegio','tipo_colegio', 'titulo_bachiller','anio_graduacion'  ]]
    df_colegios =  df_colegios.rename(columns={"colegio":"nombre_colegio"} )

    try:
        cliente = cliente_mysql()

        # Estas 4 lineas ya no se repiten
        query_estudiante = "SELECT id_estudiante, ci_pasaporte FROM estudiante"
        df_estudiante = pd.read_sql(query_estudiante, cliente)
        df_estudiante['ci_pasaporte'] = df_estudiante['ci_pasaporte'].astype(str).str.strip()

        dic_id_estudiante = df_estudiante.set_index('ci_pasaporte')['id_estudiante'].to_dict()


    

        df_colegios['id_estudiante'] = df_colegios['ci_pasaporte'].map(dic_id_estudiante)

        

        df_colegios = df_estudiantes_carreras.drop(columns=['ci_pasaporte'])
        migrar_colegios(df_colegios)


    finally:
        cliente.close()

    

    

    
    
main()