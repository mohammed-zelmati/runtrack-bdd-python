-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categorie_chambre`
--

DROP TABLE IF EXISTS `categorie_chambre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie_chambre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `description` text,
  `prix_par_nuit` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie_chambre`
--

LOCK TABLES `categorie_chambre` WRITE;
/*!40000 ALTER TABLE `categorie_chambre` DISABLE KEYS */;
INSERT INTO `categorie_chambre` VALUES (1,'Simple','Chambre pour une personne',50.00),(2,'Double','Chambre pour deux personnes',80.00),(3,'Suite','Suite luxueuse',200.00),(4,'Familiale','Chambre pour une famille',120.00),(5,'Deluxe','Chambre avec vue panoramique',150.00);
/*!40000 ALTER TABLE `categorie_chambre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chambre`
--

DROP TABLE IF EXISTS `chambre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chambre` (
  `id` int NOT NULL AUTO_INCREMENT,
  `numero_chambre` int NOT NULL,
  `id_categorie` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_chambre` (`numero_chambre`),
  KEY `id_categorie` (`id_categorie`),
  CONSTRAINT `chambre_ibfk_1` FOREIGN KEY (`id_categorie`) REFERENCES `categorie_chambre` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chambre`
--

LOCK TABLES `chambre` WRITE;
/*!40000 ALTER TABLE `chambre` DISABLE KEYS */;
INSERT INTO `chambre` VALUES (1,101,1),(2,102,1),(3,103,2),(4,104,2),(5,105,3),(6,106,3),(7,107,4),(8,108,4),(9,109,5),(10,110,5);
/*!40000 ALTER TABLE `chambre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `date_naissance` date NOT NULL,
  `adresse` varchar(255) DEFAULT NULL,
  `pays_origine` varchar(100) DEFAULT NULL,
  `nationalite` varchar(100) DEFAULT NULL,
  `numero_identite` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telephone` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero_identite` (`numero_identite`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'Mounir','Ahmed','1985-03-15','Rue ABC, Marseille','France','Fran├ºaise','123456789','mounir@example.com','123456789'),(2,'Fatima','Zahra','1990-07-22','Rue DEF, Paris','Maroc','Marocaine','987654321','fatima@example.com','987654321'),(3,'Ali','Boumediene','1988-05-12','Rue GHI, Lyon','Alg├®rie','Alg├®rienne','192837465','ali@example.com','192837465'),(4,'Sarah','Mansour','1993-11-02','Rue JKL, Bordeaux','Tunisie','Tunisienne','182736455','sarah@example.com','182736455'),(5,'Omar','Hassan','1987-09-19','Rue MNO, Nice','France','Fran├ºaise','112233445','omar@example.com','112233445'),(6,'Leila','Mohamed','1991-01-08','Rue PQR, Toulouse','├ëgypte','├ëgyptienne','556677889','leila@example.com','556677889'),(7,'Yasmine','Bouchra','1989-04-25','Rue STU, Lille','France','Fran├ºaise','998877665','yasmine@example.com','998877665'),(8,'Hassan','Kamel','1992-10-17','Rue VWX, Strasbourg','France','Fran├ºaise','123443211','hassan@example.com','123443211'),(9,'Amine','Badr','1986-06-30','Rue YZA, Montpellier','Alg├®rie','Alg├®rienne','667788990','amine@example.com','667788990'),(10,'Nadia','Saad','1994-08-13','Rue BCD, Marseille','Maroc','Marocaine','445566778','nadia@example.com','445566778');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paiement`
--

DROP TABLE IF EXISTS `paiement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paiement` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_reservation` int NOT NULL,
  `date_paiement` date NOT NULL,
  `heure_paiement` time NOT NULL,
  `numero_carte` varchar(20) NOT NULL,
  `nom_banque` varchar(100) DEFAULT NULL,
  `code_transaction` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code_transaction` (`code_transaction`),
  KEY `id_reservation` (`id_reservation`),
  CONSTRAINT `paiement_ibfk_1` FOREIGN KEY (`id_reservation`) REFERENCES `reservation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paiement`
--

LOCK TABLES `paiement` WRITE;
/*!40000 ALTER TABLE `paiement` DISABLE KEYS */;
INSERT INTO `paiement` VALUES (1,1,'2025-03-01','10:30:00','123456789123','BNP Paribas','TXN001'),(2,2,'2025-03-03','14:20:00','987654321987','Soci├®t├® G├®n├®rale','TXN002'),(3,3,'2025-03-10','09:00:00','112233445566','LCL','TXN003'),(4,4,'2025-03-12','12:45:00','998877665544','Cr├®dit Agricole','TXN004'),(5,5,'2025-03-20','16:30:00','556677889900','HSBC','TXN005'),(6,6,'2025-03-18','11:00:00','332211009988','BNP Paribas','TXN006'),(7,7,'2025-03-02','13:15:00','445566778899','Cr├®dit Mutuel','TXN007'),(8,8,'2025-03-08','10:45:00','778899112233','Soci├®t├® G├®n├®rale','TXN008'),(9,9,'2025-03-22','15:00:00','990011223344','LCL','TXN009'),(10,10,'2025-03-14','08:30:00','123443211234','Cr├®dit Agricole','TXN010'),(11,11,'2025-03-15','14:00:00','556788990012','BNP Paribas','TXN011'),(12,12,'2025-03-05','10:30:00','667788001234','HSBC','TXN012'),(13,13,'2025-03-19','09:45:00','445599112345','Cr├®dit Mutuel','TXN013'),(14,14,'2025-03-07','11:10:00','112233441122','LCL','TXN014'),(15,15,'2025-03-23','12:00:00','667755332211','BNP Paribas','TXN015');
/*!40000 ALTER TABLE `paiement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_client` int NOT NULL,
  `date_debut` date NOT NULL,
  `date_fin` date NOT NULL,
  `tarif_total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_client` (`id_client`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,1,'2025-03-01','2025-03-05',200.00),(2,2,'2025-03-03','2025-03-07',400.00),(3,3,'2025-03-10','2025-03-15',600.00),(4,4,'2025-03-12','2025-03-14',240.00),(5,5,'2025-03-20','2025-03-25',500.00),(6,6,'2025-03-18','2025-03-21',300.00),(7,7,'2025-03-02','2025-03-06',400.00),(8,8,'2025-03-08','2025-03-12',480.00),(9,9,'2025-03-22','2025-03-26',750.00),(10,10,'2025-03-14','2025-03-17',450.00),(11,1,'2025-03-15','2025-03-20',700.00),(12,3,'2025-03-05','2025-03-10',550.00),(13,4,'2025-03-19','2025-03-22',360.00),(14,6,'2025-03-07','2025-03-09',260.00),(15,7,'2025-03-23','2025-03-28',880.00);
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation_chambre`
--

DROP TABLE IF EXISTS `reservation_chambre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation_chambre` (
  `id_reservation` int NOT NULL,
  `id_chambre` int NOT NULL,
  PRIMARY KEY (`id_reservation`,`id_chambre`),
  KEY `id_chambre` (`id_chambre`),
  CONSTRAINT `reservation_chambre_ibfk_1` FOREIGN KEY (`id_reservation`) REFERENCES `reservation` (`id`),
  CONSTRAINT `reservation_chambre_ibfk_2` FOREIGN KEY (`id_chambre`) REFERENCES `chambre` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation_chambre`
--

LOCK TABLES `reservation_chambre` WRITE;
/*!40000 ALTER TABLE `reservation_chambre` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservation_chambre` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-14 14:09:12
