import pandas as pd
import numpy as np
import re

# =========================== FICHAS SOCIOECONÓMICAS ===========================
renombre_fichassc = ['ci_pasaporte','correo_tec','primer_nombre','segun_nombre','primer_apellido','segun_apellido','sexo','genero','estado_civil','num_hijos',
                     'etnia','fecha_nacimiento','tipo_parroquia', 'ciudad','prov','pais','celular','nombre_carrera','ciclo_carrera','tiene_beca','colegio','tipo_colegio',
                     'titulo_bachiller','anio_graduacion','estudio_otra_carrera','integrantes_familia','integrantes_aporte_economico','cabezas_familia','estado_vivienda','tipo_vivienda',
                     'estructura_vivienda','servicios_vivienda','ocupacion_estudiante','persona_cubre_gastos','recibe_ayuda','num_propiedades','valor_propiedades','num_vehiculos',
                     'valor_vehiculos','total_ingresos','total_egresos','razon_eleccion_instituto','razon_eleccion_carrera','nombre_contacto','telefono_contacto','tipo_sangre',
                     'semanas_embarazo','porcentaje_discapacidad','nombre_discapacidad','enfermedades','vacuna_covid','antecedentes_patalogicos_fam','periodo_academico']

df_2024p1 = pd.read_excel('/content/02 FICHA SOCIOECONÓMICA Y DE SALUD ABRIL 2024 -AGOSTO 2024 (respuestas) (3).xlsx').astype("string")
df_2025p1 = pd.read_excel('/content/FICHA SOCIOECONÓMICA Y DE SALUD ABRIL 2025 -AGOSTO 2025 (respuestas).xlsx').astype("string")
df_2023p1 = pd.read_excel('/content/FICHA SOCIOECONÓMICA Y DE SALUD ABRIL-AGOSTO 2023 (respuestas) (3) (1).xlsx').astype("string")
df_2024p2 = pd.read_excel('/content/FICHA SOCIOECONÓMICA Y DE SALUD OCTUBRE 2024 -FEBRERO 2025 (respuestas) (1).xlsx').astype("string")
df_2023p2 = pd.read_excel('/content/FICHA SOCIOECONÓMICA Y DE SALUD SEPTIEMBRE 2023-ENERO 2024.xlsx').astype("string")

print(len(df_2023p1.columns.tolist()))
print(len(df_2023p2.columns.tolist()))
print(len(df_2024p1.columns.tolist()))
print(len(df_2024p2.columns.tolist()))
print(len(df_2025p1.columns.tolist()))

df_2023p1['periodo_academico'] = '2023-1P'
df_2023p2['periodo_academico'] = '2023-2P'
df_2024p1['periodo_academico'] = '2024-1P'
df_2024p2['periodo_academico'] = '2024-2P'
df_2025p1['periodo_academico'] = '2025-1P'

df_2024p1.columns = renombre_fichassc
df_2025p1.columns = renombre_fichassc
df_2023p1.columns = renombre_fichassc
df_2024p2.columns = renombre_fichassc
df_2023p2.columns = renombre_fichassc

df_fichassc = pd.concat([
    df_2023p1,
    df_2023p2,
    df_2024p1,
    df_2024p2,
    df_2025p1
], ignore_index=True)

for col in df_fichassc.columns:
    if col != "correo_tec":
        df_fichassc[col] = (
            df_fichassc[col]
            .str.upper()
            .str.replace('.', '', regex=False)
            .str.strip()
        )

df_fichassc["nombres"] = (
    df_fichassc["primer_nombre"] + " " +
    df_fichassc["segun_nombre"] + " " +
    df_fichassc["primer_apellido"] + " " +
    df_fichassc["segun_apellido"]
)

df_fichassc = df_fichassc.drop(columns=["primer_nombre", "segun_nombre", "primer_apellido", "segun_apellido"])


col_fichassc_numericas = [
    'num_hijos', 'num_propiedades', 'valor_propiedades',
    'num_vehiculos', 'valor_vehiculos', 'total_ingresos',
    'total_egresos', 'anio_graduacion', 'semanas_embarazo',
    'porcentaje_discapacidad'
]

for col in col_fichassc_numericas:
    if col in df_fichassc.columns:
        df_fichassc[col] = (
            df_fichassc[col]
            .fillna('')
            .str.replace(r'\D', '', regex=True)
            .replace('', '0')
            .astype(int)
        )

def limpiar_tipo_sangre(valor):
    if pd.isna(valor):
        return ''
    valor_filtrado = re.sub(r'[^ABO+-]', '', valor)
    resultado = ''
    for c in valor_filtrado:
        if c not in resultado:
            resultado += c
    return resultado


if "tipo_sangre" in df_fichassc.columns:
    df_fichassc["tipo_sangre"] = df_fichassc["tipo_sangre"].apply(limpiar_tipo_sangre)

df_fichassc.to_excel("fichas_limpias.xlsx", index=False)


# =========================== NOTAS ESTUDIANTES ===========================
renombre_notas = ['periodo_academico', 'paralelo', 'ci_estudiante','carrera', 'estudiante', 'nivel', 'asignatura',
                  'num_matricula', 'asistencia', 'nota_final', 'estado', 'estado_matricula', 'tipo_ingreso',
                  'ci_docente', 'docente']

df_notas2023p1 = pd.read_excel('/content/MAESTRO DE NOTAS-2023-1P.xls', skiprows=3)
df_notas2023p2 = pd.read_excel('/content/MAESTRO DE NOTAS-2023-2P.xls', skiprows=3)
df_notas2024p1 = pd.read_excel('/content/MAESTRO DE NOTAS-2024-1P.xls', skiprows=3)
df_notas2024p2 = pd.read_excel('/content/MAESTRO DE NOTAS-2024-2P.xlsx', skiprows=3)

df_notas2023p1 = df_notas2023p1.loc[:, ~df_notas2023p1.columns.str.contains('^Unnamed')]
df_notas2023p2 = df_notas2023p2.loc[:, ~df_notas2023p2.columns.str.contains('^Unnamed')]
df_notas2024p1 = df_notas2024p1.loc[:, ~df_notas2024p1.columns.str.contains('^Unnamed')]
df_notas2024p2 = df_notas2024p2.loc[:, ~df_notas2024p2.columns.str.contains('^Unnamed')]

print(len(df_notas2023p1.columns.tolist()))
print(len(df_notas2023p2.columns.tolist()))
print(len(df_notas2024p1.columns.tolist()))
print(len(df_notas2024p2.columns.tolist()))

df_notas2023p1.columns = renombre_notas
df_notas2023p2.columns = renombre_notas
df_notas2024p1.columns = renombre_notas
df_notas2024p2.columns = renombre_notas

df_notas = pd.concat([
    df_notas2023p1,
    df_notas2023p2,
    df_notas2024p1,
    df_notas2024p2
], ignore_index=True)

df_notas['ci_estudiante'] = df_notas['ci_estudiante'].astype(str).str.zfill(10)
df_notas['ci_docente'] = df_notas['ci_docente'].astype(str).str.zfill(10)

for col in df_notas.columns:
    if pd.api.types.is_string_dtype(df_notas[col]) or df_notas[col].dtype == object:
        df_notas[col] = df_notas[col].fillna("DESCONOCIDO")
    elif pd.api.types.is_numeric_dtype(df_notas[col]):
        df_notas[col] = df_notas[col].fillna(0)

df_notas.to_excel("notas_limpias.xlsx", index=False)
