# ======================= MYSQL =======================
class Pais:
    def __init__(self, nombre_pais):
        self.nombre_pais = nombre_pais


class Provincia:
    def __init__(self, nombre_provincia, id_pais):
        self.nombre_provincia = nombre_provincia
        self.id_pais = id_pais


class Ciudad:
    def __init__(self, nombre_ciudad, id_provincia):
        self.nombre_ciudad = nombre_ciudad
        self.id_provincia = id_provincia


class Barrio:
    def __init__(self, sector, tipo_parroquia, id_ciudad):
        self.sector = sector
        self.tipo_parroquia = tipo_parroquia
        self.id_ciudad = id_ciudad


class Estudiante:
    def __init__(self, cedula_pasaporte, nombres, apellidos, sexo, direccion, genero, estado_civil,
                 lugar_nacimiento, fecha_nacimiento, nro_hijos, etnia, idioma_nativo, celular,
                 telefono, id_barrio):
        self.cedula_pasaporte = cedula_pasaporte
        self.nombres = nombres
        self.apellidos = apellidos
        self.sexo = sexo
        self.direccion = direccion
        self.genero = genero
        self.estado_civil = estado_civil
        self.lugar_nacimiento = lugar_nacimiento
        self.fecha_nacimiento = fecha_nacimiento
        self.nro_hijos = nro_hijos
        self.etnia = etnia
        self.idioma_nativo = idioma_nativo
        self.celular = celular
        self.telefono = telefono
        self.id_barrio = id_barrio


class DireccionEmail:
    def __init__(self, email, id_estudiante):
        self.email = email
        self.id_estudiante = id_estudiante


class Vivienda:
    def __init__(self, condicion_vivienda, tipo_vivienda, estructura_vivienda, id_estudiante):
        self.condicion_vivienda = condicion_vivienda
        self.tipo_vivienda = tipo_vivienda
        self.estructura_vivienda = estructura_vivienda
        self.id_estudiante = id_estudiante


class ServicioBasico:
    def __init__(self, nombre_servicio):
        self.nombre_servicio = nombre_servicio


class OtraTitulacion:
    def __init__(self, nombre_carrera, registro_titulo, id_estudiante):
        self.nombre_carrera = nombre_carrera
        self.registro_titulo = registro_titulo
        self.id_estudiante = id_estudiante


class Carrera:
    def __init__(self, nombre_carrera):
        self.nombre_carrera = nombre_carrera


class CarreraEstudiante:
    def __init__(self, periodo, ciclo, razon_estudio, razones_eleccion_carrera, id_carrera, 
                 id_estudiante):
        self.periodo = periodo
        self.ciclo = ciclo
        self.razon_estudio = razon_estudio
        self.razones_eleccion_carrera = razones_eleccion_carrera
        self.id_carrera = id_carrera
        self.id_estudiante = id_estudiante


class EstructuraFamiliar:
    def __init__(self, familiares_conviven, familiares_aportan_economicamente, cabezas_familia,
                 familiares_cubren_estudio, id_estudiante):
        self.familiares_conviven = familiares_conviven
        self.familiares_aportan_economicamente = familiares_aportan_economicamente
        self.cabezas_familia = cabezas_familia
        self.familiares_cubren_estudio = familiares_cubren_estudio
        self.id_estudiante = id_estudiante


class AyudaEconomica:
    def __init__(self, tipo_ayuda, id_estudiante):
        self.tipo_ayuda = tipo_ayuda
        self.id_estudiante = id_estudiante


class OcupacionEstudiante:
    def __init__(self, tipo_ocupacion, id_estudiante):
        self.tipo_ocupacion = tipo_ocupacion
        self.id_estudiante = id_estudiante


class PropiedadExtra:
    def __init__(self, nro_propiedades, valor_propiedades, nro_vehiculo, valor_vehiculos, id_estudiante):
        self.nro_propiedades = nro_propiedades
        self.valor_propiedades = valor_propiedades
        self.nro_vehiculo = nro_vehiculo
        self.valor_vehiculos = valor_vehiculos
        self.id_estudiante = id_estudiante


