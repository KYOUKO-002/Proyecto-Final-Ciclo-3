import pandas as pd
import os
from db_mysql_crud import crear_estudiantes


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
    
def agregar_columnas_extras(ruta_archivo):
    df = cargar_data(ruta_archivo)
    
    pass

def migrar_colegios():
    df_colegios = cargar_data(os.path.join(BASE_DIR, "data", "fichas_limpias_final.xlsx"))
    df_colegios = df_colegios[["", "colegio", "anio_graduacion"]]
    
    # Aquí se llamaría a la función para crear colegios, similar a crear_estudiantes
    # crear_colegios(df_colegios)  # Esta función debe ser implementada   
                                     


