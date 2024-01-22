CREATE DATABASE  IF NOT EXISTS `erp_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `erp_system`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: erp_system
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add product',7,'add_product'),(26,'Can change product',7,'change_product'),(27,'Can delete product',7,'delete_product'),(28,'Can view product',7,'view_product'),(29,'Can add raw material',8,'add_rawmaterial'),(30,'Can change raw material',8,'change_rawmaterial'),(31,'Can delete raw material',8,'delete_rawmaterial'),(32,'Can view raw material',8,'view_rawmaterial'),(33,'Can add warehouse',9,'add_warehouse'),(34,'Can change warehouse',9,'change_warehouse'),(35,'Can delete warehouse',9,'delete_warehouse'),(36,'Can view warehouse',9,'view_warehouse'),(37,'Can add raw material inventory',10,'add_rawmaterialinventory'),(38,'Can change raw material inventory',10,'change_rawmaterialinventory'),(39,'Can delete raw material inventory',10,'delete_rawmaterialinventory'),(40,'Can view raw material inventory',10,'view_rawmaterialinventory'),(41,'Can add production order',11,'add_productionorder'),(42,'Can change production order',11,'change_productionorder'),(43,'Can delete production order',11,'delete_productionorder'),(44,'Can view production order',11,'view_productionorder'),(45,'Can add product inventory',12,'add_productinventory'),(46,'Can change product inventory',12,'change_productinventory'),(47,'Can delete product inventory',12,'delete_productinventory'),(48,'Can view product inventory',12,'view_productinventory'),(49,'Can add customer',13,'add_customer'),(50,'Can change customer',13,'change_customer'),(51,'Can delete customer',13,'delete_customer'),(52,'Can view customer',13,'view_customer'),(53,'Can add supplier',14,'add_supplier'),(54,'Can change supplier',14,'change_supplier'),(55,'Can delete supplier',14,'delete_supplier'),(56,'Can view supplier',14,'view_supplier'),(57,'Can add product raw material',15,'add_productrawmaterial'),(58,'Can change product raw material',15,'change_productrawmaterial'),(59,'Can delete product raw material',15,'delete_productrawmaterial'),(60,'Can view product raw material',15,'view_productrawmaterial'),(61,'Can add purchase order',16,'add_purchaseorder'),(62,'Can change purchase order',16,'change_purchaseorder'),(63,'Can delete purchase order',16,'delete_purchaseorder'),(64,'Can view purchase order',16,'view_purchaseorder'),(65,'Can add sales order',17,'add_salesorder'),(66,'Can change sales order',17,'change_salesorder'),(67,'Can delete sales order',17,'delete_salesorder'),(68,'Can view sales order',17,'view_salesorder'),(69,'Can add sales order item',18,'add_salesorderitem'),(70,'Can change sales order item',18,'change_salesorderitem'),(71,'Can delete sales order item',18,'delete_salesorderitem'),(72,'Can view sales order item',18,'view_salesorderitem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$600000$4Uhz5tjXqmw0FL8IqnKs3b$TACAIIOBkgHMc3H8O8d5dinEldacauLt4BIyqAxlG70=','2024-01-21 10:18:09.598389',1,'admin','','','',1,1,'2023-12-30 07:31:21.576596'),(2,'pbkdf2_sha256$600000$oYqdG9JRsnsXQxMRm86eRH$NNKIIb9KRheIT4GVrvYMIBy0vrZj7T7zfPuNfFg8Gbg=','2024-01-18 16:20:07.873580',0,'newUser','','','',0,1,'2024-01-18 16:20:07.363333'),(3,'pbkdf2_sha256$600000$GGvnERLxq25upotAYtxf8g$8YDRUnKZ2/V1rZIefHB7lsk1AJrFI/Fo6yaags8pSjo=','2024-01-20 10:12:08.864026',0,'usernew','','','',0,1,'2024-01-20 10:12:07.486361');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Sun Furnitures','0778673987','contact@sunfurnitures.com','890 Maple Road, Oldtown, State 34567'),(2,'ComfortCraft Furnishings','555 123-4567','info@comfortcraft.com','123 Main Street, Cityville, State 56789'),(3,'EliteLiving Designs','555 987-6543','contact@elitelivingdesigns.com','456 Oak Avenue, Townsville, State 12345'),(4,'ZenHaven Furnishings','(555) 789-0123','info@zenhavenfurniture.com','789 Serenity Lane, Tranquility City, State 67890'),(5,'UrbanStyle Creations','(555) 234-5678','hello@urbanstylecreations.com','567 Metro Plaza, Cityscape, State 23456');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(13,'CRM','customer'),(14,'CRM','supplier'),(12,'Inventory','productinventory'),(15,'Inventory','productrawmaterial'),(8,'Inventory','rawmaterial'),(10,'Inventory','rawmaterialinventory'),(9,'Inventory','warehouse'),(7,'Production','product'),(11,'Production','productionorder'),(16,'PurchaseOrder','purchaseorder'),(17,'SalesOrder','salesorder'),(18,'SalesOrder','salesorderitem'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'Inventory','0001_initial','2023-12-30 07:30:52.300608'),(2,'Production','0001_initial','2023-12-30 07:30:52.329800'),(3,'contenttypes','0001_initial','2023-12-30 07:30:52.390455'),(4,'auth','0001_initial','2023-12-30 07:30:52.825430'),(5,'admin','0001_initial','2023-12-30 07:30:52.945349'),(6,'admin','0002_logentry_remove_auto_add','2023-12-30 07:30:52.959342'),(7,'admin','0003_logentry_add_action_flag_choices','2023-12-30 07:30:52.973279'),(8,'contenttypes','0002_remove_content_type_name','2023-12-30 07:30:53.123401'),(9,'auth','0002_alter_permission_name_max_length','2023-12-30 07:30:53.208699'),(10,'auth','0003_alter_user_email_max_length','2023-12-30 07:30:53.248590'),(11,'auth','0004_alter_user_username_opts','2023-12-30 07:30:53.263854'),(12,'auth','0005_alter_user_last_login_null','2023-12-30 07:30:53.316969'),(13,'auth','0006_require_contenttypes_0002','2023-12-30 07:30:53.322951'),(14,'auth','0007_alter_validators_add_error_messages','2023-12-30 07:30:53.337829'),(15,'auth','0008_alter_user_username_max_length','2023-12-30 07:30:53.398294'),(16,'auth','0009_alter_user_last_name_max_length','2023-12-30 07:30:53.460862'),(17,'auth','0010_alter_group_name_max_length','2023-12-30 07:30:53.491360'),(18,'auth','0011_update_proxy_permissions','2023-12-30 07:30:53.510414'),(19,'auth','0012_alter_user_first_name_max_length','2023-12-30 07:30:53.572737'),(20,'sessions','0001_initial','2023-12-30 07:30:53.609534'),(21,'Inventory','0002_rawmaterial_cost','2023-12-31 03:33:36.994464'),(22,'Production','0002_remove_product_product_code_productionorder','2023-12-31 08:32:30.357517'),(23,'Inventory','0003_rename_quantity_rawmaterialinventory_quantity_on_hand_and_more','2023-12-31 08:32:30.778574'),(24,'CRM','0001_initial','2023-12-31 08:51:54.842162'),(25,'Inventory','0004_productrawmaterial','2024-01-01 04:01:08.293931'),(26,'PurchaseOrder','0001_initial','2024-01-01 11:06:54.085106'),(27,'Inventory','0005_alter_rawmaterialinventory_last_updated','2024-01-01 12:01:20.565705'),(28,'PurchaseOrder','0002_alter_purchaseorder_delivery_date_and_more','2024-01-01 12:01:20.689259'),(29,'PurchaseOrder','0003_remove_purchaseorder_delivery_date_and_more','2024-01-02 14:39:53.660835'),(30,'SalesOrder','0001_initial','2024-01-02 15:26:46.006873'),(31,'SalesOrder','0002_remove_salesorder_product_remove_salesorder_quantity_and_more','2024-01-02 15:35:52.424069'),(32,'SalesOrder','0003_alter_salesorder_order_date_and_more','2024-01-06 09:51:57.990602'),(33,'Production','0003_alter_productionorder_end_date_and_more','2024-01-07 04:56:29.434214'),(34,'Production','0004_remove_product_quantity_in_stock','2024-01-07 11:59:32.189348'),(35,'Production','0005_remove_productionorder_order_date','2024-01-07 12:07:29.888559');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` bigint NOT NULL AUTO_INCREMENT,
  `product_name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (10,'Wooden Chair','1st Product',100.00),(11,'Metal Desk','2nd Product',5000.00),(12,'Small Chair','dd',5000.00);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_inventory`
