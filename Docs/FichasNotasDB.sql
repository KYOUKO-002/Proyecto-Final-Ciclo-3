-- Crear base de datos
DROP DATABASE IF EXISTS FichasNotasDB;
CREATE DATABASE IF NOT EXISTS FichasNotasDB CHARACTER SET utf8 COLLATE utf8_general_ci;
USE FichasNotasDB;


-- Tabla: Estudiante
CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    ci_pasaporte VARCHAR(20) UNIQUE,
    correo_tec VARCHAR(100),
    nombres VARCHAR(100),
    sexo VARCHAR(10),
    genero VARCHAR(20),
    estado_civil VARCHAR(30),
    num_hijos INT,
    etnia VARCHAR(50),
    fecha_nacimiento DATE,
    tipo_parroquia VARCHAR(50),
    ciudad VARCHAR(50),
    provincia VARCHAR(50),
    pais VARCHAR(50),
    celular VARCHAR(20),
    tiene_beca BOOLEAN,
    estudio_otra_carrera BOOLEAN,
    ocupacion_estudiante VARCHAR(100),
    persona_cubre_gastos VARCHAR(100),
    recibe_ayuda BOOLEAN
);

-- Tabla: Carrera
CREATE TABLE carrera (
    id_carrera INT AUTO_INCREMENT PRIMARY KEY,
    nombre_carrera VARCHAR(200) UNIQUE
);

-- Tabla: EstudianteCarrera
DROP TABLE estudiante_carrera;
CREATE TABLE estudiante_carrera_backup AS SELECT * FROM estudiante_carrera;

-- 1. Eliminar la clave primaria compuesta
ALTER TABLE estudiante_carrera
DROP PRIMARY KEY;
-- 2. Agregar la nueva columna autoincrementable
ALTER TABLE estudiante_carrera

ADD COLUMN id_estudiante_carrera INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;
CREATE TABLE estudiante_carrera (
    id_carrera INT,
    id_estudiante INT,
    ciclo_carrera VARCHAR(20),
    razon_eleccion_carrera TEXT,
    razon_eleccion_instituto TEXT,
    periodo_academico VARCHAR(20),
    paralelo VARCHAR(11),
    PRIMARY KEY (id_carrera, id_estudiante, periodo_academico),
    FOREIGN KEY (id_carrera) REFERENCES carrera(id_carrera),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: ColegioGraduacion
DROP TABLE colegio_graduacion;
CREATE TABLE colegio_graduacion (
    id_colegio INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT UNIQUE,
    nombre_colegio VARCHAR(100),
    tipo_colegio VARCHAR(50),
    titulo_bachiller VARCHAR(50),
    anio_graduacion YEAR,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: PropiedadesExtra
CREATE TABLE propiedades_extra (
    id_propiedades INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    num_propiedades INT,
    valor_propiedades DECIMAL(10,2),
    num_vehiculos INT,
    valor_vehiculos DECIMAL(10,2),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: EconomiaEstudiante
CREATE TABLE economia_estudiante (
    id_economia INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    total_ingresos DECIMAL(10,2),
    total_egresos DECIMAL(10,2),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: ContactoEmergencia
CREATE TABLE contacto_emergencia (
    id_contacto_emergencia INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    nombre_contacto VARCHAR(100),
    telefono_contacto VARCHAR(20),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: DatosSalud
CREATE TABLE datos_salud (
    id_datos_salud INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    tipo_sangre VARCHAR(5),
    semanas_embarazo INT,
    porcentaje_discapacidad DECIMAL(5,2),
    nombre_discapacidad VARCHAR(100),
    nombre_enfermedades TEXT,
    vacuna_covid BOOLEAN,
    antecedentes_patologicos_fam TEXT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: Familia
CREATE TABLE familia (
    id_familia INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    integrantes_familia INT,
    integrantes_aporte_economico INT,
    cabezas_familia INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: Vivienda
CREATE TABLE vivienda (
    id_vivienda INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    tipo_vivienda VARCHAR(50),
    estructura_vivienda VARCHAR(50),
    servicios_vivienda TEXT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante)
);

-- Tabla: Asignatura
CREATE TABLE asignatura (
    id_asignatura INT AUTO_INCREMENT PRIMARY KEY,
    id_carrera INT,
    nombre_asignatura VARCHAR(100),
    FOREIGN KEY (id_carrera) REFERENCES carrera(id_carrera)
);

-- Tabla: EstudianteAsignatura
CREATE TABLE estudiante_asignatura (
    id_estudiante_asignatura INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante_carrera INT,
    id_asignatura INT,
    numero_matricula INT,
    porcentaje_asistencia DECIMAL(5,2),
    nota_final DECIMAL(5,2),
    estado_estudiante VARCHAR(50),
    estado_matricula VARCHAR(50),
    tipo_ingreso VARCHAR(50),
    FOREIGN KEY (id_estudiante_carrera) REFERENCES estudiante_carrera(id_estudiante_carrera),
    FOREIGN KEY (id_asignatura) REFERENCES asignatura(id_asignatura)
);
