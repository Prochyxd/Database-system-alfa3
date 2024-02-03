START TRANSACTION;
CREATE DATABASE  IF NOT EXISTS `funeral_db` /*!40100 DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_czech_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `funeral_db`;
-- Procházka Adam, C4c, prochazka7@spsejecna.cz
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: funeral_db
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `cemetery`
--

DROP TABLE IF EXISTS `cemetery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cemetery` (
  `cemeteryID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`cemeteryID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cemetery`
--

LOCK TABLES `cemetery` WRITE;
/*!40000 ALTER TABLE `cemetery` DISABLE KEYS */;
INSERT INTO `cemetery` VALUES (1,'Hřbitov','Praha'),(2,'Hřbitov','Brno'),(3,'Hřbitov','Ostrava'),(4,'Hřbitov','Plzeň'),(5,'Hřbitov','Liberec'),(6,'Hřbitov','Olomouc'),(7,'Hřbitov','Ústí nad Labem'),(8,'Hřbitov','Hradec Králové'),(9,'Hřbitov','Pardubice'),(10,'Hřbitov','Zlín'),(11,'Hřbitov','Jihlava'),(12,'Hřbitov','České Budějovice');
/*!40000 ALTER TABLE `cemetery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deceased`
--

DROP TABLE IF EXISTS `deceased`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `deceased` (
  `deceasedID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `surname` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `date_of_birth` date NOT NULL,
  `date_of_death` date NOT NULL,
  PRIMARY KEY (`deceasedID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deceased`
--

LOCK TABLES `deceased` WRITE;
/*!40000 ALTER TABLE `deceased` DISABLE KEYS */;
INSERT INTO `deceased` VALUES (1,'Jan','Novák','1980-01-01','2020-01-01'),(2,'Petr','Svoboda','1970-01-01','2020-01-01'),(3,'Marie','Kovářová','1990-01-01','2020-01-01'),(4,'Jana','Nováková','1985-01-01','2020-01-01'),(5,'Pavel','Svoboda','1975-01-01','2020-01-01'),(6,'Josef','Kovář','1995-01-01','2020-01-01'),(7,'Jiří','Novák','1980-01-01','2020-01-01'),(8,'Petr','Svoboda','1970-01-01','2020-01-01'),(9,'Marie','Kovářová','1990-01-01','2020-01-01'),(10,'Jana','Nováková','1985-01-01','2020-01-01'),(11,'Pavel','Svoboda','1975-01-01','2020-01-01'),(12,'Josef','Kovář','1995-01-01','2020-01-01');
/*!40000 ALTER TABLE `deceased` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funeral`
--

DROP TABLE IF EXISTS `funeral`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funeral` (
  `funeralID` int NOT NULL AUTO_INCREMENT,
  `deceasedID` int NOT NULL,
  `serviceID` int NOT NULL,
  `cemeteryID` int NOT NULL,
  `date` datetime NOT NULL,
  `participantID` int DEFAULT NULL,
  PRIMARY KEY (`funeralID`),
  KEY `deceasedID` (`deceasedID`),
  KEY `serviceID` (`serviceID`),
  KEY `cemeteryID` (`cemeteryID`),
  KEY `participantID` (`participantID`),
  CONSTRAINT `funeral_ibfk_1` FOREIGN KEY (`deceasedID`) REFERENCES `deceased` (`deceasedID`),
  CONSTRAINT `funeral_ibfk_2` FOREIGN KEY (`serviceID`) REFERENCES `funeral_service` (`serviceID`),
  CONSTRAINT `funeral_ibfk_3` FOREIGN KEY (`cemeteryID`) REFERENCES `cemetery` (`cemeteryID`),
  CONSTRAINT `funeral_ibfk_4` FOREIGN KEY (`participantID`) REFERENCES `participants` (`participantID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funeral`
--

LOCK TABLES `funeral` WRITE;
/*!40000 ALTER TABLE `funeral` DISABLE KEYS */;
INSERT INTO `funeral` VALUES (1,1,1,1,'2020-01-01 12:00:00',1),(2,2,2,2,'2020-01-01 12:00:00',2),(3,3,3,3,'2020-01-01 12:00:00',3),(4,4,1,4,'2020-01-01 12:00:00',4),(5,5,2,5,'2020-01-01 12:00:00',5),(6,6,3,6,'2020-01-01 12:00:00',6),(7,7,1,7,'2020-01-01 12:00:00',7),(8,8,2,8,'2020-01-01 12:00:00',8),(9,9,3,9,'2020-01-01 12:00:00',9),(10,10,1,10,'2020-01-01 12:00:00',10),(11,11,2,11,'2020-01-01 12:00:00',11),(12,12,3,12,'2020-01-01 12:00:00',12);
/*!40000 ALTER TABLE `funeral` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funeral_service`
--

DROP TABLE IF EXISTS `funeral_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funeral_service` (
  `serviceID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`serviceID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funeral_service`
--

LOCK TABLES `funeral_service` WRITE;
/*!40000 ALTER TABLE `funeral_service` DISABLE KEYS */;
INSERT INTO `funeral_service` VALUES (1,'Základní',1000),(2,'Standardní',2000),(3,'Luxusní',3000);
/*!40000 ALTER TABLE `funeral_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `funeral_view`
--

DROP TABLE IF EXISTS `funeral_view`;
/*!50001 DROP VIEW IF EXISTS `funeral_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `funeral_view` AS SELECT 
 1 AS `funeralID`,
 1 AS `deceased_name`,
 1 AS `deceased_surname`,
 1 AS `service_name`,
 1 AS `cemetery_name`,
 1 AS `date`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `logID` int NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `message` text COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`logID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `log_view`
--

DROP TABLE IF EXISTS `log_view`;
/*!50001 DROP VIEW IF EXISTS `log_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `log_view` AS SELECT 
 1 AS `logID`,
 1 AS `date`,
 1 AS `message`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `participants`
--

DROP TABLE IF EXISTS `participants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `participants` (
  `participantID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `surname` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `relationship` enum('family','friend','other') COLLATE utf8mb3_czech_ci NOT NULL,
  PRIMARY KEY (`participantID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_czech_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `participants`
--

LOCK TABLES `participants` WRITE;
/*!40000 ALTER TABLE `participants` DISABLE KEYS */;
INSERT INTO `participants` VALUES (1,'Petr','Novák','family'),(2,'Marie','Svobodová','family'),(3,'Jana','Kovářová','family'),(4,'Pavel','Novák','friend'),(5,'Josef','Svoboda','friend'),(6,'Jiří','Kovář','friend'),(7,'Petr','Novák','family'),(8,'Marie','Svobodová','family'),(9,'Jana','Kovářová','family'),(10,'Pavel','Novák','other'),(11,'Josef','Svoboda','friend'),(12,'Jiří','Kovář','friend');
/*!40000 ALTER TABLE `participants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'funeral_db'
--

--
-- Dumping routines for database 'funeral_db'
--

--
-- Final view structure for view `funeral_view`
--

/*!50001 DROP VIEW IF EXISTS `funeral_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `funeral_view` AS select `funeral`.`funeralID` AS `funeralID`,`deceased`.`name` AS `deceased_name`,`deceased`.`surname` AS `deceased_surname`,`funeral_service`.`name` AS `service_name`,`cemetery`.`name` AS `cemetery_name`,`funeral`.`date` AS `date` from (((`funeral` join `deceased` on((`funeral`.`deceasedID` = `deceased`.`deceasedID`))) join `funeral_service` on((`funeral`.`serviceID` = `funeral_service`.`serviceID`))) join `cemetery` on((`funeral`.`cemeteryID` = `cemetery`.`cemeteryID`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `log_view`
--

/*!50001 DROP VIEW IF EXISTS `log_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `log_view` AS select `log`.`logID` AS `logID`,`log`.`date` AS `date`,`log`.`message` AS `message` from `log` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-03 18:26:17

COMMIT;
