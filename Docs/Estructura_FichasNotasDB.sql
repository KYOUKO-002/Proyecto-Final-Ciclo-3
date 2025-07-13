CREATE DATABASE  IF NOT EXISTS `fichasnotasdb` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `fichasnotasdb`;
-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: fichasnotasdb
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `asignatura`
--

DROP TABLE IF EXISTS `asignatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asignatura` (
  `id_asignatura` int NOT NULL AUTO_INCREMENT,
  `id_carrera` int DEFAULT NULL,
  `nombre_asignatura` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_asignatura`),
  UNIQUE KEY `nombre_asignatura` (`nombre_asignatura`),
  KEY `id_carrera` (`id_carrera`),
  CONSTRAINT `asignatura_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carrera` (`id_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=26079 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `carrera`
--

DROP TABLE IF EXISTS `carrera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrera` (
  `id_carrera` int NOT NULL AUTO_INCREMENT,
  `codigo_carrera` varchar(50) DEFAULT NULL,
  `nombre_carrera` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_carrera`),
  UNIQUE KEY `codigo_carrera` (`codigo_carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=26079 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `colegio_graduacion`
--

DROP TABLE IF EXISTS `colegio_graduacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colegio_graduacion` (
  `id_colegio` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `nombre_colegio` varchar(100) DEFAULT NULL,
  `tipo_colegio` varchar(50) DEFAULT NULL,
  `titulo_bachiller` varchar(50) DEFAULT NULL,
  `anio_graduacion` int DEFAULT NULL,
  PRIMARY KEY (`id_colegio`),
  UNIQUE KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `colegio_graduacion_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `contacto_emergencia`
--

DROP TABLE IF EXISTS `contacto_emergencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacto_emergencia` (
  `id_contacto_emergencia` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `nombre_contacto` varchar(100) DEFAULT NULL,
  `telefono_contacto` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_contacto_emergencia`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `contacto_emergencia_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `datos_salud`
--

DROP TABLE IF EXISTS `datos_salud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `datos_salud` (
  `id_datos_salud` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `tipo_sangre` varchar(11) DEFAULT NULL,
  `semanas_embarazo` int DEFAULT NULL,
  `porcentaje_discapacidad` decimal(5,2) DEFAULT NULL,
  `nombre_discapacidad` varchar(100) DEFAULT NULL,
  `nombre_enfermedades` text,
  `vacuna_covid` varchar(70) DEFAULT NULL,
  `antecedentes_patologicos_fam` text,
  PRIMARY KEY (`id_datos_salud`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `datos_salud_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `economia_estudiante`
--

DROP TABLE IF EXISTS `economia_estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `economia_estudiante` (
  `id_economia` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `total_ingresos` decimal(10,2) DEFAULT NULL,
  `total_egresos` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_economia`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `economia_estudiante_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estudiante`
--

DROP TABLE IF EXISTS `estudiante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante` (
  `id_estudiante` int NOT NULL AUTO_INCREMENT,
  `ci_pasaporte` varchar(20) DEFAULT NULL,
  `correo_tec` varchar(100) DEFAULT NULL,
  `nombres` varchar(100) DEFAULT NULL,
  `sexo` varchar(11) DEFAULT NULL,
  `genero` varchar(20) DEFAULT NULL,
  `estado_civil` varchar(30) DEFAULT NULL,
  `num_hijos` int DEFAULT NULL,
  `etnia` varchar(50) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `tipo_parroqui` varchar(50) DEFAULT NULL,
  `ciudad` varchar(50) DEFAULT NULL,
  `provincia` varchar(50) DEFAULT NULL,
  `pais` varchar(50) DEFAULT NULL,
  `celular` varchar(20) DEFAULT NULL,
  `tiene_beca` tinyint(1) DEFAULT NULL,
  `estudio_otra_carrera` tinyint(1) DEFAULT NULL,
  `ocupacion_estudiante` varchar(100) DEFAULT NULL,
  `persona_cubre_gastos` varchar(100) DEFAULT NULL,
  `recibe_ayuda` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_estudiante`),
  UNIQUE KEY `ci_pasaporte` (`ci_pasaporte`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estudiante_asignatura`
--

DROP TABLE IF EXISTS `estudiante_asignatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante_asignatura` (
  `id_estudiante_carrera` int NOT NULL,
  `id_asignatura` int NOT NULL,
  `numero_matricula` int DEFAULT NULL,
  `porcentaje_asistencia` decimal(5,2) DEFAULT NULL,
  `nota_final` decimal(5,2) DEFAULT NULL,
  `estado_estudiante` varchar(50) DEFAULT NULL,
  `estado_matricula` varchar(50) DEFAULT NULL,
  `tipo_ingreso` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_estudiante_carrera`,`id_asignatura`),
  KEY `id_asignatura` (`id_asignatura`),
  CONSTRAINT `estudiante_asignatura_ibfk_1` FOREIGN KEY (`id_estudiante_carrera`) REFERENCES `estudiante_carrera` (`id_estudiante_carrera`),
  CONSTRAINT `estudiante_asignatura_ibfk_2` FOREIGN KEY (`id_asignatura`) REFERENCES `asignatura` (`id_asignatura`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `estudiante_carrera`
--

DROP TABLE IF EXISTS `estudiante_carrera`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiante_carrera` (
  `id_estudiante_carrera` int NOT NULL AUTO_INCREMENT,
  `id_carrera` int DEFAULT NULL,
  `id_estudiante` int DEFAULT NULL,
  `ciclo_carrera` varchar(20) DEFAULT NULL,
  `periodo_academico` varchar(20) DEFAULT NULL,
  `paralelo` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`id_estudiante_carrera`),
  KEY `id_carrera` (`id_carrera`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `estudiante_carrera_ibfk_1` FOREIGN KEY (`id_carrera`) REFERENCES `carrera` (`id_carrera`),
  CONSTRAINT `estudiante_carrera_ibfk_2` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=5139 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `familia`
--

DROP TABLE IF EXISTS `familia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `familia` (
  `id_familia` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `integrantes_familia` text,
  `integrantes_aporte_economico` text,
  `cabezas_familia` text,
  PRIMARY KEY (`id_familia`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `familia_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `propiedades_extra`
--

DROP TABLE IF EXISTS `propiedades_extra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `propiedades_extra` (
  `id_propiedades` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `num_propiedades` int DEFAULT NULL,
  `valor_propiedades` decimal(10,2) DEFAULT NULL,
  `num_vehiculos` int DEFAULT NULL,
  `valor_vehiculos` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_propiedades`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `propiedades_extra_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vivienda`
--

DROP TABLE IF EXISTS `vivienda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vivienda` (
  `id_vivienda` int NOT NULL AUTO_INCREMENT,
  `id_estudiante` int DEFAULT NULL,
  `tipo_vivienda` varchar(100) DEFAULT NULL,
  `condicion_vivienda` varchar(100) DEFAULT NULL,
  `servicios_vivienda` text,
  PRIMARY KEY (`id_vivienda`),
  KEY `id_estudiante` (`id_estudiante`),
  CONSTRAINT `vivienda_ibfk_1` FOREIGN KEY (`id_estudiante`) REFERENCES `estudiante` (`id_estudiante`)
) ENGINE=InnoDB AUTO_INCREMENT=3964 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-13 12:09:48