class ContactoEmergencia:
    def __init__(self, nombre_contacto, telefono_contacto, id_estudiante):
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        self.id_estudiante = id_estudiante


class Beca:
    def __init__(self, tipo_beca, id_estudiante):
        self.tipo_beca = tipo_beca
        self.id_estudiante = id_estudiante


class Colegio:
    def __init__(self, nombre_colegio, tipo_colegio):
        self.nombre_colegio = nombre_colegio
        self.tipo_colegio = tipo_colegio


class TitulacionColegio:
    def __init__(self, anio_titulacion, tipo_titulacion, id_estudiante, id_colegio):
        self.anio_titulacion = anio_titulacion
        self.tipo_titulacion = tipo_titulacion
        self.id_estudiante = id_estudiante
        self.id_colegio = id_colegio


class Finanzas:
    def __init__(self, ingreso_mensual_estudiante, ingreso_mensual_conyuge, ingreso_mensual_padre,
                 ingreso_mensual_madre, ingreso_mensual_otros_familiares, otros_ingreso,
                 gasto_mensual_vivienda, gasto_mensual_alimentacion, gasto_mensual_educacion,
                 gasto_mensual_transporte, gasto_mensual_salud, gasto_mensual_servicios_basicos,
                 gasto_mensual_vestuarios, gasto_mensual_otros, id_estudiante):
        self.ingreso_mensual_estudiante = ingreso_mensual_estudiante
        self.ingreso_mensual_conyuge = ingreso_mensual_conyuge
        self.ingreso_mensual_padre = ingreso_mensual_padre
        self.ingreso_mensual_madre = ingreso_mensual_madre
        self.ingreso_mensual_otros_familiares = ingreso_mensual_otros_familiares
        self.otros_ingreso = otros_ingreso
        self.gasto_mensual_vivienda = gasto_mensual_vivienda
        self.gasto_mensual_alimentacion = gasto_mensual_alimentacion
        self.gasto_mensual_educacion = gasto_mensual_educacion
        self.gasto_mensual_transporte = gasto_mensual_transporte
        self.gasto_mensual_salud = gasto_mensual_salud
        self.gasto_mensual_servicios_basicos = gasto_mensual_servicios_basicos
        self.gasto_mensual_vestuarios = gasto_mensual_vestuarios
        self.gasto_mensual_otros = gasto_mensual_otros
        self.id_estudiante = id_estudiante


class DatosSalud:
    def __init__(self, tipo_sangre, discapacidad, tipo_discapacidad, porcentaje_discapacidad, carnet_conadis,
                 enfermedad_cronica, enfermedad_catastrofica, vacuna_covid, ultima_vacuna_covid,
                 tiempo_embarazo_semanas, discapacidad_multiple, otras_enfermedades, antecedentes_patologicos_familiares,
                 parentesco_problema_salud, id_estudiante):
        self.tipo_sangre = tipo_sangre
        self.discapacidad = discapacidad
        self.tipo_discapacidad = tipo_discapacidad
        self.porcentaje_discapacidad = porcentaje_discapacidad
        self.carnet_conadis = carnet_conadis
        self.enfermedad_cronica = enfermedad_cronica
        self.enfermedad_catastrofica = enfermedad_catastrofica
        self.vacuna_covid = vacuna_covid
        self.ultima_vacuna_covid = ultima_vacuna_covid
        self.tiempo_embarazo_semanas = tiempo_embarazo_semanas
        self.discapacidad_multiple = discapacidad_multiple
        self.otras_enfermedades = otras_enfermedades
        self.antecedentes_patologicos_familiares = antecedentes_patologicos_familiares
        self.parentesco_problema_salud = parentesco_problema_salud
        self.id_estudiante = id_estudiante


class ServicioVivienda:
    def __init__(self, id_servicio_basico, id_vivienda):
        self.id_servicio_basico = id_servicio_basico
        self.id_vivienda = id_vivienda


# ======================= MONGO =======================