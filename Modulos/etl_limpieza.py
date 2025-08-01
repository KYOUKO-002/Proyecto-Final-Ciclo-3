import pandas as pd
import numpy as np
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
base_path = os.path.join(BASE_DIR, "data")

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
    df_fichas_20231p = pd.read_excel(os.path.join(BASE_DIR, "data", "Fichas_2023_1P.xlsx"), dtype={"ci_pasaporte": str})
    df_fichas_20232p = pd.read_excel(os.path.join(BASE_DIR, "data", "Fichas_2023_2P.xlsx"), dtype={"ci_pasaporte": str})
    df_fichas_20241p = pd.read_excel(os.path.join(BASE_DIR, "data", "Fichas_2024_1P.xlsx"), dtype={"ci_pasaporte": str})
    df_fichas_20242p = pd.read_excel(os.path.join(BASE_DIR, "data", "Fichas_2024_2P.xlsx"), dtype={"ci_pasaporte": str})
    df_fichas_20251p = pd.read_excel(os.path.join(BASE_DIR, "data", "Fichas_2025_1P.xlsx"), dtype={"ci_pasaporte": str})

    df_fichas = pd.concat([df_fichas_20231p, df_fichas_20232p, df_fichas_20241p, df_fichas_20242p, df_fichas_20251p],
                        ignore_index=True)
    df_fichas["ci_pasaporte"] = df_fichas["ci_pasaporte"].str.zfill(10)
    df_fichas = df_fichas.astype(str)
    
    for col in df_fichas.columns:
        if col != "correo_tec":
            df_fichas[col] = df_fichas[col].str.strip().str.upper()
            df_fichas[col] = df_fichas[col].replace(".", "", regex=False)
            df_fichas[col] = df_fichas[col].fillna("DESCONOCIDO")

 
    df_fichas["nombres"] = (df_fichas["PrimerNombre"] + " " +
        df_fichas["SegunNombre"] + " " +
        df_fichas["PrimerApellido"] + " " +
        df_fichas["SegunApellido"]
    )
                
    df_fichas = df_fichas.drop(columns=["PrimerNombre", "SegunNombre", "PrimerApellido", "SegunApellido"])
    
    columnas_enteras = ["num_hijos", "anio_graduacion", "num_propiedades", "num_vehiculos", "semanas_embarazo"]
    columnnas_flotantes =["valor_propiedades", "valor_vehiculos", "total_ingresos", "total_egresos", "porcentaje_discapacidad"]
    columnas_booleanas = ["tiene_beca","estudio_otra_carrera","recibe_ayuda","tiene_carnet_conadis"]

    for col in columnas_enteras:
        df_fichas[col] = df_fichas[col].str.replace(r"[^0-9]", "", regex=True).replace("",np.nan).fillna(0).astype(int)

    for col in columnnas_flotantes:
        df_fichas[col] = df_fichas[col].str.replace(r"[^0-9]", "", regex=True).replace("",np.nan).fillna(0).astype(float)

    for col in columnas_booleanas:
        df_fichas[col] = df_fichas[col] == "SÍ"

    columnas_str = df_fichas.select_dtypes(include=["string", "object"]).columns
    df_fichas[columnas_str] = df_fichas[columnas_str].fillna("DESCONOCIDO")
    
    columnas_num = df_fichas.select_dtypes(include=["number"]).columns
    df_fichas[columnas_num] = df_fichas[columnas_num].fillna(0)
    
    print(df_fichas.isnull().sum().sort_values(ascending=False))

    df_fichas[columnas_str] = df_fichas[columnas_str].replace(
        to_replace=r"^\s*(nan|NaN|NAN)\s*$",
        value="DESCONOCIDO",
        regex=True
    )

    df_fichas.to_excel(os.path.join(BASE_DIR, "data", "fichas_limpias_final.xlsx"), index=False)



limpiar_fichas()
#limpiar_notas()    