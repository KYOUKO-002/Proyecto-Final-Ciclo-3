import streamlit as st
import pandas as pd


def vista_migracion_datos():
    archivo = st.file_uploader("Sube un archivo Excel", type=["xls", "xlsx"])

    if archivo is not None:
        try:
            df = pd.read_excel(archivo, skiprows=3)

            st.write("Vista previa del archivo:")
            st.dataframe(df)

        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")