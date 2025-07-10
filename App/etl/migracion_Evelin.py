import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from App.modulos.db_conexion import cliente_mysql

def cargar_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'fichas_limpias.xlsx')
    df_fichas = pd.read_excel(data_path)

    data_path = os.path.join(base_dir, 'data', 'notas_limpias.xlsx')
    df_notas = pd.read_excel(data_path, dtype={'ci_estudiante': str})

    return df_fichas, df_notas

def migrar_colegios(df_colegios):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO colegio_graduacion (
        id_estudiante,
        nombre_colegio,
        tipo_colegio,
        titulo_bachiller,
        anio_graduacion 
        ) VALUES (
            %s, %s, %s, %s, %s
        )
    """

    valores = list(df_colegios.itertuples(index=False, name=None))

    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla colegio.")

    cursor.close()
    cliente.close()

def main():
    df_fichas, df_notas = cargar_data()

    # MIGRACIÓN DE COLEGIOS ---------------------------
    df_colegios= df_fichas [[ 'ci_pasaporte', 'colegio','tipo_colegio', 'titulo_bachiller','anio_graduacion'  ]]
    df_colegios =  df_colegios.rename(columns={"colegio":"nombre_colegio"} )

    try:
        cliente = cliente_mysql()

        # Estas 4 lineas ya no se repiten
        query_estudiante = "SELECT id_estudiante, ci_pasaporte FROM estudiante"
        df_estudiante = pd.read_sql(query_estudiante, cliente)
        df_estudiante['ci_pasaporte'] = df_estudiante['ci_pasaporte'].astype(str).str.strip()

        dic_id_estudiante = df_estudiante.set_index('ci_pasaporte')['id_estudiante'].to_dict()


    

        df_colegios['id_estudiante'] = df_colegios['ci_pasaporte'].map(dic_id_estudiante)

        

        df_colegios = df_colegios.drop(columns=['ci_pasaporte'])
        df_colegios = df_colegios.dropna(subset=['id_estudiante'])
        df_colegios.id_estudiante = df_colegios.id_estudiante.astype(int)
        print(df_colegios.sample(5))
        print(df_colegios.shape)
        migrar_colegios(df_colegios)


    finally:
        cliente.close()

main()


# Migración de Propiedades Extra
def preparar_y_migrar_propiedades_extra(df_fichas, dic_id_estudiante):
    df_propiedades = df_fichas[[ 
        'ci_pasaporte',
        'num_propiedades',
        'valor_propiedades',
        'num_vehiculos',
        'valor_vehiculos'
    ]]

    try:
        cliente = cliente_mysql()
        df_propiedades['id_estudiante'] = df_propiedades['ci_pasaporte'].map(dic_id_estudiante)
        df_propiedades = df_propiedades.drop(columns=['ci_pasaporte'])
        df_propiedades = df_propiedades.dropna(subset=['id_estudiante'])
        df_propiedades.id_estudiante = df_propiedades.id_estudiante.astype(int)

        print(df_propiedades.sample(5))
        print(df_propiedades.shape)

        migrar_propiedades_extra(df_propiedades)
    finally:
        cliente.close()



    # MIGRACIÓN DE PROPIEDAD EXTRA ---------------------------


    
    df_propiedades = df_fichas[[ 
    'ci_pasaporte',
    'num_propiedades',
    'valor_propiedades',
    'num_vehiculos',
    'valor_vehiculos'
    ]]

    try:
    cliente = cliente_mysql()
   


    finally:
        cliente.close()

   
    df_propiedades['id_estudiante'] = df_propiedades['ci_pasaporte'].map(dic_id_estudiante)
    df_propiedades = df_propiedades.drop(columns=['ci_pasaporte'])
    df_propiedades = df_propiedades.dropna(subset=['id_estudiante'])

    df_propiedades.id_estudiante = df_propiedades.id_estudiante.astype(int)

    print(df_propiedades.sample(5))
    print(df_propiedades.shape)

    migrar_propiedades_extra(df_propiedades)

    finally:
    cliente.close()

    

    
    
main()

# Migración de Economía Estudiante
def migrar_economia_estudiante(df_economia):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO economia_estudiante (
            id_estudiante,
            total_ingresos,
            total_egresos
        ) VALUES (%s, %s, %s)
    """

  
    valores = list(df_economia.itertuples(index=False, name=None))

    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla economia_estudiante.")

    cursor.close()
    cliente.close()


# Migración de Economía df_fichas
def preparar_y_migrar_economia(df_fichas, dic_id_estudiante):
    df_economia = df_fichas[[ 
        'ci_pasaporte',
        'total_ingresos',
        'total_egresos'
    ]]

    try:
        cliente = cliente_mysql()

      
        df_economia['id_estudiante'] = df_economia['ci_pasaporte'].map(dic_id_estudiante)

        
        df_economia = df_economia.drop(columns=['ci_pasaporte'])
        df_economia = df_economia.dropna(subset=['id_estudiante'])
        df_economia.id_estudiante = df_economia.id_estudiante.astype(int)

     
        print(df_economia.sample(5))
        print(df_economia.shape)


        migrar_economia_estudiante(df_economia)

    finally:
        cliente.close()

