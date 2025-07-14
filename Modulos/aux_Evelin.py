from db_conexion import obtener_cliente_mysql
import pandas as pd
import plotly.express as px
import streamlit as st

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





df_genero= obtener_datos_genero()
st.plotly_chart(grafica_pastel_genero(df_genero)) 