--

DROP TABLE IF EXISTS `product_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_inventory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_on_hand` int NOT NULL,
  `last_updated` datetime(6) NOT NULL,
  `product_id` bigint NOT NULL,
  `warehouse_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_inventory_product_id_fbab5ec7_fk_product_product_id` (`product_id`),
  KEY `product_inventory_warehouse_id_78b2a388_fk_warehouse` (`warehouse_id`),
  CONSTRAINT `product_inventory_product_id_fbab5ec7_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  CONSTRAINT `product_inventory_warehouse_id_78b2a388_fk_warehouse` FOREIGN KEY (`warehouse_id`) REFERENCES `warehouse` (`warehouse_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_inventory`
--

LOCK TABLES `product_inventory` WRITE;
/*!40000 ALTER TABLE `product_inventory` DISABLE KEYS */;
INSERT INTO `product_inventory` VALUES (1,155,'2024-01-22 02:26:30.958405',10,3),(2,30,'2024-01-07 12:08:07.452181',11,3);
/*!40000 ALTER TABLE `product_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_raw_material`
--

DROP TABLE IF EXISTS `product_raw_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_raw_material` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_required` int unsigned NOT NULL,
  `product_id` bigint NOT NULL,
  `raw_material_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_raw_material_product_id_raw_material_id_879fa513_uniq` (`product_id`,`raw_material_id`),
  KEY `product_raw_material_raw_material_id_c708b1c1_fk_raw_mater` (`raw_material_id`),
  CONSTRAINT `product_raw_material_product_id_144ae73f_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`),
  CONSTRAINT `product_raw_material_raw_material_id_c708b1c1_fk_raw_mater` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`raw_material_id`),
  CONSTRAINT `product_raw_material_chk_1` CHECK ((`quantity_required` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_raw_material`
--

LOCK TABLES `product_raw_material` WRITE;
/*!40000 ALTER TABLE `product_raw_material` DISABLE KEYS */;
INSERT INTO `product_raw_material` VALUES (11,5,10,1),(12,1,10,2),(13,5,11,1),(14,100,11,2),(15,11,12,1),(16,11,12,3);
/*!40000 ALTER TABLE `product_raw_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `production_order`
--

DROP TABLE IF EXISTS `production_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `production_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `production_order_product_id_110e5f6b_fk_product_product_id` (`product_id`),
  CONSTRAINT `production_order_product_id_110e5f6b_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `production_order`
--

LOCK TABLES `production_order` WRITE;
/*!40000 ALTER TABLE `production_order` DISABLE KEYS */;
INSERT INTO `production_order` VALUES (16,100,'2024-01-02','2024-01-09',10),(17,100,'2024-01-02','2024-01-09',10),(18,10,'2024-01-06','2024-01-13',11),(19,10,'2024-01-07','2024-01-14',10),(20,10,'2024-01-07','2024-01-14',11),(21,10,'2024-01-07','2024-01-14',10),(22,10,'2024-01-07','2024-01-14',11),(23,10,'2024-01-07','2024-01-09',11);
/*!40000 ALTER TABLE `production_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_order`
--

DROP TABLE IF EXISTS `purchase_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_order` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `quantity` int unsigned NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `raw_material_id` int NOT NULL,
  `supplier_id` bigint NOT NULL,
  `warehouse_id` int NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `purchase_order_raw_material_id_c9578962_fk_raw_mater` (`raw_material_id`),
  KEY `purchase_order_supplier_id_f3ce40ee_fk_supplier_id` (`supplier_id`),
  KEY `purchase_order_warehouse_id_2bb9b357_fk_warehouse_warehouse_id` (`warehouse_id`),
  CONSTRAINT `purchase_order_raw_material_id_c9578962_fk_raw_mater` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`raw_material_id`),
  CONSTRAINT `purchase_order_supplier_id_f3ce40ee_fk_supplier_id` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`),
  CONSTRAINT `purchase_order_warehouse_id_2bb9b357_fk_warehouse_warehouse_id` FOREIGN KEY (`warehouse_id`) REFERENCES `warehouse` (`warehouse_id`),
  CONSTRAINT `purchase_order_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_order`
--

LOCK TABLES `purchase_order` WRITE;
/*!40000 ALTER TABLE `purchase_order` DISABLE KEYS */;
INSERT INTO `purchase_order` VALUES (5,'2024-01-02',1000,50000.00,1,1,3),(6,'2024-01-02',5000,100000.00,2,1,3),(7,'2024-01-02',5000,10000.00,2,1,3),(8,'2024-01-02',1000,100000.00,1,1,3),(9,'2024-01-02',10000,1000000.00,2,1,3);
/*!40000 ALTER TABLE `purchase_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_material`
--

DROP TABLE IF EXISTS `raw_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `raw_material` (
  `raw_material_id` int NOT NULL AUTO_INCREMENT,
  `material_name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `cost` decimal(12,2) NOT NULL,
  PRIMARY KEY (`raw_material_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_material`
--

LOCK TABLES `raw_material` WRITE;
/*!40000 ALTER TABLE `raw_material` DISABLE KEYS */;
INSERT INTO `raw_material` VALUES (1,'Screws','Screws that will be used for chair',50.00),(2,'Fabric','Fabric used for seat',200.00),(3,'Wood','Wood used for chairs and tables',1000.00);
/*!40000 ALTER TABLE `raw_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `raw_material_inventory`
--

DROP TABLE IF EXISTS `raw_material_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `raw_material_inventory` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity_on_hand` int unsigned NOT NULL,
  `last_updated` date NOT NULL,
  `unit_cost` decimal(10,2) NOT NULL,
  `total_cost` decimal(12,2) NOT NULL,
  `raw_material_id` int NOT NULL,
  `warehouse_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `raw_material_invento_raw_material_id_18f16cc7_fk_raw_mater` (`raw_material_id`),
  KEY `raw_material_invento_warehouse_id_c37f11bb_fk_warehouse` (`warehouse_id`),
  CONSTRAINT `raw_material_invento_raw_material_id_18f16cc7_fk_raw_mater` FOREIGN KEY (`raw_material_id`) REFERENCES `raw_material` (`raw_material_id`),
  CONSTRAINT `raw_material_invento_warehouse_id_c37f11bb_fk_warehouse` FOREIGN KEY (`warehouse_id`) REFERENCES `warehouse` (`warehouse_id`),
  CONSTRAINT `raw_material_inventory_quantity_on_hand_7643475d_check` CHECK ((`quantity_on_hand` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_material_inventory`
--

LOCK TABLES `raw_material_inventory` WRITE;
/*!40000 ALTER TABLE `raw_material_inventory` DISABLE KEYS */;
INSERT INTO `raw_material_inventory` VALUES (3,700,'2024-01-07',100.00,20000.00,1,3),(4,10780,'2024-01-07',100.00,588000.00,2,3),(5,0,'2024-01-02',0.00,0.00,1,4);
/*!40000 ALTER TABLE `raw_material_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_order`
--

DROP TABLE IF EXISTS `sales_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_date` date NOT NULL,
  `ship_date` date NOT NULL,
  `status` varchar(50) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `customer_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SalesOrder_salesorder_customer_id_4a6ca709_fk_customer_id` (`customer_id`),
  CONSTRAINT `SalesOrder_salesorder_customer_id_4a6ca709_fk_customer_id` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_order`
--

LOCK TABLES `sales_order` WRITE;
/*!40000 ALTER TABLE `sales_order` DISABLE KEYS */;
INSERT INTO `sales_order` VALUES (1,'2024-01-03','2024-01-04','shipped',10000.00,1),(2,'2024-01-06','2024-01-07','shipped',50000.00,1),(3,'2024-01-22','2024-01-23','pending',100000.00,2);
/*!40000 ALTER TABLE `sales_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_order_product`
--

DROP TABLE IF EXISTS `sales_order_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_order_product` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `total_price` decimal(10,2) NOT NULL,
  `order_id` bigint NOT NULL,
  `product_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sales_order_product_order_id_a1d07c3e_fk_sales_order_id` (`order_id`),
  KEY `sales_order_product_product_id_a064bca6_fk_product_product_id` (`product_id`),
  CONSTRAINT `sales_order_product_order_id_a1d07c3e_fk_sales_order_id` FOREIGN KEY (`order_id`) REFERENCES `sales_order` (`id`),
  CONSTRAINT `sales_order_product_product_id_a064bca6_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_order_product`
--

LOCK TABLES `sales_order_product` WRITE;
/*!40000 ALTER TABLE `sales_order_product` DISABLE KEYS */;
INSERT INTO `sales_order_product` VALUES (1,5,100.00,500.00,1,10),(2,10,100.00,1000.00,2,10),(3,10,5000.00,50000.00,2,11),(4,50,100.00,5000.00,3,10);
/*!40000 ALTER TABLE `sales_order_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `address` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Sunil Iron','011594307','suniliron@email.com','Colombo-10');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `warehouse_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  PRIMARY KEY (`warehouse_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
INSERT INTO `warehouse` VALUES (3,'Colombo Warehouse','Colombo'),(4,'Negombo Warehouse','Negombo');
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-22  8:00:07
