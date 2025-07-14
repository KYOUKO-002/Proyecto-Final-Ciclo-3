from db_conexion import obtener_cliente_mysql
import pandas as pd
import plotly.express as px
import streamlit as st

# grafica tiene_beca
def obtener_datos_beca(carrera=None, periodo_academico=None):
    cliente = obtener_cliente_mysql()
    
    sql = """
    SELECT e.tiene_beca, c.nombre_carrera, ec.periodo_academico
    FROM estudiante e
    JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
    JOIN carrera c ON ec.id_carrera = c.id_carrera
    WHERE e.tiene_beca IS NOT NULL
    """
    
    filtros = []
    if carrera and carrera != "Todas":
        filtros.append(f"c.nombre_carrera = '{carrera}'")
    if periodo_academico and periodo_academico != "Todos":
        filtros.append(f"ec.periodo_academico = '{periodo_academico}'")
    
    if filtros:
        sql += " AND " + " AND ".join(filtros)
    
    df = pd.read_sql(sql, cliente)
    cliente.close()
    return df

# Función para crear la gráfica de pastel
def grafica_pastel_beca(df):
    conteo = df["tiene_beca"].value_counts().reset_index()
    conteo.columns = ["tiene_beca", "cantidad"]
    # Para que sea más claro, cambiar 0 y 1 a No y Sí
    conteo["tiene_beca"] = conteo["tiene_beca"].map({0: "No", 1: "Sí"})
    
    fig = px.pie(conteo, names="tiene_beca", values="cantidad")
    return fig

# --- Streamlit UI ---
st.title("Análisis de rendimiento académico ")
st.subheader("Distribución de estudiantes con beca")
# Primero, obtener opciones únicas para carrera y periodo
cliente = obtener_cliente_mysql()
carreras_df = pd.read_sql("SELECT DISTINCT nombre_carrera FROM carrera", cliente)
periodos_df = pd.read_sql("SELECT DISTINCT periodo_academico FROM estudiante_carrera", cliente)
cliente.close()

carreras = ["Todas"] + sorted(carreras_df["nombre_carrera"].dropna().tolist())
periodos = ["Todos"] + sorted(periodos_df["periodo_academico"].dropna().tolist())

# Widgets de selección
carrera_seleccionada = st.selectbox("Selecciona carrera", carreras)
periodo_seleccionado = st.selectbox("Selecciona periodo académico", periodos)

# Obtener datos con filtros
df_beca = obtener_datos_beca(carrera=carrera_seleccionada, periodo_academico=periodo_seleccionado)

# Mostrar gráfica si hay datos
if not df_beca.empty:
    fig = grafica_pastel_beca(df_beca)
    st.plotly_chart(fig, key="grafica_beca")  # usa un key para evitar duplicados
else:
    st.warning("No hay datos para la combinación seleccionada.")





# Aquí se obtiene el DataFrame con filtros seleccionados
#df_beca = obtener_datos_beca()

# Mostrar la gráfica
#st.plotly_chart(grafica_pastel_beca(df_beca))
#---------------------------------grafica - recibe_ayuda

def obtener_datos_ayuda(carrera=None, periodo_academico=None):
    cliente = obtener_cliente_mysql()
    
    sql = """
    SELECT e.recibe_ayuda, c.nombre_carrera, ec.periodo_academico
    FROM estudiante e
    JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
    JOIN carrera c ON ec.id_carrera = c.id_carrera
    WHERE e.recibe_ayuda IS NOT NULL
    """
    
    filtros = []
    if carrera and carrera != "Todas":
        filtros.append(f"c.nombre_carrera = '{carrera}'")
    if periodo_academico and periodo_academico != "Todos":
        filtros.append(f"ec.periodo_academico = '{periodo_academico}'")
    
    if filtros:
        sql += " AND " + " AND ".join(filtros)
    
    df = pd.read_sql(sql, cliente)
    cliente.close()
    return df



def grafica_pastel_ayuda(df):
    conteo = df["recibe_ayuda"].value_counts().reset_index()
    conteo.columns = ["recibe_ayuda", "cantidad"]
    conteo["recibe_ayuda"] = conteo["recibe_ayuda"].map({0: "No", 1: "Sí"})
    
    fig = px.pie(conteo, names="recibe_ayuda", values="cantidad")
    return fig


st.subheader("Distribución de estudiantes que reciben ayuda")
df_ayuda = obtener_datos_ayuda(carrera=carrera_seleccionada, periodo_academico=periodo_seleccionado)

if not df_ayuda.empty:
    fig = grafica_pastel_ayuda(df_ayuda)
    st.plotly_chart(fig, key="grafica_ayuda")
else:
    st.warning("No hay datos para la combinación seleccionada.")

#df_ayuda = obtener_datos_ayuda()
#st.plotly_chart(grafica_pastel_ayuda(df_ayuda))


#---------------------------------grafica -estudio_otra_carrera

def obtener_datos_otra_carrera(carrera=None, periodo_academico=None): 
    cliente = obtener_cliente_mysql()
    
    sql = """
    SELECT e.estudio_otra_carrera, c.nombre_carrera, ec.periodo_academico
    FROM estudiante e
    JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
    JOIN carrera c ON ec.id_carrera = c.id_carrera
    WHERE e.estudio_otra_carrera IS NOT NULL
    """
    
    filtros = []
    if carrera and carrera != "Todas":
        filtros.append(f"c.nombre_carrera = '{carrera}'")
    if periodo_academico and periodo_academico != "Todos":
        filtros.append(f"ec.periodo_academico = '{periodo_academico}'")
    
    if filtros:
        sql += " AND " + " AND ".join(filtros)
    
    df = pd.read_sql(sql, cliente)
    cliente.close()
    return df


def grafica_pastel_otra_carrera(df):
    conteo = df["estudio_otra_carrera"].value_counts().reset_index()
    conteo.columns = ["estudio_otra_carrera", "cantidad"]
    conteo["estudio_otra_carrera"] = conteo["estudio_otra_carrera"].map({0: "No", 1: "Sí"})
    
    colores = {"No": "sky blue", "Sí": "green"}  # Colores personalizados
    
    fig = px.pie(
        conteo, 
        names="estudio_otra_carrera", 
        values="cantidad",
        color="estudio_otra_carrera",
        color_discrete_map=colores
    )
    return fig


st.subheader("Distribución de estudiantes que estudian otra carrera")
df_otra_carrera = obtener_datos_otra_carrera(carrera=carrera_seleccionada, periodo_academico=periodo_seleccionado)

if not df_otra_carrera.empty:
    fig = grafica_pastel_otra_carrera(df_otra_carrera)
    st.plotly_chart(fig, key="grafica_otra_carrera")
else:
    st.warning("No hay datos para la combinación seleccionada.")




#df_otra_carrera = obtener_otra_carrera_por_periodo()
#st.plotly_chart(grafica_barras_otra_carrera_por_periodo(df_otra_carrera))

