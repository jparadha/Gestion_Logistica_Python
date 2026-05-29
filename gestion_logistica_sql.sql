-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-05-2026 a las 17:58:35
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- --------------------------------------------------------
-- Base de datos: `gestion_logistica`
--
CREATE DATABASE IF NOT EXISTS `gestion_logistica` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `gestion_logistica`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `envios`
--

CREATE TABLE `envios` (
  `ID` int(11) NOT NULL,
  `NumeroSeguimiento` varchar(50) NOT NULL,
  `Origen` varchar(100) NOT NULL,
  `Destino` varchar(100) NOT NULL,
  `FechaEntregaPrevista` date DEFAULT NULL,
  `Estado` varchar(50) DEFAULT 'En tránsito'
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Volcado de datos para la tabla `envios`
--

INSERT INTO `envios` (`ID`, `NumeroSeguimiento`, `Origen`, `Destino`, `FechaEntregaPrevista`, `Estado`) VALUES
(1, 'ENV-001', 'Santiago', 'Valparaíso', '2026-06-10', 'En tránsito'),
(2, 'ENV-002', 'Concepción', 'Antofagasta', '2026-06-12', 'Pendiente'),
(3, 'ENV-003', 'Puerto Montt', 'La Serena', '2026-06-15', 'Entregado');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `envios`
--
ALTER TABLE `envios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `envios`
--
ALTER TABLE `envios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- Base de datos: `phpmyadmin`
--
CREATE DATABASE IF NOT EXISTS `phpmyadmin` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
USE `phpmyadmin`;