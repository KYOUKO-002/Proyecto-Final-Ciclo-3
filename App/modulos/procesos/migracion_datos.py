import pandas as pd

import modulos.db.modelos as modelos
import modulos.db.mysql_crud as crud


def migrar_datos_df(df: pd.DataFrame):
    df_limpio = limpiar_datos(df)
    cargar_estudiantes(df_limpio)


def cargar_estudiantes(df: pd.DataFrame):

    df_estudiantes = df[['Identificacion', 'Estudiante']].drop_duplicates(subset='Identificacion')
    print(f"Total únicos en Excel: {df_estudiantes.shape[0]}")
    identificaciones_existentes = crud.obtener_todas_las_identificaciones()
    df_nuevos = df_estudiantes[~df_estudiantes['Identificacion'].isin(identificaciones_existentes)]
    print(f"Nuevos a insertar: {df_nuevos.shape[0]}")

    lista_para_insertar = [
        (row['Identificacion'], row['Estudiante'])
        for _, row in df_nuevos.iterrows()
    ]
    crud.insertar_estudiantes_en_lote(lista_para_insertar)


def limpiar_datos(df):
    return df




