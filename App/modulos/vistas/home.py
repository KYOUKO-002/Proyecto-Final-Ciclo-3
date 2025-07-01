from PIL import Image
import streamlit as st

def vista_home():
    imagen = Image.open("./././img/logo_tec.png")
    col1, col2, col3 = st.columns([1, 15, 1])

    with col2:
        st.image(imagen, use_container_width=True)
        st.title('Proyecto final ciclo 3: Redimiento Académico')
        st.subheader('Por: Evelyn Criollo, Anthony Rosillo, Justin Escalante y Eduardo Mendieta')