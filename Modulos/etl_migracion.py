import pandas as pd
import numpy as np
import os
from db_mysql_crud import crear_estudiantes, crear_estudiantes_colegio, crear_propiedades_extra, crear_economia_estudiante
from db_mysql_crud import crear_contacto_emergencia, crear_datos_salud, crear_familia, crear_vivienda, crear_carreras
from db_mysql_crud import crear_estudiantes_carreras, crear_asignaturas, crear_estudiantes_asignaturas 
from db_mysql_consultas import obtener_id_ci_estudiante, obtener_id_codigo_carrera, obtener_id_nombre_asignaturas, obtener_id_por_columnas_aux_estudiante_carrera 


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
    df_estudiantes = df_estudiantes.replace({np.nan: None})
    crear_estudiantes(df_estudiantes)
    
def agregar_columnas_extras_ficha():
    df = cargar_data(os.path.join(BASE_DIR, "data", "fichas_limpias_final.xlsx"))

    df["id_estudiante"]=df["ci_pasaporte"].map(obtener_id_ci_estudiante())
    return df

def migrar_colegios():
    df_colegios = agregar_columnas_extras_ficha()
    df_colegios = df_colegios[["id_estudiante", "nombre_colegio", "tipo_colegio","titulo_bachiller","anio_graduacion"]]
    df_colegios = df_colegios.replace({np.nan: None})
    crear_estudiantes_colegio(df_colegios)



def migrar_propiedades_extras():
    df_propiedades = agregar_columnas_extras_ficha()
    df_propiedades = df_propiedades[["id_estudiante", "num_propiedades", "valor_propiedades", "num_vehiculos", "valor_vehiculos"]]                                
    df_propiedades = df_propiedades.replace({np.nan: None})
    crear_propiedades_extra(df_propiedades)


def migrar_economia():
    df_economia = agregar_columnas_extras_ficha()
    df_economia = df_economia[["id_estudiante", "total_ingresos", "total_egresos"]]                                
    df_economia = df_economia.replace({np.nan: None})
    crear_economia_estudiante(df_economia)


def migrar_contacto_emergencia():
    df_contacto_emergencia = agregar_columnas_extras_ficha()
    df_contacto_emergencia = df_contacto_emergencia[["id_estudiante", "nombre_contacto", "telefono_contacto"]]                                
    df_contacto_emergencia = df_contacto_emergencia.replace({np.nan: None})
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


def migrar_carreras():
    df_carreras = cargar_data(os.path.join(BASE_DIR, "data", "notas_limpias_final.xlsx"))
    df_carreras = df_carreras[["codigo_carrera", "nombre_carrera"]]
    df_carreras = df_carreras.replace({np.nan: None})
    crear_carreras(df_carreras)


def agregar_columnas_extras_nota():
    df = cargar_data(os.path.join(BASE_DIR, "data", "notas_limpias_final.xlsx"))

    df["id_estudiante"]=df["ci_pasaporte"].map(obtener_id_ci_estudiante())
    df["id_carrera"]=df["codigo_carrera"].map(obtener_id_codigo_carrera())
    
    return df


def migrar_estudiantes_carreras():
    df_estudiantes_carreras = agregar_columnas_extras_nota()

    df_estudiantes_carreras = df_estudiantes_carreras[[
        "id_carrera", "id_estudiante", "ciclo_carrera", 
        "periodo_academico", "paralelo"
    ]]

    df_estudiantes_carreras = df_estudiantes_carreras.drop_duplicates(
        subset=["id_carrera", "id_estudiante", "periodo_academico"]
    )

    
    df_estudiantes_carreras = df_estudiantes_carreras.replace({np.nan: None})

    crear_estudiantes_carreras(df_estudiantes_carreras)
    

def migrar_asignaturas():
    df_asignaturas = agregar_columnas_extras_nota()

    df_asignaturas = df_asignaturas[[
        "id_carrera", "nombre_asignatura"
    ]]

    df_asignaturas = df_asignaturas.replace({np.nan: None})

    crear_asignaturas(df_asignaturas)



def migrar_estudiante_asignatura():
    df_estudiante_asignatura = agregar_columnas_extras_nota()

    df_estudiante_asignatura = df_estudiante_asignatura[[
        "id_carrera", "id_estudiante", "periodo_academico", "nombre_asignatura",
        "numero_matricula", "porcentaje_asistencia",
        "nota_final", "estado_estudiante", "estado_matricula", "tipo_ingreso"
    ]]

    df_estudiante_asignatura["id_carrera"]= df_estudiante_asignatura["id_carrera"].fillna("0").astype(int)
    df_estudiante_asignatura["id_estudiante"]= df_estudiante_asignatura["id_estudiante"].fillna("0").astype(int)


    df_estudiante_asignatura["aux_estudiante_carrera"] = (
        df_estudiante_asignatura["id_carrera"].astype(str) + "-" +
        df_estudiante_asignatura["id_estudiante"].astype(str) + "-" +
        df_estudiante_asignatura["periodo_academico"].astype(str)
    )

    
    df_estudiante_asignatura["id_asignatura"] = df_estudiante_asignatura["nombre_asignatura"].map(obtener_id_nombre_asignaturas())

    df_estudiante_asignatura["id_estudiante_carrera"] = df_estudiante_asignatura["aux_estudiante_carrera"].map(obtener_id_por_columnas_aux_estudiante_carrera())

    df_estudiante_asignatura["id_estudiante_carrera"] = df_estudiante_asignatura["id_estudiante_carrera"].fillna("0").astype(int)

    df_estudiante_asignatura = df_estudiante_asignatura.drop(
        columns=["id_carrera", "id_estudiante", "periodo_academico", "nombre_asignatura"]
    )

    df_estudiante_asignatura = df_estudiante_asignatura.replace({np.nan: None})
    crear_estudiantes_asignaturas(df_estudiante_asignatura)

migrar_estudiante_asignatura()

