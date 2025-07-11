import pandas as pd
import numpy as np
import os
from db_mysql_crud import crear_estudiantes, crear_estudiantes_colegio, crear_propiedades_extra, crear_economia_estudiante
from db_mysql_crud import crear_contacto_emergencia, crear_datos_salud, crear_familia, crear_vivienda
from db_mysql_consultas import obtener_id_ci_estudiante


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def cargar_data(ruta_archivo):
    """
    Carga un archivo Excel y devuelve un DataFrame de pandas.
    """
    return pd.read_excel(ruta_archivo, dtype={"ci_pasaporte": str})
    

def migrar_estudiantes():
    df_estudiantes = cargar_data(os.path.join(BASE_DIR, "data", "fichas_limpias_final.xlsx"))
    df_estudiantes = df_estudiantes[["ci_pasaporte", "correo_tec","nombres", 
                                     "sexo","genero","estado_civil","num_hijos",
                                     "etnia","fecha_nacimiento","tipo_parroqui",
                                     "ciudad","provincia","pais","celular",
                                     "tiene_beca","estudio_otra_carrera",
                                     "ocupacion_estudiante","persona_cubre_gastos",
                                     "recibe_ayuda"]]
    crear_estudiantes(df_estudiantes)
    
def agregar_columnas_extras_ficha():
    df = cargar_data(os.path.join(BASE_DIR, "data", "fichas_limpias_final.xlsx"))

    df["id_estudiante"]=df["ci_pasaporte"].map(obtener_id_ci_estudiante())
    return df

def migrar_colegios():
    df_colegios = agregar_columnas_extras_ficha()
    df_colegios = df_colegios[["id_estudiante", "nombre_colegio", "tipo_colegio","titulo_bachiller","anio_graduacion"]]

    crear_estudiantes_colegio(df_colegios)



def migrar_propiedades_extras():
    df_propiedades = agregar_columnas_extras_ficha()
    df_propiedades = df_propiedades[["id_estudiante", "num_propiedades", "valor_propiedades", "num_vehiculos", "valor_vehiculos"]]                                

    crear_propiedades_extra(df_propiedades)


def migrar_economia():
    df_economia = agregar_columnas_extras_ficha()
    df_economia = df_economia[["id_estudiante", "total_ingresos", "total_egresos"]]                                

    crear_economia_estudiante(df_economia)


def migrar_contacto_emergencia():
    df_contacto_emergencia = agregar_columnas_extras_ficha()
    df_contacto_emergencia = df_contacto_emergencia[["id_estudiante", "nombre_contacto", "telefono_contacto"]]                                

    crear_contacto_emergencia(df_contacto_emergencia)


def migrar_datos_salud():
    df_datos_salud = agregar_columnas_extras_ficha()
    df_datos_salud = df_datos_salud[["id_estudiante", "tipo_sangre", "semanas_embarazo", "porcentaje_discapacidad", "nombre_discapacidad", 
        "nombre_enfermedades", "vacuna_covid", "antecedentes_patologicos_fam"]]

    df_datos_salud = df_datos_salud.replace({np.nan: None})                                

    crear_datos_salud(df_datos_salud)


def migrar_familia():
    df_familia = agregar_columnas_extras_ficha()
    df_familia = df_familia[["id_estudiante", "integrantes_familia", "integrantes_aporte_economico", "cabezas_familia"]]

    df_familia = df_familia.replace({np.nan: None})

    crear_familia(df_familia)


def migrar_familia():
    df_familia = agregar_columnas_extras_ficha()
    df_familia = df_familia[["id_estudiante", "integrantes_familia", "integrantes_aporte_economico", "cabezas_familia"]]

    df_familia = df_familia.replace({np.nan: None})

    crear_familia(df_familia)


def migrar_vivienda():
    df_vivienda = agregar_columnas_extras_ficha()
    df_vivienda = df_vivienda[["id_estudiante", "tipo_vivienda", "condicion_vivienda", "servicios_vivienda"]]

    df_vivienda = df_vivienda.replace({np.nan: None})

    crear_vivienda(df_vivienda)


migrar_vivienda()