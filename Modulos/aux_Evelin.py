from db_conexion import obtener_cliente_mysql
import pandas as pd
import plotly.express as px
import streamlit as st


# Filtros
def obtener_datos_demograficos(carrera, periodo):
    cliente = obtener_cliente_mysql()
    sql = """
    SELECT e.genero, e.estado_civil, e.numero_hijos, e.etnia, e.fecha_nacimiento
    FROM estudiante e
    JOIN carrera c ON e.id_carrera = c.id_carrera
    JOIN nota n ON e.id_estudiante = n.id_estudiante
    WHERE c.nombre_carrera = %s AND n.periodo_academico = %s
    """
    df = pd.read_sql(sql, cliente, params=(carrera, periodo))
    cliente.close()
    return df



# SEXO  

def obtener_datos_sexo():
    cliente= obtener_cliente_mysql()
    sql= "select sexo from estudiante where sexo is not null"

    df= pd.read_sql(sql,cliente) 
    cliente.close()

    return df


def grafica_pastel_sexo(df_sexo):
    conteo= df_sexo["sexo"].value_counts().reset_index()
    conteo.columns= ["sexo", "cantidad"]
    fig=px.pie(conteo, names="sexo", values="cantidad", title="Distribucion de sexo")

    return fig


# GENERO

def obtener_datos_genero():
    cliente= obtener_cliente_mysql()
    sql= "select genero from estudiante where genero is not null"

    df= pd.read_sql(sql,cliente) 
    cliente.close()

    return df


def grafica_pastel_genero(df_genero):
    conteo= df_genero["genero"].value_counts().reset_index()
    conteo.columns= ["genero", "cantidad"]
    fig=px.pie(conteo, names="genero", values="cantidad", title="Distribucion de genero")

    return fig




#  ESTADO CIVIL

def obtener_datos_estado_civil():
    cliente= obtener_cliente_mysql()
    sql= "select estado_civil from estudiante where estado_civil is not null"

    df= pd.read_sql(sql,cliente) 
    cliente.close()
    return df

def grafica_estado_civil(df_estado_civil):
    conteo = df_estado_civil["estado_civil"].value_counts().reset_index()
    conteo.columns = ["estado_civil", "cantidad"]
    fig = px.pie(conteo, names="estado_civil", values="cantidad", title="Estado Civil")
    return fig

# NUMERO DE HIJOS  num_hijos

def obtener_datos_numero_hijos():
    cliente= obtener_cliente_mysql()
    sql= "select numero_hijos from estudiante where numero_hijos is not null"

    df= pd.read_sql(sql,cliente) 
    cliente.close()
    return df


def grafica_numero_hijos(df_numero_hijos):
    conteo = df_numero_hijos["numero_hijos"].value_counts().reset_index()
    conteo.columns = ["numero_hijos", "cantidad"]
    fig = px.pie(conteo, names="numero_hijos", values="cantidad", title="Número de Hijos")
    return fig

# ETNIA

def obtener_datos_etnia():
    cliente= obtener_cliente_mysql()
    sql= "select etnia from estudiante where etnia is not null"

    df= pd.read_sql(sql,cliente) 
    cliente.close()
    return df

def grafica_etnia(df_etnia):
    conteo = df_etnia["etnia"].value_counts().reset_index()
    conteo.columns = ["etnia", "cantidad"]
    fig = px.pie(conteo, names="etnia", values="cantidad", title="Distribución por Etnia")
    return fig


# FECHA NACIMIENTO
def obtener_datos_fecha_nacimiento():
    cliente= obtener_cliente_mysql()
    sql= "select fecha_nacimiento from estudiante where fecha_nacimiento is not null"

    df= pd.read_sql(sql,cliente) 
    cliente.close()
    return df


def grafica_fecha_nacimiento(df_fecha_nacimiento):
    df = df_fecha_nacimiento.copy()
    df["anio"] = pd.to_datetime(df["fecha_nacimiento"], errors='coerce').dt.year
    df = df[df["anio"].notna()]
    fig = px.histogram(df, x="anio", nbins=20, title="Distribución por Año de Nacimiento")
    return fig







# Ejecutar en Streamlit REVISAR
carrera = "TECNOLOGIA SUPERIOR EN DESARROLLO DE SOFTWARE"
periodo = "2023-1"

df = obtener_datos_demograficos(carrera, periodo)



if df.empty:
    st.warning("No hay datos para los filtros seleccionados.")
else:
    st.plotly_chart(grafica_genero(df))