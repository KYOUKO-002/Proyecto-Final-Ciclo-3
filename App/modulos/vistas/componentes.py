import streamlit as st

import modulos.vistas.home as vista_home

def configurar_pagina():
    st.set_page_config(
        page_title="Rendimiento Académico PFC3",
        page_icon="./img/icono_app.png",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def menu_principal():
    st.sidebar.markdown("## **Menú**")

    if 'pagina' not in st.session_state:
        st.session_state['pagina'] = "🏠 Home"

    if st.sidebar.button("🏠 **Home**"):
        st.session_state['pagina'] = "🏠 Home"

    if st.sidebar.button("📂 **Cargar Datos**"):
        st.session_state['pagina'] = "📂 Cargar Datos"

    if st.sidebar.button("📊 **Estadísticas**"):
        st.session_state['pagina'] = "📊 Estadísticas"

    if st.sidebar.button("🧠 **Entrenar Modelos**"):
        st.session_state['pagina'] = "🧠 Entrenar Modelos"
        
    if st.sidebar.button("🔮 **Predicciones**"):
        st.session_state['pagina'] = "🔮 Predicciones"

    return st.session_state['pagina']


def actualizar_pagina(pagina):
    if pagina == "🏠 Home":
        vista_home.cargar_contenido()

    elif pagina == "📂 Cargar Datos":
        st.write("Aquí puedes cargar tus archivos CSV.")

    elif pagina == "📊 Estadísticas":
        st.write("Estadísticas descriptivas de los datos.")

    elif pagina == "🧠 Entrenar Modelos":
        st.write("Entrenamiento de modelos de Machine Learning.")

    elif pagina == "🔮 Predicciones":
        st.write("Realiza predicciones con tus modelos entrenados.")
        
    else:
        st.write("¡Página no encontrada!")