#Migración Contacto de Emergencia
def migrar_contacto_emergencia(df_contactos):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO contacto_emergencia (
            id_estudiante,
            nombre_contacto,
            telefono_contacto
        ) VALUES (%s, %s, %s)
    """

    valores = list(df_contactos.itertuples(index=False, name=None))
    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla contacto_emergencia.")

    cursor.close()
    cliente.close()


def preparar_y_migrar_contacto_emergencia(df_fichas, dic_id_estudiante):
    df_contactos = df_fichas[[ 
        'ci_pasaporte',
        'nombre_contacto',
        'telefono_contacto'
    ]]

    try:
        cliente = cliente_mysql()

       
        df_contactos['id_estudiante'] = df_contactos['ci_pasaporte'].map(dic_id_estudiante)

        
        df_contactos = df_contactos.drop(columns=['ci_pasaporte'])
        df_contactos = df_contactos.dropna(subset=['id_estudiante'])
        df_contactos.id_estudiante = df_contactos.id_estudiante.astype(int)

        print(df_contactos.sample(5))
        print(df_contactos.shape)

        migrar_contacto_emergencia(df_contactos)

    finally:
        cliente.close()


    
# Migrar Datos salud
def migrar_datos_salud(df_salud):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO datos_salud (
            id_estudiante,
            tipo_sangre,
            semanas_embarazo,
            porcentaje_discapacidad,
            nombre_discapacidad,
            nombre_enfermedades,
            vacuna_covid,
            antecedentes_patologicos_fam
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = list(df_salud.itertuples(index=False, name=None))
    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla datos_salud.")

    cursor.close()
    cliente.close()

def preparar_y_migrar_datos_salud(df_fichas, dic_id_estudiante):
    df_salud = df_fichas[[ 
        'ci_pasaporte',
        'tipo_sangre',
        'semanas_embarazo',
        'porcentaje_discapacidad',
        'nombre_discapacidad',
        'enfermedades',
        'vacuna_covid',
        'antecedentes_patalogicos_fam' 
    ]]

    try:
        cliente = cliente_mysql()

        df_salud['id_estudiante'] = df_salud['ci_pasaporte'].map(dic_id_estudiante)

  
        df_salud = df_salud.drop(columns=['ci_pasaporte'])
        df_salud = df_salud.dropna(subset=['id_estudiante'])
        df_salud.id_estudiante = df_salud.id_estudiante.astype(int)

    
        print(df_salud.sample(5))
        print(df_salud.shape)

        # Migrar
        migrar_datos_salud(df_salud)

    finally:
        cliente.close()


# Migrar tabla Famiia
def migrar_familia(df_familia):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO familia (
            id_estudiante,
            integrantes_familia,
            integrantes_aporte_economico,
            cabezas_familia
        ) VALUES (%s, %s, %s, %s)
    """

    valores = list(df_familia.itertuples(index=False, name=None))
    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla familia.")

    cursor.close()
    cliente.close()

def preparar_y_migrar_familia(df_fichas, dic_id_estudiante):
    df_familia = df_fichas[[ 
        'ci_pasaporte',
        'integrantes_familia',
        'integrantes_aporte_economico',
        'cabezas_familia'
    ]]

    try:
        cliente = cliente_mysql()

        
        df_familia['id_estudiante'] = df_familia['ci_pasaporte'].map(dic_id_estudiante)

      
        df_familia = df_familia.drop(columns=['ci_pasaporte'])
        df_familia = df_familia.dropna(subset=['id_estudiante'])
        df_familia.id_estudiante = df_familia.id_estudiante.astype(int)

        print(df_familia.sample(5))
        print(df_familia.shape)

        migrar_familia(df_familia)

    finally:
        cliente.close()


# Migrar Vivienda
def migrar_vivienda(df_vivienda):
    cliente = cliente_mysql()
    cursor = cliente.cursor()

    sql = """
        INSERT IGNORE INTO vivienda (
            id_estudiante,
            tipo_vivienda,
            estructura_vivienda,
            servicios_vivienda
        ) VALUES (%s, %s, %s, %s)
    """

    valores = list(df_vivienda.itertuples(index=False, name=None))
    cursor.executemany(sql, valores)
    cliente.commit()

    print(f"{cursor.rowcount} filas insertadas en la tabla vivienda.")

    cursor.close()
    cliente.close()

def preparar_y_migrar_vivienda(df_fichas, dic_id_estudiante):
    df_vivienda = df_fichas[[ 
        'ci_pasaporte',
        'tipo_vivienda',
        'estructura_vivienda',
        'servicios_vivienda'
    ]]

    try:
        cliente = cliente_mysql()

        # Mapear ID del estudiante
        df_vivienda['id_estudiante'] = df_vivienda['ci_pasaporte'].map(dic_id_estudiante)

        # Limpiar y convertir
        df_vivienda = df_vivienda.drop(columns=['ci_pasaporte'])
        df_vivienda = df_vivienda.dropna(subset=['id_estudiante'])
        df_vivienda.id_estudiante = df_vivienda.id_estudiante.astype(int)

        print(df_vivienda.sample(5))
        print(df_vivienda.shape)

        migrar_vivienda(df_vivienda)

    finally:
        cliente.close()

