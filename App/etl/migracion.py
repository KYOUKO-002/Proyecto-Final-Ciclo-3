import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from App.modulos.db_conexion import cliente_mysql

def cargar_data(nombre_archivo):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    if nombre_archivo == 'fichas_limpias.xlsx':
        data_path = os.path.join(base_dir, 'data', 'fichas_limpias.xlsx')
        df = pd.read_excel(data_path)

    else:
        data_path = os.path.join(base_dir, 'data', 'notas_limpias.xlsx')
        df = pd.read_excel(data_path, dtype={'ci_estudiante': str})
        df.rename(columns={'carrera': 'nombres_estudiantes', 'estudiante': 'nombre_carrera'}, inplace=True)

    return df


