import streamlit as st
import pandas as pd

from modulos.procesos.migracion_datos import migrar_datos_df

def vista_migracion_datos():
    archivo = st.file_uploader("Sube un archivo Excel", type=["xls", "xlsx"])

    if archivo is not None:
        try:
            df = pd.read_excel(archivo, skiprows=3)
            df = df[['Periodo', 'Paralelo', 'Identificacion', 'Estudiante', 'Carrera', 'Nivel', 'Asignatura', 
                     'Num_matricula', 'Asistencia', 'Nota final', 'Estado', 'Estado Matrícula', 'Tipo Ingreso', 
                     'Cédula docente', 'Nombre docente']]
            
            migrar = st.button('Cargar Datos')

            st.write("Vista previa del archivo:")
            st.dataframe(df)

            if migrar:
                migrar_datos_df(df)
                st.success('Datos migrados con éxito!')

        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")