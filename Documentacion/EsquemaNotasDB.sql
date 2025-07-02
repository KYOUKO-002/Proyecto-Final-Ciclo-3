-- Crear base de datos
CREATE DATABASE IF NOT EXISTS NotasDB CHARACTER SET utf8 COLLATE utf8_general_ci;
USE NotasDB;

-- Tabla: estudiante
CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    identificacion VARCHAR(20) UNIQUE NOT NULL,
    nombres_estudiante VARCHAR(100) NOT NULL
);

-- Tabla: carrera
CREATE TABLE carrera (
    id_carrera INT AUTO_INCREMENT PRIMARY KEY,
    nombre_carrera VARCHAR(100) NOT NULL
);

-- Tabla: docente
CREATE TABLE docente (
    id_docente INT AUTO_INCREMENT PRIMARY KEY,
    cedula_docente VARCHAR(20) NOT NULL,
    nombre_docente VARCHAR(100) NOT NULL
);

-- Tabla: asignatura
CREATE TABLE asignatura (
    id_asignatura INT AUTO_INCREMENT PRIMARY KEY,
    nombre_asignatura VARCHAR(100),
    nivel VARCHAR(50),
    id_carrera INT,
    FOREIGN KEY (id_carrera) REFERENCES carrera(id_carrera)
);

-- Tabla: periodo NOOOOOOOOO
CREATE TABLE periodo (
    id_periodo INT AUTO_INCREMENT PRIMARY KEY,
    nombre_periodo VARCHAR(20),
    paralelo VARCHAR(10)
);

-- Tabla: matricula
CREATE TABLE matricula (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT,
    id_periodo INT,
    estado_matricula VARCHAR(50),
    tipo_ingreso VARCHAR(50),
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_periodo) REFERENCES periodo(id_periodo)
);

-- Tabla: detalle_matricula
CREATE TABLE detalle_matricula (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_matricula INT,
    id_asignatura INT,
    id_docente INT,
    asistencia DECIMAL(5,2),
    nota_final DECIMAL(5,2),
    estado_academico VARCHAR(50),
    FOREIGN KEY (id_matricula) REFERENCES matricula(id_matricula),
    FOREIGN KEY (id_asignatura) REFERENCES asignatura(id_asignatura),
    FOREIGN KEY (id_docente) REFERENCES docente(id_docente)
);




CREATE TABLE notas (
    id_notas INT AUTO_INCREMENT PRIMARY KEY,
    asistencia DECIMAL(5,2),
    nota_final DECIMAL(5,2),
    id_estudiante INT,
    id_asignatura INT,
    id_periodo INT,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_asignatura) REFERENCES asignatura(id_asignatura),
    FOREIGN KEY (id_periodo) REFERENCES periodo(id_periodo)
);
