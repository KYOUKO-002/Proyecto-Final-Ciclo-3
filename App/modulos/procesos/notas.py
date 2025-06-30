import pandas as pd

import modulos.db.modelos as modelos
import modulos.db.mysql_crud as crud


def cargar_excel_notas():
    ruta = '/home/eduardo/Documentos/GH/justinGH/Proyecto-Final-Ciclo-3/Documentacion/Data/DataOriginal/MAESTRO DE NOTAS-2020-2P.xlsx'
    df = pd.read_excel(ruta, skiprows=3)
    print(df.columns.tolist())


def cargar_estudiantes():
    estudiante = modelos.Estudiante(nombres='Pepito Prado')
    crud.crear_estudiante(estudiante)



