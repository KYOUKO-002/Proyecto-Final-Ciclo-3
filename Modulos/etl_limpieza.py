import pandas as pd
import numpy as np
import os


base_path = "data"

def limpiar_notas():
    df_notas_20231p = pd.read_excel(os.path.join(base_path, "NOTAS_2023_1P.xlsx"), dtype={"ci_pasaporte": str})
    df_notas_20232p = pd.read_excel(os.path.join(base_path, "NOTAS_2023_2P.xlsx"), dtype={"ci_pasaporte": str})
    df_notas_20241p = pd.read_excel(os.path.join(base_path, "NOTAS_2024_1P.xlsx"), dtype={"ci_pasaporte": str})
    df_notas_20242p = pd.read_excel(os.path.join(base_path, "NOTAS_2024_2P.xlsx"), dtype={"ci_pasaporte": str})

    df_notas = pd.concat([df_notas_20231p, df_notas_20232p, df_notas_20241p, df_notas_20242p],
                        ignore_index=True)

    df_notas["ci_pasaporte"] = df_notas["ci_pasaporte"].str.zfill(10)

    split_columnas = df_notas["carrera"].str.split("-", n=-1)
    df_notas["nombre_carrera"] = split_columnas.str[-1]
    df_notas["codigo_carrera"] = split_columnas.str[:-1].str.join("-")

    columnas_str = df_notas.select_dtypes(include=["object", "string"]).columns
    for col in columnas_str:
        df_notas[col] = df_notas[col].fillna("DESCONOCIDO")
        df_notas[col] = df_notas[col].str.strip()
        df_notas[col] = df_notas[col].str.upper()

    columnas_num = df_notas.select_dtypes(include=["number"]).columns
    df_notas[columnas_num] = df_notas[columnas_num].fillna(0)

    df_notas.rename(columns={"asignatura": "nombre_asignatura"}, inplace=True)
    df_notas.drop(columns=["carrera"], inplace=True)

    df_notas.to_excel(os.path.join(base_path, "notas_limpias_final.xlsx"), index=False)


def limpiar_fichas():
    pass

