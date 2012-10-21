-- MySQL dump 10.13  Distrib 5.5.24, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: lakshya
-- ------------------------------------------------------
-- Server version	5.5.24-0ubuntu0.12.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_donation`
--

DROP TABLE IF EXISTS `accounts_donation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_donation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `date_of_donation` date NOT NULL,
  `donor_id` int(11) NOT NULL,
  `donation_fund_id` int(11) NOT NULL,
  `transacation_type` int(11) NOT NULL,
  `transaction_details` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_donation_2017d081` (`donor_id`),
  KEY `accounts_donation_ce239fc1` (`donation_fund_id`),
  CONSTRAINT `donation_fund_id_refs_id_87a07cf4dcdc460` FOREIGN KEY (`donation_fund_id`) REFERENCES `accounts_donationfund` (`id`),
  CONSTRAINT `donor_id_refs_id_5f640f03cb6992a9` FOREIGN KEY (`donor_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_donation`
--

LOCK TABLES `accounts_donation` WRITE;
/*!40000 ALTER TABLE `accounts_donation` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_donation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_donationfund`
--

DROP TABLE IF EXISTS `accounts_donationfund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_donationfund` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_donationfund`
--

LOCK TABLES `accounts_donationfund` WRITE;
/*!40000 ALTER TABLE `accounts_donationfund` DISABLE KEYS */;
INSERT INTO `accounts_donationfund` VALUES (1,'Trahi Foundation','<p>Trahi Foundation is an organization formed by the 1993 batch NITW alumni and is based in Bangalore.</p>\r\n'),(2,'NITW Americas Alumni Chapter','<p>The NITW Americas Alumni Chapter is a tax exempt organization under IRS Code Section 501 (c)(3) set up by the NITW alumni in the United States in 1999.</p>'),(3,'NITW Alumni Middle East Chapter','<p>The NITW Alumni Middle East Chapter connects alumni from Western Asia and parts of North Africa.</p>'),(4,'Tom Zacharia Foundation','<p>Tom Zacharia foundation was established on 17 December 2010 by Tom\'s family. The key objective of the foundation is to keep the memory of Tom alive by supporting the values he held close to his heart - brilliance in your work, giving back to society, forging friendships across race and religion, and loving with a fire.<br/>\r\nThe foundation aspires to achieve the following:<br/>\r\n<ul>\r\n<li>Support those who wish to pursue a professional career in science or engineering but do not have the means to do so.</li>\r\n<li>Provide financial support and or scholarships to deserving children.</li>\r\n<li>Provide support to other foundations / institutions that propagate and/or stand for above described causes.</li></ul>\r\nThe foundation is primarily funded by the family. Secondary funding comes from royalties of the book \"Live Like Tom\" being published by Bency and Zac Thomas.</p>'),(5,'BVS Murthy 1979-83 NITW Alumni Scholarship','<p>The NITW Class of 1979-83 established this scholarship in memory of their deceased batchmate, Mr.B.V.S.Murty.</p>'),(6,'K Srikant Murty 1979-83 NITW Alumni Scholarship','<p>The NITW Class of 1979-83 established this scholarship in memory of their deceased batchmate, Mr.K. Srikant Murty.</p>'),(7,'Jyothirmoy Das 1979-83 NITW Alumni Scholarship','<p>The NITW Class of 1979-83 established this scholarship in memory of their deceased batchmate, Mr. Jyothirmoy Das.</p>'),(8,'Mr. Narayan','<p>Mr.Narayan is from the NITW Class of 1983 and graduated with a undergraduate degree in Electronics and Communication Engineering.</p>'),(9,'Mr. Prabhakar Puvvada','<p>Mr. Prabhakar Puvvada is from the NITW Class of 1980 and graduated with a undergraduate degree in Electrical and Electronics Engineering.</p>'),(10,'Mr. Vasant Roy','<p>Mr.Vasant Roy is from the NITW Class of 198o and graduated with a undergraduate degree in Mechanical Engineering.</p>');
/*!40000 ALTER TABLE `accounts_donationfund` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_expense`
--

DROP TABLE IF EXISTS `accounts_expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_expense` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `date_of_expense` date NOT NULL,
  `date_of_entry` date NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  `expense_header_first_level` int(11) NOT NULL,
  `expense_header_second_level` int(11) NOT NULL,
  `scan_bill` varchar(100) NOT NULL,
  `details` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_expense`
--

LOCK TABLES `accounts_expense` WRITE;
/*!40000 ALTER TABLE `accounts_expense` DISABLE KEYS */;
INSERT INTO `accounts_expense` VALUES (1,4500.00,'2009-02-10','2012-10-20',1,1,2,'','cheque no:239573, paid to Chief Warden '),(2,4500.00,'2009-02-10','2012-10-20',1,1,2,'','Cheque no:239572 in the name of Chief Warden'),(3,4500.00,'2009-02-19','2012-10-20',1,1,2,'','cheque no.239571 in the name of chief warden'),(4,1500.00,'2009-03-04','2012-10-20',1,1,2,'','cheque no:239576 in the name of Chief Warden'),(5,4500.00,'2009-03-05','2012-10-20',1,1,2,'','Cheque no.239574 in the name of Chief Warden'),(6,4500.00,'2009-03-06','2012-10-20',1,1,2,'','cheque no.239575 in the name of Chief Warden'),(7,10000.00,'2009-09-08','2012-10-20',1,1,2,'','Cheque no.239579 in the name of Director'),(8,10000.00,'2009-09-29','2012-10-20',1,1,2,'','Cheque no.239583 in the name of Director'),(9,10000.00,'2009-09-29','2012-10-20',1,1,2,'','Cheque no.239584 in the name of NIT'),(10,10000.00,'2009-09-29','2012-10-20',1,1,2,'','Cheque no.239585 in the name of Director'),(11,6000.00,'2009-10-13','2012-10-20',1,1,2,'','Cheque no.239589 in the name of Director'),(12,9000.00,'2009-10-13','2012-10-20',1,1,2,'','Cheque no.239587 in the name of Director'),(13,6000.00,'2009-10-13','2012-10-20',1,1,2,'','Cheque no.239588 in the name of Director.'),(14,9000.00,'2009-11-07','2012-10-20',1,1,2,'','Cheque no.239586 in the name of Director'),(15,6200.00,'2010-01-27','2012-10-20',1,1,2,'','Cheque no.239599 in the name of Director.'),(16,6200.00,'2010-01-27','2012-10-20',1,1,2,'','Cheque no.239598 in the name of Director.'),(17,6200.00,'2010-01-27','2012-10-20',1,1,2,'','Cheque no.239597 in the name of Director.'),(18,6900.00,'2010-01-27','2012-10-20',1,1,2,'','Cheque no.239596 in the name of Director.'),(19,20000.00,'2010-07-28','2012-10-20',1,1,2,'','Cheque no.165796 in the name of Warden'),(20,78500.00,'2010-11-30','2012-10-20',1,1,2,'','Cheque no.165798 in the name of Director.'),(21,35000.00,'2010-12-08','2012-10-20',1,1,2,'','Cheque no.165800 in the name of Director'),(22,18000.00,'2010-12-08','2012-10-20',1,1,2,'','Cheque no.165799 in the name of Director.'),(23,6250.00,'2011-01-27','2012-10-20',1,1,2,'','Cheque no.322685 in the name of Director.'),(24,6250.00,'2011-01-27','2012-10-20',1,1,2,'','Cheque no.322684 in the name of Director.'),(25,6250.00,'2011-01-27','2012-10-20',1,1,2,'','Cheque no.322687 in the name of Director.'),(26,6250.00,'2011-01-27','2012-10-20',1,1,2,'','Cheque no.322689 in the name of Director.'),(27,6250.00,'2011-01-29','2012-10-20',1,1,2,'','Cheque no.322686 in the name of Director.'),(28,17500.00,'2011-01-29','2012-10-20',1,1,2,'','Cheque no.322688 in the name of Director.'),(29,17500.00,'2011-01-29','2012-10-20',1,1,2,'','Cheque no.322688 in the name of Director.'),(30,6950.00,'2011-01-31','2012-10-20',1,1,2,'','Cheque no.322682 in the name of Director.'),(31,6950.00,'2011-02-01','2012-10-20',1,1,2,'','Cheque no.322683 in the name of Director.'),(32,4000.00,'2011-03-11','2012-10-20',1,1,2,'','Cheque no.322690 in the name of Director.'),(33,3000.00,'2011-07-30','2012-10-20',1,1,2,'','Cheque no.378575 in the name of Chief Warden.'),(34,3000.00,'2011-07-30','2012-10-20',1,1,2,'','Cheque no.378575 in the name of Chief Warden.'),(35,3000.00,'2011-07-30','2012-10-20',1,1,2,'','Cheque no.378588 in the name of Chief Warden.'),(36,3000.00,'2011-07-30','2012-10-20',1,1,2,'','Cheque no.378590 in the name of Chief Warden.'),(37,3000.00,'2011-07-30','2012-10-20',1,1,2,'','Cheque no.378592 in the name of Chief Warden.'),(38,3000.00,'2011-07-30','2012-10-20',1,1,2,'','Cheque no.378586 in the name of Chief Warden.'),(39,4000.00,'2011-08-02','2012-10-20',1,1,2,'','Cheque no.378579 in the name of Chief Warden.'),(40,4000.00,'2011-08-02','2012-10-20',1,1,2,'','Cheque no.378571 in the name of Chief Warden.'),(41,4000.00,'2011-08-02','2012-10-20',1,1,2,'','Cheque no.322693 in the name of Chief Warden.'),(42,4000.00,'2011-08-02','2012-10-20',1,1,2,'','Cheque no.378595 in the name of Chief Warden.'),(43,18000.00,'2011-08-04','2012-10-20',1,1,2,'','Cheque no.322695 in the name of Director.'),(44,8000.00,'2011-08-08','2012-10-20',1,1,2,'','Cheque no.322694 in the name of Director.'),(45,10000.00,'2011-08-08','2012-10-20',1,1,2,'','Cheque no.322692 in the name of Director.'),(46,4000.00,'2011-08-08','2012-10-20',1,1,2,'','Cheque no.378573 in the name of Chief Warden.'),(47,4000.00,'2011-08-09','2012-10-20',1,1,2,'','Cheque no.378584in the name of Chief Warden.'),(48,4000.00,'2011-08-19','2012-10-20',1,1,2,'','Cheque no.378597 in the name of Chief Warden.'),(49,4000.00,'2011-08-19','2012-10-20',1,1,2,'','Cheque no.378577 in the name of Chief Warden.'),(50,18000.00,'2011-08-25','2012-10-20',1,1,2,'','Cheque no.378596 in the name of Director.'),(51,26500.00,'2011-08-26','2012-10-20',1,1,2,'','Cheque no.378591 in the name of Director.'),(52,17000.00,'2011-08-26','2012-10-20',1,1,2,'','Cheque no.378580 in the name of Director.'),(53,18000.00,'2011-08-30','2012-10-20',1,1,2,'','Cheque no.378594 in the name of Director.'),(54,29500.00,'2011-08-30','2012-10-20',1,1,2,'','Cheque no.378583 in the name of Director.'),(55,18000.00,'2011-08-30','2012-10-20',1,1,2,'','Cheque no.378578 in the name of Director.'),(56,10000.00,'2011-09-24','2012-10-20',1,3,5,'','Cheque no.378600 in the name of T Viswarath.'),(57,26500.00,'2011-10-05','2012-10-20',1,1,2,'','Cheque no.378585 in the name of Director.'),(58,3000.00,'2011-11-18','2012-10-20',1,1,2,'','Cheque no.378581 in the name of Chief Warden.'),(59,10000.00,'2011-11-19','2012-10-20',1,3,5,'','Cheque no.2281 in the name of Deepinka Agarwal.'),(60,7317.00,'2011-11-21','2012-10-20',1,2,4,'','Cheque no.2282 in the name of Joby.'),(61,16500.00,'2012-01-27','2012-10-20',1,1,2,'','Cheque no.2283 in the name of Director.'),(62,250.00,'2012-01-27','2012-10-20',0,1,2,'','Cheque no.2284 in the name of Director.'),(63,7660.00,'2012-02-03','2012-10-20',1,2,4,'','Cheque no.2285 in the name of JOBY.'),(64,6650.00,'2012-05-23','2012-10-20',1,0,4,'','Cheque no.2288 in the name of P Satish.'),(65,1242.00,'2012-05-24','2012-10-20',1,0,4,'','Cheque no.2291 in the name of Anand Rajagopal.'),(66,6220.00,'2012-05-24','2012-10-20',1,0,4,'','Cheque no.2290 in the name of Anand Rajagopal.'),(67,3978.00,'2012-05-29','2012-10-20',1,2,4,'','Cheque no.2289 in the name of JOBY.'),(68,26500.00,'2012-06-01','2012-10-20',1,1,2,'','Cheque no.2293in the name of Director.'),(69,26500.00,'2012-06-01','2012-10-20',1,1,2,'','Cheque no.2292 in the name of Director.'),(70,8500.00,'2012-06-14','2012-10-20',1,4,3,'','Cheque no.2294 in the name of TALWAR ADVOCATES.'),(71,5000.00,'2012-08-02','2012-10-20',1,1,2,'','Cheque no.2301 in the name of Chief Warden.'),(72,5000.00,'2012-08-11','2012-10-20',1,1,2,'','Cheque no.2303 in the name of Chief Warden.'),(73,5000.00,'2012-08-11','2012-10-20',1,1,2,'','Cheque no.2304 in the name of Chief Warden.'),(74,5000.00,'2012-08-11','2012-10-20',1,1,2,'','Cheque no.2305 in the name of Chief Warden.'),(75,20000.00,'2012-08-24','2012-10-20',0,4,5,'','Cheque no.52246 in the name of Anand Rajagopalan.'),(76,5000.00,'2012-08-24','2012-10-20',1,1,2,'','Cheque no.2302 in the name of Chief Warden.'),(77,10000.00,'2012-08-29','2012-10-20',1,2,4,'','Cheque no.52248 in the name of Abhiram.'),(78,2500.00,'2012-08-29','2012-10-20',1,2,4,'','Cheque no.52247 in the name of Abhiram.'),(79,30000.00,'2012-08-31','2012-10-20',1,1,2,'','Cheque no.2296 in the name of Director'),(80,30000.00,'2012-08-31','2012-10-20',1,1,2,'','Cheque no.2297 in the name of Director.'),(81,30000.00,'2012-08-31','2012-10-20',1,1,2,'','Cheque no.2298 in the name of Director.'),(82,2500.00,'2012-07-06','2012-10-20',1,2,4,'','Cheque no.2286 in the name of C.Sumanth Reddy.'),(83,20000.00,'2012-06-22','2012-10-20',1,0,4,'','Cheque no.2295 in the name of SRI MANOHAR SINGH TAKHUR.'),(84,26500.00,'2011-09-23','2012-10-20',1,1,2,'','Cheque no.378587 in the name of NIT.'),(85,12683.00,'2011-08-17','2012-10-20',1,2,4,'','Cheque no.378599 in the name of SRI JOBY .'),(86,29500.00,'2011-08-12','2012-10-20',1,1,2,'','Cheque no.378576 in the name of Director.'),(87,29500.00,'2011-08-12','2012-10-20',1,1,2,'','Cheque no.378572 in the name of Director.'),(88,3309.00,'2010-08-02','2012-10-20',1,4,3,'','Cheque no.322681 in the name of AKASAM Associates.'),(89,3309.00,'2011-04-26','2012-10-20',1,4,3,'','Cheque no.322691 in the name of AKASAM Associates.'),(90,3309.00,'2011-08-02','2012-10-20',1,4,3,'','Cheque no.378598 in the name of AKASAM Associates.'),(91,110.00,'2010-07-14','2012-10-20',1,4,4,'','Charges for Cheque Book Issue'),(92,55.00,'2009-03-04','2012-10-20',1,4,4,'','Bank Charges'),(93,55.00,'2009-04-25','2012-10-20',1,4,4,'','Bank Charges');
/*!40000 ALTER TABLE `accounts_expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_paymenttemp`
--

DROP TABLE IF EXISTS `accounts_paymenttemp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_paymenttemp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email_address` varchar(75) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `email_receipt` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_paymenttemp`
--

LOCK TABLES `accounts_paymenttemp` WRITE;
/*!40000 ALTER TABLE `accounts_paymenttemp` DISABLE KEYS */;
INSERT INTO `accounts_paymenttemp` VALUES (1,'mahesh.gitta@gmail.com',20.00,1),(2,'mahesh.gitta@gmail.com',20.00,1),(3,'anandr31@gmail.com',101.00,1);
/*!40000 ALTER TABLE `accounts_paymenttemp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=103 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add group',2,'add_group'),(2,'Can add permission',1,'add_permission'),(3,'Can add user',3,'add_user'),(4,'Can change group',2,'change_group'),(5,'Can change permission',1,'change_permission'),(6,'Can change user',3,'change_user'),(7,'Can delete group',2,'delete_group'),(8,'Can delete permission',1,'delete_permission'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add log entry',6,'add_logentry'),(17,'Can change log entry',6,'change_logentry'),(18,'Can delete log entry',6,'delete_logentry'),(19,'Can add migration history',7,'add_migrationhistory'),(20,'Can change migration history',7,'change_migrationhistory'),(21,'Can delete migration history',7,'delete_migrationhistory'),(22,'Can add person',8,'add_person'),(23,'Can add person_preference',9,'add_person_preference'),(24,'Can add team member',10,'add_teammember'),(25,'Can change person',8,'change_person'),(26,'Can change person_preference',9,'change_person_preference'),(27,'Can change team member',10,'change_teammember'),(28,'Can delete person',8,'delete_person'),(29,'Can delete person_preference',9,'delete_person_preference'),(30,'Can delete team member',10,'delete_teammember'),(31,'Can add Donation Fund',12,'add_donationfund'),(32,'Can add donation',13,'add_donation'),(33,'Can add expense',11,'add_expense'),(34,'Can change Donation Fund',12,'change_donationfund'),(35,'Can change donation',13,'change_donation'),(36,'Can change expense',11,'change_expense'),(37,'Can delete Donation Fund',12,'delete_donationfund'),(38,'Can delete donation',13,'delete_donation'),(39,'Can delete expense',11,'delete_expense'),(40,'Can add innovation',15,'add_innovation'),(41,'Can add innovation application',14,'add_innovationapplication'),(42,'Can add innovation payment',19,'add_innovationpayment'),(43,'Can add innovation update',16,'add_innovationupdate'),(44,'Can add innovation update image',17,'add_innovationupdateimage'),(45,'Can add innovation update video',18,'add_innovationupdatevideo'),(46,'Can change innovation',15,'change_innovation'),(47,'Can change innovation application',14,'change_innovationapplication'),(48,'Can change innovation payment',19,'change_innovationpayment'),(49,'Can change innovation update',16,'change_innovationupdate'),(50,'Can change innovation update image',17,'change_innovationupdateimage'),(51,'Can change innovation update video',18,'change_innovationupdatevideo'),(52,'Can delete innovation',15,'delete_innovation'),(53,'Can delete innovation application',14,'delete_innovationapplication'),(54,'Can delete innovation payment',19,'delete_innovationpayment'),(55,'Can delete innovation update',16,'delete_innovationupdate'),(56,'Can delete innovation update image',17,'delete_innovationupdateimage'),(57,'Can delete innovation update video',18,'delete_innovationupdatevideo'),(58,'Can add family detail',23,'add_familydetail'),(59,'Can add grade update',30,'add_gradeupdate'),(60,'Can add other exam performance',22,'add_otherexamperformance'),(61,'Can add other scholarship',24,'add_otherscholarship'),(62,'Can add repayment',31,'add_repayment'),(63,'Can add scholar',26,'add_scholar'),(64,'Can add scholar academic update',29,'add_scholaracademicupdate'),(65,'Can add scholar update',28,'add_scholarupdate'),(66,'Can add scholarship application',20,'add_scholarshipapplication'),(67,'Can add scholarship payment',27,'add_scholarshippayment'),(68,'Can add scholarship verification',25,'add_scholarshipverification'),(69,'Can add sgpa',21,'add_sgpa'),(70,'Can change family detail',23,'change_familydetail'),(71,'Can change grade update',30,'change_gradeupdate'),(72,'Can change other exam performance',22,'change_otherexamperformance'),(73,'Can change other scholarship',24,'change_otherscholarship'),(74,'Can change repayment',31,'change_repayment'),(75,'Can change scholar',26,'change_scholar'),(76,'Can change scholar academic update',29,'change_scholaracademicupdate'),(77,'Can change scholar update',28,'change_scholarupdate'),(78,'Can change scholarship application',20,'change_scholarshipapplication'),(79,'Can change scholarship payment',27,'change_scholarshippayment'),(80,'Can change scholarship verification',25,'change_scholarshipverification'),(81,'Can change sgpa',21,'change_sgpa'),(82,'Can delete family detail',23,'delete_familydetail'),(83,'Can delete grade update',30,'delete_gradeupdate'),(84,'Can delete other exam performance',22,'delete_otherexamperformance'),(85,'Can delete other scholarship',24,'delete_otherscholarship'),(86,'Can delete repayment',31,'delete_repayment'),(87,'Can delete scholar',26,'delete_scholar'),(88,'Can delete scholar academic update',29,'delete_scholaracademicupdate'),(89,'Can delete scholar update',28,'delete_scholarupdate'),(90,'Can delete scholarship application',20,'delete_scholarshipapplication'),(91,'Can delete scholarship payment',27,'delete_scholarshippayment'),(92,'Can delete scholarship verification',25,'delete_scholarshipverification'),(93,'Can delete sgpa',21,'delete_sgpa'),(94,'Can add lakshya update',32,'add_lakshyaupdate'),(95,'Can add lakskhya testimonial',33,'add_lakskhyatestimonial'),(96,'Can change lakshya update',32,'change_lakshyaupdate'),(97,'Can change lakskhya testimonial',33,'change_lakskhyatestimonial'),(98,'Can delete lakshya update',32,'delete_lakshyaupdate'),(99,'Can delete lakskhya testimonial',33,'delete_lakskhyatestimonial'),(100,'Can add payment temp',34,'add_paymenttemp'),(101,'Can change payment temp',34,'change_paymenttemp'),(102,'Can delete payment temp',34,'delete_paymenttemp');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'lakshya','','','sriharimaneru@gmail.com','pbkdf2_sha256$10000$kykIMNScgAQK$IuNHF818m4V6YjDm/8SsBkgx4ZPAamtlnk5sQ565jx8=',1,1,1,'2012-10-14 13:45:15','2012-09-20 11:21:00'),(2,'mesrijareddy@gmail.com','Srija','Reddy','mesrijareddy@gmail.com','pbkdf2_sha256$10000$TqhmkJR8UFcz$lLs6haw0nsIskasY4nooI38Jb1N8x4dx3GpAbRc+VFc=',0,1,0,'2012-09-28 17:20:46','2012-09-28 17:20:46'),(3,'kiran.nitwarangal@gmail.com','Kiran Kumar','Avvaru','kiran.nitwarangal@gmail.com','pbkdf2_sha256$10000$S6PKLfMRpFPT$UE6icXJTBUxIdlUTzWdqk7poFz2Th8xDNpgJH95yv7g=',0,1,0,'2012-09-28 17:39:56','2012-09-28 17:39:56'),(4,'shekhar.shekhar.mintu@gmail.co','Shekhar','Suman','shekhar.shekhar.mintu@gmail.co','pbkdf2_sha256$10000$dxcjuurHE4PJ$vGxPSkNIPERs+igbe7B0B70rEnV/ZYN2x2J1YARzMUA=',0,1,0,'2012-09-28 17:41:16','2012-09-28 17:41:16'),(5,'vadiginatatarao@gmail.com','V Thata','Rao','vadiginatatarao@gmail.com','pbkdf2_sha256$10000$MvLtVhDK9dy9$FoK2aySgBu+i1cPddZapbY6RoV99PQkCwRqxHpg5A/A=',0,1,0,'2012-09-28 17:41:55','2012-09-28 17:41:55'),(6,'praveen.pravi08@gmail.com','Durgam Praveen','Kumar','praveen.pravi08@gmail.com','pbkdf2_sha256$10000$pNUHB2FDjkEe$N8/lvbX+AWR4hzH/RrqaAFxDkiBIQdouvg7LYpWhy1s=',0,1,0,'2012-09-28 17:42:31','2012-09-28 17:42:31'),(7,'gkgayathri1@gmail.com','Gayathri','Kaliyamoorhty','gkgayathri1@gmail.com','pbkdf2_sha256$10000$5Ms5rLhDFVe6$9YG8d/KwWZbhuyZTqbZ6u1kSHizmSuAGkqQAY3opJEE=',0,1,0,'2012-09-28 17:43:01','2012-09-28 17:43:01'),(8,'rajuponnala143@gmail.com','Raju','Ponnala','rajuponnala143@gmail.com','pbkdf2_sha256$10000$ONst26JQjdSt$1/6L3mab4xHK5k1VBAdLR0AUTjXgwanuJSQ5Hkq2DT0=',0,1,0,'2012-09-28 17:45:50','2012-09-28 17:45:50'),(9,'justjayaswal@gmail.com','Rajeev','Jayaswal','justjayaswal@gmail.com','pbkdf2_sha256$10000$V93423ZXqkAb$6UCkzUo002ynQcVuWWWbE+fGoo7JSR5CMLQNBujpHs0=',0,1,0,'2012-09-28 17:46:31','2012-09-28 17:46:31'),(10,'hcmg2489@gmail.com','Channa','Mallikarjuna','hcmg2489@gmail.com','pbkdf2_sha256$10000$9gbkdb4WHo8b$X7OQhSdom1j7aIJY+nRP00FAk8Xv82gZbVLSUDjJBKA=',0,1,0,'2012-09-28 17:47:03','2012-09-28 17:47:03'),(11,'ss51091@gmail.com','Suman','Srikanth','ss51091@gmail.com','pbkdf2_sha256$10000$2MpEmeHV73kV$91t5GHH/jTr/AIOn0t+VT72xNLObyj9LmfxWEsDUt+U=',0,1,0,'2012-09-28 17:48:04','2012-09-28 17:48:04'),(12,'mahesh.gitta@gmail.com','Mahesh','Gitta','mahesh.gitta@gmail.com','pbkdf2_sha256$10000$IP16S12XVIDO$zSIQFILR1QwspQ4n92KvYo1YXTfQV610xAha5RRkc1E=',0,1,0,'2012-09-28 17:50:36','2012-09-28 17:50:36'),(13,'rajafrnd2u@gmail.com','Rajesh','Vadlapatla','rajafrnd2u@gmail.com','pbkdf2_sha256$10000$77ywi2lDc7kk$WHYKyTnaL5kGWu+T33tCA3440HdKOxN7yCwGil367GA=',0,1,0,'2012-09-28 17:51:21','2012-09-28 17:51:21'),(14,'chaitanyasai03@gmail.com','Kedari','Chaitanya','chaitanyasai03@gmail.com','pbkdf2_sha256$10000$XCmvJeAZcUlp$ygCKJHrxjFFMb2ZMH+vaaoV5ERE8OGBdXE9dN/jxhTQ=',0,1,0,'2012-09-28 17:53:58','2012-09-28 17:53:58'),(15,'mastanvali.nitw@gmail.com','Mastan','Vali','mastanvali.nitw@gmail.com','pbkdf2_sha256$10000$VG6ASZUUgvEP$1s0sVmM14KOqkOemoQmG1rT6x8vAEnCj71N2LRmVXqM=',0,1,0,'2012-09-28 17:57:12','2012-09-28 17:57:12'),(16,'aadhi33@gmail.com','Aadinarayana','Reddy','aadhi33@gmail.com','pbkdf2_sha256$10000$3WnnW7Y46n3d$yHZ1BOq8qHkzCuWKHMLGiy5uWEfLnzsvnfj3/o8xlkE=',0,1,0,'2012-09-28 17:58:02','2012-09-28 17:58:02'),(17,'desmalanils48@gmail.com','Anil','Solanki','desmalanils48@gmail.com','pbkdf2_sha256$10000$jf3J5kO7gwZ8$L6d5bbpUAiYXns737wkThrNghZbUcGr+DH+4rdoKS84=',0,1,0,'2012-09-28 17:59:10','2012-09-28 17:59:10'),(18,'sandhyalalprateek2010@gmail.co','Sandhyalal','Kumar','sandhyalalprateek2010@gmail.co','pbkdf2_sha256$10000$BK5cgFq3GaVT$5rGwBiY0XFJKxnmbP5A1Pkhaps0jZfr9IhgOgdObpd0=',0,1,0,'2012-09-28 18:00:18','2012-09-28 18:00:18'),(19,'sonupdh@gmail.com','Rahul','Upadhyay','sonupdh@gmail.com','pbkdf2_sha256$10000$VQKdnke0ClFA$tLt6tyFdydttNuFOOtQFhTZKlvh+FBFzH+5xDuBcODg=',0,1,0,'2012-09-28 18:01:20','2012-09-28 18:01:20'),(20,'alkapil06raj@gmail.com','Kapil','Rakaj','alkapil06raj@gmail.com','pbkdf2_sha256$10000$6Zd7LMqiIw6v$FWGYL92gtTD69E0Ti91pRjTRntH6sClcnmrSLGj+LoQ=',0,1,0,'2012-09-28 18:03:05','2012-09-28 18:03:05'),(21,'adikiprakash@gmail.com','Adiki','Prakash','adikiprakash@gmail.com','pbkdf2_sha256$10000$qun11jZ3Lyi3$CZFgnpCPj8yBQPPpobQJFNp1plTcgfEf7JB8F/cbO+g=',0,1,0,'2012-09-28 18:03:53','2012-09-28 18:03:53'),(22,'ravitejabadisa@gmail.com','Ravi','Teja','ravitejabadisa@gmail.com','pbkdf2_sha256$10000$165zWlIxTEnJ$keu0vbQXuHaItLzuonX0BzUb7SSZchGCHytVGCX5D3I=',0,1,0,'2012-09-28 18:05:15','2012-09-28 18:05:15'),(23,'yetti.143@gmail.com','Singaraiah','Yetti','yetti.143@gmail.com','pbkdf2_sha256$10000$3gp3OVeKD1Ch$F7LyONt+2OEkjCTlL7h3+DCp7UwKMrDYB8PCIzKBAQ8=',0,1,0,'2012-09-28 18:07:07','2012-09-28 18:07:07');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=457 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2012-10-20 16:01:33',1,32,'1','LakshyaUpdate object',1,''),(2,'2012-10-20 16:01:33',1,32,'2','LakshyaUpdate object',1,''),(3,'2012-10-20 16:01:33',1,32,'3','LakshyaUpdate object',1,''),(4,'2012-10-20 16:01:33',1,10,'1','TeamMember object',1,''),(5,'2012-10-20 16:01:33',1,10,'1','TeamMember object',2,'Changed photo.'),(6,'2012-10-20 16:01:33',1,10,'1','TeamMember object',2,'Changed name, designation, description, fb_link, linkedin_link and twitter_link.'),(7,'2012-10-20 16:01:33',1,10,'1','TeamMember object',2,'Changed designation.'),(8,'2012-10-20 16:01:33',1,10,'1','TeamMember object',2,'Changed description.'),(9,'2012-10-20 16:01:33',1,10,'1','TeamMember object',2,'Changed description.'),(10,'2012-10-20 16:01:33',1,10,'1','TeamMember object',2,'No fields changed.'),(11,'2012-10-20 16:01:32',1,32,'3','LakshyaUpdate object',2,'Changed photo.'),(12,'2012-10-20 16:01:32',1,32,'4','LakshyaUpdate object',1,''),(13,'2012-10-20 16:01:32',1,32,'5','LakshyaUpdate object',1,''),(14,'2012-10-20 16:01:32',1,32,'6','LakshyaUpdate object',1,''),(15,'2012-10-20 16:01:32',1,32,'2','LakshyaUpdate object',2,'Changed photo.'),(16,'2012-10-20 16:01:32',1,32,'7','LakshyaUpdate object',1,''),(17,'2012-10-20 16:01:32',1,32,'4','LakshyaUpdate object',2,'Changed update_text.'),(18,'2012-10-20 16:01:32',1,32,'6','LakshyaUpdate object',2,'Changed update_text.'),(19,'2012-10-20 16:01:32',1,32,'6','LakshyaUpdate object',2,'Changed update_text.'),(20,'2012-10-20 16:01:32',1,11,'1','2009-02-10 : Rs.4500',1,''),(21,'2012-10-20 16:01:32',1,11,'2','2009-02-10 : Rs.4500',1,''),(22,'2012-10-20 16:01:32',1,11,'3','2009-02-19 : Rs.4500',1,''),(23,'2012-10-20 16:01:32',1,11,'4','2009-03-04 : Rs.1500',1,''),(24,'2012-10-20 16:01:32',1,11,'5','2009-03-05 : Rs.4500',1,''),(25,'2012-10-20 16:01:32',1,11,'6','2009-03-06 : Rs.4500',1,''),(26,'2012-10-20 16:01:32',1,11,'7','2009-09-08 : Rs.10000',1,''),(27,'2012-10-20 16:01:32',1,11,'8','2009-09-29 : Rs.10000',1,''),(28,'2012-10-20 16:01:32',1,11,'9','2009-09-29 : Rs.10000',1,''),(29,'2012-10-20 16:01:31',1,11,'10','2009-09-29 : Rs.10000',1,''),(30,'2012-10-20 16:01:31',1,11,'11','2009-10-13 : Rs.6000',1,''),(31,'2012-10-20 16:01:31',1,11,'12','2009-10-13 : Rs.9000',1,''),(32,'2012-10-20 16:01:31',1,11,'13','2009-10-13 : Rs.6000',1,''),(33,'2012-10-20 16:01:31',1,11,'14','2011-11-07 : Rs.9000',1,''),(34,'2012-10-20 16:01:31',1,11,'15','2010-01-27 : Rs.6200',1,''),(35,'2012-10-20 16:01:31',1,11,'16','2010-01-27 : Rs.6200',1,''),(36,'2012-10-20 16:01:31',1,11,'14','2009-11-07 : Rs.9000',2,'Changed date_of_expense.'),(37,'2012-10-20 16:01:31',1,11,'17','2010-01-27 : Rs.6200',1,''),(38,'2012-10-20 16:01:31',1,11,'18','2010-01-27 : Rs.6900',1,''),(39,'2012-10-20 16:01:31',1,11,'19','2010-07-28 : Rs.20000',1,''),(40,'2012-10-20 16:01:31',1,11,'20','2010-11-30 : Rs.78500',1,''),(41,'2012-10-20 16:01:31',1,11,'21','2010-12-08 : Rs.35000',1,''),(42,'2012-10-20 16:01:31',1,11,'22','2010-12-08 : Rs.18000',1,''),(43,'2012-10-20 16:01:31',1,11,'23','2011-01-27 : Rs.6250',1,''),(44,'2012-10-20 16:01:31',1,11,'24','2011-01-27 : Rs.6250',1,''),(45,'2012-10-20 16:01:31',1,11,'25','2011-01-27 : Rs.6250',1,''),(46,'2012-10-20 16:01:31',1,11,'26','2011-01-27 : Rs.6250',1,''),(47,'2012-10-20 16:01:31',1,11,'27','2011-01-29 : Rs.6250',1,''),(48,'2012-10-20 16:01:31',1,11,'28','2011-01-29 : Rs.17500',1,''),(49,'2012-10-20 16:01:31',1,11,'29','2011-01-29 : Rs.17500',1,''),(50,'2012-10-20 16:01:31',1,11,'30','2011-01-31 : Rs.6950',1,''),(51,'2012-10-20 16:01:30',1,11,'31','2011-02-01 : Rs.6950',1,''),(52,'2012-10-20 16:01:30',1,11,'32','2011-03-11 : Rs.4000',1,''),(53,'2012-10-20 16:01:30',1,11,'33','2011-07-30 : Rs.3000',1,''),(54,'2012-10-20 16:01:30',1,11,'34','2011-07-30 : Rs.3000',1,''),(55,'2012-10-20 16:01:30',1,11,'35','2011-07-30 : Rs.3000',1,''),(56,'2012-10-20 16:01:30',1,11,'36','2011-07-30 : Rs.3000',1,''),(57,'2012-10-20 16:01:30',1,11,'37','2011-07-30 : Rs.3000',1,''),(58,'2012-10-20 16:01:30',1,11,'38','2011-07-30 : Rs.300',1,''),(59,'2012-10-20 16:01:30',1,11,'38','2011-07-30 : Rs.3000',2,'Changed amount.'),(60,'2012-10-20 16:01:30',1,11,'39','2011-08-02 : Rs.4000',1,''),(61,'2012-10-20 16:01:30',1,11,'39','2011-08-02 : Rs.4000',2,'No fields changed.'),(62,'2012-10-20 16:01:30',1,11,'40','2011-08-02 : Rs.4000',1,''),(63,'2012-10-20 16:01:30',1,11,'41','2011-08-02 : Rs.4000',1,''),(64,'2012-10-20 16:01:30',1,11,'42','2011-08-02 : Rs.4000',1,''),(65,'2012-10-20 16:01:30',1,11,'43','2011-08-04 : Rs.18000',1,''),(66,'2012-10-20 16:01:30',1,11,'41','2011-08-02 : Rs.4000',2,'Changed details.'),(67,'2012-10-20 16:01:30',1,11,'44','2011-08-08 : Rs.8000',1,''),(68,'2012-10-20 16:01:30',1,11,'43','2011-08-04 : Rs.18000',2,'Changed details.'),(69,'2012-10-20 16:01:30',1,11,'44','2011-08-08 : Rs.8000',2,'Changed status.'),(70,'2012-10-20 16:01:30',1,11,'45','2011-08-08 : Rs.10000',1,''),(71,'2012-10-20 16:01:30',1,11,'46','2011-08-08 : Rs.4000',1,''),(72,'2012-10-20 16:01:30',1,11,'47','2011-08-09 : Rs.4000',1,''),(73,'2012-10-20 16:01:30',1,11,'48','2011-08-19 : Rs.4000',1,''),(74,'2012-10-20 16:01:29',1,11,'49','2011-08-19 : Rs.4000',1,''),(75,'2012-10-20 16:01:29',1,11,'50','2011-08-25 : Rs.18000',1,''),(76,'2012-10-20 16:01:29',1,11,'51','2011-08-26 : Rs.26500',1,''),(77,'2012-10-20 16:01:29',1,11,'52','2011-08-26 : Rs.17000',1,''),(78,'2012-10-20 16:01:29',1,11,'53','2011-08-30 : Rs.18000',1,''),(79,'2012-10-20 16:01:29',1,11,'54','2011-08-30 : Rs.29500',1,''),(80,'2012-10-20 16:01:29',1,11,'55','2011-08-30 : Rs.18000',1,''),(81,'2012-10-20 16:01:29',1,11,'56','2011-09-24 : Rs.10000',1,''),(82,'2012-10-20 16:01:29',1,11,'55','2011-08-30 : Rs.18000',2,'Changed details.'),(83,'2012-10-20 16:01:29',1,11,'50','2011-08-25 : Rs.18000',2,'No fields changed.'),(84,'2012-10-20 16:01:29',1,11,'51','2011-08-26 : Rs.26500',2,'Changed details.'),(85,'2012-10-20 16:01:29',1,11,'52','2011-08-26 : Rs.17000',2,'Changed details.'),(86,'2012-10-20 16:01:29',1,11,'53','2011-08-30 : Rs.18000',2,'Changed details.'),(87,'2012-10-20 16:01:29',1,11,'52','2011-08-26 : Rs.17000',2,'No fields changed.'),(88,'2012-10-20 16:01:28',1,11,'54','2011-08-30 : Rs.29500',2,'Changed details.'),(89,'2012-10-20 16:01:28',1,11,'55','2011-08-30 : Rs.18000',2,'No fields changed.'),(90,'2012-10-20 16:01:28',1,11,'57','2011-10-05 : Rs.26500',1,''),(91,'2012-10-20 16:01:28',1,11,'58','2011-11-18 : Rs.3000',1,''),(92,'2012-10-20 16:01:28',1,11,'59','2011-11-19 : Rs.10000',1,''),(93,'2012-10-20 16:01:28',1,11,'60','2011-11-21 : Rs.7317',1,''),(94,'2012-10-20 16:01:28',1,11,'61','2012-01-27 : Rs.16500',1,''),(95,'2012-10-20 16:01:28',1,11,'62','2012-01-27 : Rs.250',1,''),(96,'2012-10-20 16:01:28',1,11,'63','2012-02-03 : Rs.7660',1,''),(97,'2012-10-20 16:01:28',1,11,'64','2012-05-23 : Rs.6650',1,''),(98,'2012-10-20 16:01:28',1,11,'65','2012-05-24 : Rs.1242',1,''),(99,'2012-10-20 16:01:28',1,11,'65','2012-05-24 : Rs.1242',2,'Changed details.'),(100,'2012-10-20 16:01:27',1,11,'66','2012-05-24 : Rs.6220',1,''),(101,'2012-10-20 16:01:27',1,11,'67','2012-05-29 : Rs.3978',1,''),(102,'2012-10-20 16:01:27',1,11,'68','2012-06-01 : Rs.26500',1,''),(103,'2012-10-20 16:01:27',1,11,'69','2012-06-01 : Rs.26500',1,''),(104,'2012-10-20 16:01:27',1,11,'70','2012-06-14 : Rs.8500',1,''),(105,'2012-10-20 16:01:27',1,11,'71','2012-08-02 : Rs.5000',1,''),(106,'2012-10-20 16:01:27',1,11,'72','2012-08-11 : Rs.5000',1,''),(107,'2012-10-20 16:01:27',1,11,'73','2012-08-11 : Rs.5000',1,''),(108,'2012-10-20 16:01:27',1,11,'74','2012-08-11 : Rs.5000',1,''),(109,'2012-10-20 16:01:27',1,11,'75','2012-08-24 : Rs.20000',1,''),(110,'2012-10-20 16:01:27',1,11,'76','2012-08-24 : Rs.5000',1,''),(111,'2012-10-20 16:01:27',1,11,'77','2012-08-29 : Rs.10000',1,''),(112,'2012-10-20 16:01:27',1,11,'78','2012-08-29 : Rs.2500',1,''),(113,'2012-10-20 16:01:27',1,11,'79','2012-08-31 : Rs.30000',1,''),(114,'2012-10-20 16:01:27',1,11,'79','2012-08-31 : Rs.30000',3,''),(115,'2012-10-20 16:01:27',1,11,'79','2012-08-31 : Rs.30000',1,''),(116,'2012-10-20 16:01:27',1,11,'80','2012-08-31 : Rs.30000',1,''),(117,'2012-10-20 16:01:27',1,11,'81','2012-08-31 : Rs.30000',1,''),(118,'2012-10-20 16:01:26',1,11,'82','2012-07-06 : Rs.2500',1,''),(119,'2012-10-20 16:01:26',1,11,'83','2012-06-22 : Rs.20000',1,''),(120,'2012-10-20 16:01:26',1,11,'84','2011-09-23 : Rs.26500',1,''),(121,'2012-10-20 16:01:26',1,11,'85','2011-08-17 : Rs.12683',1,''),(122,'2012-10-20 16:01:26',1,11,'86','2011-08-12 : Rs.29500',1,''),(123,'2012-10-20 16:01:26',1,11,'87','2011-08-12 : Rs.29500',1,''),(124,'2012-10-20 16:01:26',1,11,'88','2010-08-02 : Rs.3309',1,''),(125,'2012-10-20 16:01:26',1,11,'89','2011-04-26 : Rs.3309',1,''),(126,'2012-10-20 16:01:26',1,11,'90','2011-08-02 : Rs.3309',1,''),(127,'2012-10-20 16:01:26',1,11,'91','2010-07-14 : Rs.110',1,''),(128,'2012-10-20 16:01:26',1,11,'92','2009-03-04 : Rs.55',1,''),(129,'2012-10-20 16:01:26',1,11,'93','2009-04-25 : Rs.55',1,''),(130,'2012-10-20 16:01:26',1,10,'2','TeamMember object',1,''),(131,'2012-10-20 16:01:26',1,10,'1','TeamMember object',2,'Changed photo.'),(132,'2012-10-20 16:01:26',1,10,'1','TeamMember object',2,'Changed photo.'),(133,'2012-10-20 16:01:26',1,10,'3','TeamMember object',1,''),(134,'2012-10-20 16:01:26',1,10,'4','TeamMember object',1,''),(135,'2012-10-20 16:01:26',1,10,'4','TeamMember object',2,'Changed designation.'),(136,'2012-10-20 16:01:25',1,10,'4','TeamMember object',2,'Changed photo.'),(137,'2012-10-20 16:01:25',1,10,'5','TeamMember object',1,''),(138,'2012-10-20 16:01:25',1,10,'6','TeamMember object',1,''),(139,'2012-10-20 16:01:25',1,10,'7','TeamMember object',1,''),(140,'2012-10-20 16:01:25',1,10,'8','TeamMember object',1,''),(141,'2012-10-20 16:01:25',1,10,'8','TeamMember object',2,'Changed name.'),(142,'2012-10-20 16:01:25',1,10,'9','TeamMember object',1,''),(143,'2012-10-20 16:01:25',1,10,'10','TeamMember object',1,''),(144,'2012-10-20 16:01:25',1,10,'11','TeamMember object',1,''),(145,'2012-10-20 16:01:25',1,10,'12','TeamMember object',1,''),(146,'2012-10-20 16:01:25',1,10,'12','TeamMember object',2,'Changed designation.'),(147,'2012-10-20 16:01:25',1,10,'13','TeamMember object',1,''),(148,'2012-10-20 16:01:25',1,10,'14','TeamMember object',1,''),(149,'2012-10-20 16:01:25',1,10,'15','TeamMember object',1,''),(150,'2012-10-20 16:01:25',1,32,'1','LakshyaUpdate object',2,'Changed update_text.'),(151,'2012-10-20 16:01:25',1,32,'7','LakshyaUpdate object',2,'Changed update_text.'),(152,'2012-10-20 16:01:25',1,32,'7','LakshyaUpdate object',2,'Changed update_text.'),(153,'2012-10-20 16:01:25',1,32,'7','LakshyaUpdate object',2,'Changed update_text.'),(154,'2012-10-20 16:01:25',1,32,'4','LakshyaUpdate object',2,'Changed update_text.'),(155,'2012-10-20 16:01:25',1,32,'7','LakshyaUpdate object',2,'No fields changed.'),(156,'2012-10-20 16:01:25',1,32,'4','LakshyaUpdate object',2,'Changed update_text.'),(157,'2012-10-20 16:01:25',1,32,'4','LakshyaUpdate object',2,'Changed update_text.'),(158,'2012-10-20 16:01:25',1,32,'2','LakshyaUpdate object',2,'Changed update_text.'),(159,'2012-10-20 16:01:24',1,32,'5','LakshyaUpdate object',2,'Changed update_text.'),(160,'2012-10-20 16:01:24',1,32,'3','LakshyaUpdate object',2,'Changed update_text.'),(161,'2012-10-20 16:01:24',1,32,'6','LakshyaUpdate object',2,'No fields changed.'),(162,'2012-10-20 16:01:24',1,10,'11','TeamMember object',2,'Changed description.'),(163,'2012-10-20 16:01:24',1,10,'13','TeamMember object',2,'Changed description.'),(164,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed designation.'),(165,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed description.'),(166,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed description.'),(167,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed name and description.'),(168,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed name.'),(169,'2012-10-20 16:01:24',1,10,'11','TeamMember object',2,'Changed name and description.'),(170,'2012-10-20 16:01:24',1,10,'11','TeamMember object',2,'Changed description.'),(171,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed name and description.'),(172,'2012-10-20 16:01:24',1,10,'12','TeamMember object',2,'Changed description.'),(173,'2012-10-20 16:01:24',1,3,'2','mesrijareddy@gmail.com',1,''),(174,'2012-10-20 16:01:24',1,8,'1','',1,''),(175,'2012-10-20 16:01:24',1,20,'1','',1,''),(176,'2012-10-20 16:01:24',1,8,'1','',2,'No fields changed.'),(177,'2012-10-20 16:01:24',1,3,'2','mesrijareddy@gmail.com',2,'Changed password, first_name, last_name and email.'),(178,'2012-10-20 16:01:24',1,3,'3','kiran.nitwarangal@gmail.com',1,''),(179,'2012-10-20 16:01:24',1,3,'3','kiran.nitwarangal@gmail.com',2,'Changed password, first_name, last_name and email.'),(180,'2012-10-20 16:01:23',1,3,'3','kiran.nitwarangal@gmail.com',2,'Changed password.'),(181,'2012-10-20 16:01:23',1,3,'4','shekhar.shekhar.mintu@gmail.co',1,''),(182,'2012-10-20 16:01:23',1,3,'4','shekhar.shekhar.mintu@gmail.co',2,'Changed password, first_name, last_name and email.'),(183,'2012-10-20 16:01:23',1,3,'5','vadiginatatarao@gmail.com',1,''),(184,'2012-10-20 16:01:23',1,3,'5','vadiginatatarao@gmail.com',2,'Changed password, first_name, last_name and email.'),(185,'2012-10-20 16:01:23',1,3,'6','praveen.pravi08@gmail.com',1,''),(186,'2012-10-20 16:01:23',1,3,'6','praveen.pravi08@gmail.com',2,'Changed password, first_name, last_name and email.'),(187,'2012-10-20 16:01:23',1,3,'7','gkgayathri1@gmail.com',1,''),(188,'2012-10-20 16:01:23',1,3,'7','gkgayathri1@gmail.com',2,'Changed password, first_name, last_name and email.'),(189,'2012-10-20 16:01:23',1,3,'7','gkgayathri1@gmail.com',2,'Changed password.'),(190,'2012-10-20 16:01:23',1,3,'8','rajuponnala143@gmail.com',1,''),(191,'2012-10-20 16:01:23',1,3,'8','rajuponnala143@gmail.com',2,'Changed password, first_name, last_name and email.'),(192,'2012-10-20 16:01:23',1,3,'9','justjayaswal@gmail.com',1,''),(193,'2012-10-20 16:01:23',1,3,'9','justjayaswal@gmail.com',2,'Changed password, first_name, last_name and email.'),(194,'2012-10-20 16:01:23',1,3,'10','hcmg2489@gmail.com',1,''),(195,'2012-10-20 16:01:23',1,3,'10','hcmg2489@gmail.com',2,'Changed password, first_name, last_name and email.'),(196,'2012-10-20 16:01:23',1,3,'11','ss51091@gmail.com',1,''),(197,'2012-10-20 16:01:23',1,3,'11','ss51091@gmail.com',2,'Changed password, first_name, last_name and email.'),(198,'2012-10-20 16:01:23',1,3,'12','mahesh.gitta@gmail.com',1,''),(199,'2012-10-20 16:01:23',1,3,'12','mahesh.gitta@gmail.com',2,'Changed password, first_name, last_name and email.'),(200,'2012-10-20 16:01:23',1,3,'13','rajafrnd2u@gmail.com',1,''),(201,'2012-10-20 16:01:22',1,3,'13','rajafrnd2u@gmail.com',2,'Changed password, first_name, last_name and email.'),(202,'2012-10-20 16:01:22',1,3,'14','chaitanyasai03@gmail.com',1,''),(203,'2012-10-20 16:01:22',1,3,'14','chaitanyasai03@gmail.com',2,'Changed password, first_name, last_name and email.'),(204,'2012-10-20 16:01:22',1,3,'15','mastanvali.nitw@gmail.com',1,''),(205,'2012-10-20 16:01:22',1,3,'15','mastanvali.nitw@gmail.com',2,'Changed password, first_name, last_name and email.'),(206,'2012-10-20 16:01:22',1,3,'16','aadhi33@gmail.com',1,''),(207,'2012-10-20 16:01:22',1,3,'16','aadhi33@gmail.com',2,'Changed password, first_name, last_name and email.'),(208,'2012-10-20 16:01:22',1,3,'17','desmalanils48@gmail.com',1,''),(209,'2012-10-20 16:01:22',1,3,'17','desmalanils48@gmail.com',2,'Changed password, first_name, last_name and email.'),(210,'2012-10-20 16:01:22',1,3,'18','sandhyalalprateek2010@gmail.co',1,''),(211,'2012-10-20 16:01:22',1,3,'18','sandhyalalprateek2010@gmail.co',2,'Changed password, first_name, last_name and email.'),(212,'2012-10-20 16:01:22',1,3,'19','sonupdh@gmail.com',1,''),(213,'2012-10-20 16:01:22',1,3,'19','sonupdh@gmail.com',2,'Changed password, first_name, last_name and email.'),(214,'2012-10-20 16:01:22',1,3,'20','alkapil06raj@gmail.com',1,''),(215,'2012-10-20 16:01:22',1,3,'20','alkapil06raj@gmail.com',2,'Changed password, first_name, last_name and email.'),(216,'2012-10-20 16:01:22',1,3,'20','alkapil06raj@gmail.com',2,'Changed password.'),(217,'2012-10-20 16:01:22',1,3,'21','adikiprakash@gmail.com',1,''),(218,'2012-10-20 16:01:22',1,3,'21','adikiprakash@gmail.com',2,'Changed password, first_name, last_name and email.'),(219,'2012-10-20 16:01:22',1,3,'22','ravitejabadisa@gmail.com',1,''),(220,'2012-10-20 16:01:22',1,3,'22','ravitejabadisa@gmail.com',2,'Changed password, first_name, last_name and email.'),(221,'2012-10-20 16:01:22',1,3,'23','yetti.143@gmail.com',1,''),(222,'2012-10-20 16:01:22',1,3,'23','yetti.143@gmail.com',2,'Changed password, first_name, last_name and email.'),(223,'2012-10-20 16:01:21',1,8,'2','Suman',1,''),(224,'2012-10-20 16:01:21',1,8,'2','Suman',2,'No fields changed.'),(225,'2012-10-20 16:01:21',1,8,'3','Channa',1,''),(226,'2012-10-20 16:01:21',1,8,'4','Rajeev',1,''),(227,'2012-10-20 16:01:21',1,8,'5','Raju',1,''),(228,'2012-10-20 16:01:21',1,3,'7','gkgayathri1@gmail.com',2,'Changed password and last_name.'),(229,'2012-10-20 16:01:21',1,8,'6','Gayathri',1,''),(230,'2012-10-20 16:01:21',1,8,'7','Durgam Praveen',1,''),(231,'2012-10-20 16:01:21',1,8,'8','V Thata',1,''),(232,'2012-10-20 16:01:21',1,8,'8','V Thata',2,'Changed contact_number.'),(233,'2012-10-20 16:01:21',1,8,'9','Shekhar',1,''),(234,'2012-10-20 16:01:21',1,8,'10','Kiran Kumar',1,''),(235,'2012-10-20 16:01:21',1,8,'11','Kedari',1,''),(236,'2012-10-20 16:01:21',1,8,'12','Mastan',1,''),(237,'2012-10-20 16:01:21',1,8,'12','Mastan',2,'Changed billing_country, contact_number, is_nitw_alumni, department and year_of_passing.'),(238,'2012-10-20 16:01:21',1,8,'13','Aadinarayana',1,''),(239,'2012-10-20 16:01:21',1,8,'14','Anil',1,''),(240,'2012-10-20 16:01:21',1,8,'15','Sandhyalal',1,''),(241,'2012-10-20 16:01:21',1,8,'16','Rahul',1,''),(242,'2012-10-20 16:01:20',1,8,'17','Kapil',1,''),(243,'2012-10-20 16:01:20',1,8,'18','Adiki',1,''),(244,'2012-10-20 16:01:20',1,8,'19','Ravi',1,''),(245,'2012-10-20 16:01:20',1,8,'20','Singaraiah',1,''),(246,'2012-10-20 16:01:20',1,8,'9','Shekhar',2,'Changed is_nitw_alumni.'),(247,'2012-10-20 16:01:20',1,8,'15','Sandhyalal',2,'Changed is_nitw_alumni.'),(248,'2012-10-20 16:01:20',1,20,'2','Channa',1,''),(249,'2012-10-20 16:01:20',1,20,'2','Channa',2,'Changed status.'),(250,'2012-10-20 16:01:20',1,20,'2','Channa',2,'Changed intermediate_percentage.'),(251,'2012-10-20 16:01:20',1,8,'21','Rajesh',1,''),(252,'2012-10-20 16:01:20',1,8,'22','Mahesh',1,''),(253,'2012-10-20 16:01:20',1,20,'3','Suman',1,''),(254,'2012-10-20 16:01:20',1,20,'2','Channa',2,'Changed sgpa for sgpa \"Sgpa object\".'),(255,'2012-10-20 16:01:20',1,20,'4','Rajesh',1,''),(256,'2012-10-20 16:01:20',1,20,'4','Rajesh',2,'Changed ssc_board.'),(257,'2012-10-20 16:01:20',1,20,'4','Rajesh',2,'No fields changed.'),(258,'2012-10-20 16:01:20',1,20,'5','Mahesh',1,''),(259,'2012-10-20 16:01:20',1,20,'5','Mahesh',2,'Changed ssc_percentage and intermediate_percentage.'),(260,'2012-10-20 16:01:20',1,20,'6','Kiran Kumar',1,''),(261,'2012-10-20 16:01:20',1,20,'7','Durgam Praveen',1,''),(262,'2012-10-20 16:01:20',1,20,'6','Kiran Kumar',2,'Changed status.'),(263,'2012-10-20 16:01:20',1,20,'8','Gayathri',1,''),(264,'2012-10-20 16:01:19',1,20,'9','V Thata',1,''),(265,'2012-10-20 16:01:19',1,20,'10','Raju',1,''),(266,'2012-10-20 16:01:19',1,20,'11','Shekhar',1,''),(267,'2012-10-20 16:01:19',1,20,'11','Shekhar',2,'Changed status.'),(268,'2012-10-20 16:01:19',1,20,'12','Rajeev',1,''),(269,'2012-10-20 16:01:19',1,20,'2','Channa',2,'No fields changed.'),(270,'2012-10-20 16:01:19',1,20,'13','Kedari',1,''),(271,'2012-10-20 16:01:19',1,20,'8','Gayathri',2,'Changed sex and roll_num.'),(272,'2012-10-20 16:01:19',1,20,'14','Mastan',1,''),(273,'2012-10-20 16:01:19',1,20,'15','Singaraiah',1,''),(274,'2012-10-20 16:01:19',1,20,'16','Anil',1,''),(275,'2012-10-20 16:01:19',1,20,'17','Ravi',1,''),(276,'2012-10-20 16:01:19',1,20,'18','Aadinarayana',1,''),(277,'2012-10-20 16:01:19',1,20,'19','Adiki',1,''),(278,'2012-10-20 16:01:19',1,20,'20','Sandhyalal',1,''),(279,'2012-10-20 16:01:19',1,20,'21','Rahul',1,''),(280,'2012-10-20 16:01:19',1,20,'22','Kapil',1,''),(281,'2012-10-20 16:01:19',1,12,'1','Trahi Foundation',1,''),(282,'2012-10-20 16:01:19',1,12,'2','NITW Americas Alumni Chapter',1,''),(283,'2012-10-20 16:01:19',1,12,'3','NITW Alumni Middle East Chapter',1,''),(284,'2012-10-20 16:01:19',1,12,'4','Tom Zacharia Foundation',1,''),(285,'2012-10-20 16:01:19',1,12,'5','BVS Murthy 1979-83 NITW Alumni Scholarship',1,''),(286,'2012-10-20 16:01:18',1,12,'6','K Srikant Murty 1979-83 NITW Alumni Scholarship',1,''),(287,'2012-10-20 16:01:18',1,12,'7','Jyothirmoy Das 1979-83 NITW Alumni Scholarship',1,''),(288,'2012-10-20 16:01:18',1,12,'8','Mr. Narayan',1,''),(289,'2012-10-20 16:01:18',1,12,'9','Mr. Prabhakar Puvvada',1,''),(290,'2012-10-20 16:01:18',1,12,'10','Mr. Vasant Roy',1,''),(291,'2012-10-20 16:01:18',1,26,'1','Srija',1,''),(292,'2012-10-20 16:01:18',1,26,'2','Kiran Kumar',1,''),(293,'2012-10-20 16:01:18',1,26,'3','Rahul',1,''),(294,'2012-10-20 16:01:18',1,26,'4','Singaraiah',1,''),(295,'2012-10-20 16:01:18',1,26,'5','Kapil',1,''),(296,'2012-10-20 16:01:18',1,26,'6','Adiki',1,''),(297,'2012-10-20 16:01:18',1,26,'7','Aadinarayana',1,''),(298,'2012-10-20 16:01:18',1,26,'8','Ravi',1,''),(299,'2012-10-20 16:01:18',1,26,'9','Sandhyalal',1,''),(300,'2012-10-20 16:01:17',1,26,'10','Anil',1,''),(301,'2012-10-20 16:01:17',1,26,'11','Kedari',1,''),(302,'2012-10-20 16:01:17',1,26,'12','Mastan',1,''),(303,'2012-10-20 16:01:17',1,26,'13','Rajeev',1,''),(304,'2012-10-20 16:01:17',1,26,'14','Channa',1,''),(305,'2012-10-20 16:01:17',1,26,'15','Suman',1,''),(306,'2012-10-20 16:01:17',1,26,'16','Rajesh',1,''),(307,'2012-10-20 16:01:17',1,26,'17','Mahesh',1,''),(308,'2012-10-20 16:01:17',1,26,'18','Durgam Praveen',1,''),(309,'2012-10-20 16:01:17',1,26,'19','Gayathri',1,''),(310,'2012-10-20 16:01:17',1,26,'20','V Thata',1,''),(311,'2012-10-20 16:01:17',1,26,'21','Raju',1,''),(312,'2012-10-20 16:01:16',1,26,'22','Shekhar',1,''),(313,'2012-10-20 16:01:16',1,29,'1','Channa - First Semester',1,''),(314,'2012-10-20 16:01:16',1,29,'2','Channa - Second Semester',1,''),(315,'2012-10-20 16:01:16',1,29,'3','Channa - Third Semester',1,''),(316,'2012-10-20 16:01:16',1,29,'4','Channa - Fourth Semester',1,''),(317,'2012-10-20 16:01:16',1,29,'5','Channa - Fifth Semester',1,''),(318,'2012-10-20 16:01:16',1,29,'6','Channa - Sixth Semster',1,''),(319,'2012-10-20 16:01:16',1,29,'7','Channa - Seventh Semster',1,''),(320,'2012-10-20 16:01:16',1,29,'8','Channa - Eighth Semster',1,''),(321,'2012-10-20 16:01:16',1,12,'5','BVS Murthy 1979-83 NITW Alumni Scholarship',2,'Changed description.'),(322,'2012-10-20 16:01:16',1,26,'14','Channa',2,'Changed donation_fund.'),(323,'2012-10-20 16:01:16',1,26,'15','Suman',2,'Changed donation_fund.'),(324,'2012-10-20 16:01:16',1,26,'14','Channa',2,'Changed donation_fund.'),(325,'2012-10-20 16:01:16',1,26,'15','Suman',2,'Changed donation_fund.'),(326,'2012-10-20 16:01:16',1,12,'1','Trahi Foundation',2,'Changed description.'),(327,'2012-10-20 16:01:16',1,12,'2','NITW Americas Alumni Chapter',2,'Changed description.'),(328,'2012-10-20 16:01:16',1,12,'3','NITW Alumni Middle East Chapter',2,'Changed description.'),(329,'2012-10-20 16:01:15',1,12,'4','Tom Zacharia Foundation',2,'Changed description.'),(330,'2012-10-20 16:01:15',1,12,'6','K Srikant Murty 1979-83 NITW Alumni Scholarship',2,'Changed description.'),(331,'2012-10-20 16:01:15',1,12,'7','Jyothirmoy Das 1979-83 NITW Alumni Scholarship',2,'Changed description.'),(332,'2012-10-20 16:01:15',1,12,'8','Mr. Narayan',2,'Changed description.'),(333,'2012-10-20 16:01:15',1,12,'9','Mr. Prabhakar Puvvada',2,'Changed description.'),(334,'2012-10-20 16:01:15',1,12,'10','Mr. Vasant Roy',2,'Changed description.'),(335,'2012-10-20 16:01:15',1,29,'9','Singaraiah - First Semester',1,''),(336,'2012-10-20 16:01:15',1,29,'10','Singaraiah - Second Semester',1,''),(337,'2012-10-20 16:01:15',1,29,'11','Singaraiah - Third Semester',1,''),(338,'2012-10-20 16:01:15',1,29,'12','Anil - First Semester',1,''),(339,'2012-10-20 16:01:15',1,29,'13','Anil - Second Semester',1,''),(340,'2012-10-20 16:01:15',1,29,'14','Anil - Third Semester',1,''),(341,'2012-10-20 16:01:15',1,29,'15','Mastan - First Semester',1,''),(342,'2012-10-20 16:01:15',1,29,'16','Mastan - Second Semester',1,''),(343,'2012-10-20 16:01:15',1,29,'17','Mastan - Third Semester',1,''),(344,'2012-10-20 16:01:15',1,29,'18','Mastan - Fourth Semester',1,''),(345,'2012-10-20 16:01:15',1,29,'19','Mastan - Fifth Semester',1,''),(346,'2012-10-20 16:01:15',1,29,'20','Ravi - First Semester',1,''),(347,'2012-10-20 16:01:15',1,29,'21','Ravi - Second Semester',1,''),(348,'2012-10-20 16:01:14',1,29,'22','Ravi - Third Semester',1,''),(349,'2012-10-20 16:01:14',1,29,'23','Aadinarayana - First Semester',1,''),(350,'2012-10-20 16:01:14',1,29,'24','Aadinarayana - Second Semester',1,''),(351,'2012-10-20 16:01:14',1,29,'25','Aadinarayana - Third Semester',1,''),(352,'2012-10-20 16:01:14',1,29,'26','Aadinarayana - Fourth Semester',1,''),(353,'2012-10-20 16:01:14',1,29,'27','Aadinarayana - Fifth Semester',1,''),(354,'2012-10-20 16:01:14',1,29,'28','Adiki - First Semester',1,''),(355,'2012-10-20 16:01:14',1,29,'29','Adiki - Second Semester',1,''),(356,'2012-10-20 16:01:14',1,29,'30','Suman - First Semester',1,''),(357,'2012-10-20 16:01:14',1,29,'31','Suman - Second Semester',1,''),(358,'2012-10-20 16:01:14',1,29,'32','Suman - Third Semester',1,''),(359,'2012-10-20 16:01:14',1,29,'33','Suman - Fourth Semester',1,''),(360,'2012-10-20 16:01:14',1,29,'34','Suman - Fifth Semester',1,''),(361,'2012-10-20 16:01:14',1,29,'35','Suman - Sixth Semster',1,''),(362,'2012-10-20 16:01:14',1,29,'36','Suman - Seventh Semster',1,''),(363,'2012-10-20 16:01:14',1,29,'37','Suman - Eighth Semster',1,''),(364,'2012-10-20 16:01:14',1,26,'5','Kapil',2,'Changed donation_fund.'),(365,'2012-10-20 16:01:14',1,29,'38','Sandhyalal - First Semester',1,''),(366,'2012-10-20 16:01:14',1,29,'39','Sandhyalal - Second Semester',1,''),(367,'2012-10-20 16:01:14',1,29,'40','Sandhyalal - Third Semester',1,''),(368,'2012-10-20 16:01:14',1,29,'41','Rahul - First Semester',1,''),(369,'2012-10-20 16:01:14',1,29,'42','Rahul - Second Semester',1,''),(370,'2012-10-20 16:01:14',1,29,'43','Rahul - Third Semester',1,''),(371,'2012-10-20 16:01:14',1,29,'44','Mahesh - First Semester',1,''),(372,'2012-10-20 16:01:14',1,29,'45','Mahesh - Second Semester',1,''),(373,'2012-10-20 16:01:13',1,29,'46','Mahesh - Third Semester',1,''),(374,'2012-10-20 16:01:13',1,29,'47','Mahesh - Fourth Semester',1,''),(375,'2012-10-20 16:01:13',1,29,'48','Mahesh - Fifth Semester',1,''),(376,'2012-10-20 16:01:13',1,29,'49','Mahesh - Sixth Semster',1,''),(377,'2012-10-20 16:01:13',1,29,'50','Mahesh - Seventh Semster',1,''),(378,'2012-10-20 16:01:13',1,29,'51','Mahesh - Eighth Semster',1,''),(379,'2012-10-20 16:01:13',1,29,'52','Rajesh - First Semester',1,''),(380,'2012-10-20 16:01:13',1,29,'53','Rajesh - Second Semester',1,''),(381,'2012-10-20 16:01:13',1,29,'54','Rajesh - Third Semester',1,''),(382,'2012-10-20 16:01:13',1,29,'55','Rajesh - Fourth Semester',1,''),(383,'2012-10-20 16:01:13',1,29,'56','Rajesh - Fifth Semester',1,''),(384,'2012-10-20 16:01:13',1,29,'57','Rajesh - Sixth Semster',1,''),(385,'2012-10-20 16:01:13',1,29,'58','Rajesh - Seventh Semster',1,''),(386,'2012-10-20 16:01:13',1,29,'59','Rajesh - Eighth Semster',1,''),(387,'2012-10-20 16:01:13',1,29,'60','Rajeev - First Semester',1,''),(388,'2012-10-20 16:01:13',1,29,'61','Rajeev - Second Semester',1,''),(389,'2012-10-20 16:01:13',1,29,'62','Rajeev - Third Semester',1,''),(390,'2012-10-20 16:01:13',1,29,'63','Rajeev - Fourth Semester',1,''),(391,'2012-10-20 16:01:13',1,29,'64','Rajeev - Fifth Semester',1,''),(392,'2012-10-20 16:01:13',1,29,'65','Rajeev - Sixth Semster',1,''),(393,'2012-10-20 16:01:13',1,29,'66','Rajeev - Seventh Semster',1,''),(394,'2012-10-20 16:01:13',1,29,'67','Rajeev - Eighth Semster',1,''),(395,'2012-10-20 16:01:12',1,29,'68','V Thata - First Semester',1,''),(396,'2012-10-20 16:01:12',1,29,'69','V Thata - Second Semester',1,''),(397,'2012-10-20 16:01:12',1,29,'70','V Thata - Third Semester',1,''),(398,'2012-10-20 16:01:12',1,29,'71','V Thata - Fourth Semester',1,''),(399,'2012-10-20 16:01:12',1,29,'72','V Thata - Fifth Semester',1,''),(400,'2012-10-20 16:01:12',1,29,'73','V Thata - Sixth Semster',1,''),(401,'2012-10-20 16:01:12',1,29,'74','V Thata - Seventh Semster',1,''),(402,'2012-10-20 16:01:12',1,29,'75','V Thata - Eighth Semster',1,''),(403,'2012-10-20 16:01:12',1,29,'76','Raju - First Semester',1,''),(404,'2012-10-20 16:01:12',1,29,'77','Raju - Second Semester',1,''),(405,'2012-10-20 16:01:12',1,29,'78','Raju - Third Semester',1,''),(406,'2012-10-20 16:01:12',1,29,'79','Raju - Fourth Semester',1,''),(407,'2012-10-20 16:01:12',1,29,'80','Raju - Fifth Semester',1,''),(408,'2012-10-20 16:01:12',1,29,'81','Raju - Sixth Semster',1,''),(409,'2012-10-20 16:01:12',1,29,'82','Raju - Seventh Semster',1,''),(410,'2012-10-20 16:01:12',1,29,'83','Raju - Eighth Semster',1,''),(411,'2012-10-20 16:01:12',1,29,'84','Kapil - First Semester',1,''),(412,'2012-10-20 16:01:12',1,29,'85','Kapil - Second Semester',1,''),(413,'2012-10-20 16:01:11',1,29,'86','Kapil - Third Semester',1,''),(414,'2012-10-20 16:01:11',1,29,'87','Shekhar - First Semester',1,''),(415,'2012-10-20 16:01:11',1,29,'88','Shekhar - Second Semester',1,''),(416,'2012-10-20 16:01:11',1,29,'89','Shekhar - Third Semester',1,''),(417,'2012-10-20 16:01:11',1,29,'90','Shekhar - Fourth Semester',1,''),(418,'2012-10-20 16:01:11',1,29,'91','Shekhar - Fifth Semester',1,''),(419,'2012-10-20 16:01:11',1,29,'92','Shekhar - Sixth Semster',1,''),(420,'2012-10-20 16:01:11',1,29,'93','Shekhar - Seventh Semster',1,''),(421,'2012-10-20 16:01:11',1,29,'94','Shekhar - Seventh Semster',1,''),(422,'2012-10-20 16:01:11',1,29,'95','Shekhar - Sixth Semster',1,''),(423,'2012-10-20 16:01:11',1,29,'96','Shekhar - Eighth Semster',1,''),(424,'2012-10-20 16:01:11',1,29,'97','Kedari - First Semester',1,''),(425,'2012-10-20 16:01:11',1,29,'98','Kedari - Second Semester',1,''),(426,'2012-10-20 16:01:11',1,29,'99','Kedari - Third Semester',1,''),(427,'2012-10-20 16:01:11',1,29,'100','Kedari - Fourth Semester',1,''),(428,'2012-10-20 16:01:11',1,29,'101','Kedari - Fifth Semester',1,''),(429,'2012-10-20 16:01:11',1,29,'102','Kiran Kumar - First Semester',1,''),(430,'2012-10-20 16:01:11',1,29,'103','Kiran Kumar - Second Semester',1,''),(431,'2012-10-20 16:01:11',1,29,'104','Kiran Kumar - Third Semester',1,''),(432,'2012-10-20 16:01:10',1,29,'105','Kiran Kumar - Fourth Semester',1,''),(433,'2012-10-20 16:01:10',1,29,'106','Kiran Kumar - Fifth Semester',1,''),(434,'2012-10-20 16:01:10',1,29,'107','Kiran Kumar - Sixth Semster',1,''),(435,'2012-10-20 16:01:10',1,29,'108','V Thata - Seventh Semster',1,''),(436,'2012-10-20 16:01:10',1,29,'109','Kiran Kumar - Eighth Semster',1,''),(437,'2012-10-20 16:01:10',1,29,'110','Gayathri - First Semester',1,''),(438,'2012-10-20 16:01:10',1,29,'111','Gayathri - Second Semester',1,''),(439,'2012-10-20 16:01:10',1,29,'112','Gayathri - Third Semester',1,''),(440,'2012-10-20 16:01:10',1,29,'113','Gayathri - Fourth Semester',1,''),(441,'2012-10-20 16:01:10',1,29,'114','Gayathri - Fifth Semester',1,''),(442,'2012-10-20 16:01:10',1,29,'115','Gayathri - Sixth Semster',1,''),(443,'2012-10-20 16:01:10',1,29,'116','Gayathri - Seventh Semster',1,''),(444,'2012-10-20 16:01:10',1,29,'117','Gayathri - Eighth Semster',1,''),(445,'2012-10-20 16:01:10',1,29,'118','Durgam Praveen - First Semester',1,''),(446,'2012-10-20 16:01:10',1,29,'119','Durgam Praveen - Second Semester',1,''),(447,'2012-10-20 16:01:10',1,29,'120','Durgam Praveen - Third Semester',1,''),(448,'2012-10-20 16:01:10',1,29,'121','Durgam Praveen - Fourth Semester',1,''),(449,'2012-10-20 16:01:10',1,29,'122','Durgam Praveen - Fifth Semester',1,''),(450,'2012-10-20 16:01:10',1,29,'123','Durgam Praveen - Sixth Semster',1,''),(451,'2012-10-20 16:01:10',1,29,'124','Durgam Praveen - Seventh Semster',1,''),(452,'2012-10-20 16:01:10',1,29,'125','Kedari - Sixth Semster',1,''),(453,'2012-10-20 16:01:09',1,29,'126','Sandhyalal - Fourth Semester',1,''),(454,'2012-10-20 16:01:09',1,29,'127','Rahul - Fourth Semester',1,''),(455,'2012-10-20 16:01:09',1,29,'128','Mastan - Sixth Semster',1,''),(456,'2012-10-20 16:01:09',1,26,'1','Srija',2,'Added scholar update \"ScholarUpdate object\". Added scholar update \"ScholarUpdate object\".');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'log entry','admin','logentry'),(7,'migration history','south','migrationhistory'),(8,'person','people','person'),(9,'person_preference','people','person_preference'),(10,'team member','people','teammember'),(11,'expense','accounts','expense'),(12,'Donation Fund','accounts','donationfund'),(13,'donation','accounts','donation'),(14,'innovation application','innovation','innovationapplication'),(15,'innovation','innovation','innovation'),(16,'innovation update','innovation','innovationupdate'),(17,'innovation update image','innovation','innovationupdateimage'),(18,'innovation update video','innovation','innovationupdatevideo'),(19,'innovation payment','innovation','innovationpayment'),(20,'scholarship application','scholarships','scholarshipapplication'),(21,'sgpa','scholarships','sgpa'),(22,'other exam performance','scholarships','otherexamperformance'),(23,'family detail','scholarships','familydetail'),(24,'other scholarship','scholarships','otherscholarship'),(25,'scholarship verification','scholarships','scholarshipverification'),(26,'scholar','scholarships','scholar'),(27,'scholarship payment','scholarships','scholarshippayment'),(28,'scholar update','scholarships','scholarupdate'),(29,'scholar academic update','scholarships','scholaracademicupdate'),(30,'grade update','scholarships','gradeupdate'),(31,'repayment','scholarships','repayment'),(32,'lakshya update','utils','lakshyaupdate'),(33,'lakskhya testimonial','utils','lakskhyatestimonial'),(34,'payment temp','accounts','paymenttemp');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('203f3ef322858b45c464dad15915488e','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:16:21'),('20dada8574661bb1e2cdcdc70a064ccd','YjUxMzFhZjNhNjRmNjlmNDFlOTA2MzAxNWYyOWY3ZDA5OWVkNGJlNjqAAn1xAS4=\n','2012-10-28 13:47:45'),('23e43f65afbeff74b3bccdfad1c67578','ZTQ1YTEwZGFlZTEwZmY2OTc5NDM0OWRjYzU3Y2E1MjY2YjM2ZGY5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n','2012-10-04 11:21:48'),('266e7e9ece30a9b2fd9c39362dc4c6df','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 08:01:03'),('2923afc1c43315ca220500c4a14be937','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 12:56:01'),('2a6696c3a14d1c8860808c67174879c8','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:42:49'),('4542e191983ad5d0d5bf871a6e3a5b6b','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:01:02'),('5018958531b8612f7843efadc6202c7f','ZTQ1YTEwZGFlZTEwZmY2OTc5NDM0OWRjYzU3Y2E1MjY2YjM2ZGY5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n','2012-10-05 13:27:26'),('748824b0d4597085910e60e9d09b70ec','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:21:34'),('7ab803d69833abc8277ee4c8b74a11cf','ZTQ1YTEwZGFlZTEwZmY2OTc5NDM0OWRjYzU3Y2E1MjY2YjM2ZGY5NTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQRLAXUu\n','2012-10-06 02:58:12'),('85ca8c8019e94b2815f94edd063d0a87','YjUxMzFhZjNhNjRmNjlmNDFlOTA2MzAxNWYyOWY3ZDA5OWVkNGJlNjqAAn1xAS4=\n','2012-10-13 20:03:11'),('98db2802571938d93cfd005bb538a516','YjUxMzFhZjNhNjRmNjlmNDFlOTA2MzAxNWYyOWY3ZDA5OWVkNGJlNjqAAn1xAS4=\n','2012-10-15 07:50:14'),('a22718cb30239eea8d14afe29c03f760','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:42:34'),('ab3e5b309f817e9e44d8ea626d14d7f7','YjUxMzFhZjNhNjRmNjlmNDFlOTA2MzAxNWYyOWY3ZDA5OWVkNGJlNjqAAn1xAS4=\n','2012-10-15 13:18:07'),('be116f1aeddb43b082c40cf5665090e3','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 07:41:01'),('bedbf8c2eeb108f21dc5b96421f3b2ef','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 08:04:23'),('c3196bd4f6740b866cbfe59be267c3f2','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:13:06'),('ce4b33bec9ca06db82fe220b47f11389','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 13:23:39'),('e116a4db31f92d2ff9980adce8063ea9','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 08:05:12'),('f3df662776242f69a2ed8ecb305ad39c','M2U3NmY4YzE1MjZkNjhkODAyMDFjM2E5YTJjMDE0OGJiZDU0ZGZlMDqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2012-10-15 07:34:50'),('f3f80ec134a2f9f2d64fbb8154032121','YjUxMzFhZjNhNjRmNjlmNDFlOTA2MzAxNWYyOWY3ZDA5OWVkNGJlNjqAAn1xAS4=\n','2012-10-13 19:37:19');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovation`
--

DROP TABLE IF EXISTS `innovation_innovation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `guide_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `innovation_innovation_application_id_439fd96ba4fff957_uniq` (`application_id`),
  KEY `innovation_innovation_398529ef` (`application_id`),
  KEY `innovation_innovation_39ece575` (`guide_id`),
  CONSTRAINT `application_id_refs_id_140ec2681d8654ac` FOREIGN KEY (`application_id`) REFERENCES `innovation_innovationapplication` (`id`),
  CONSTRAINT `guide_id_refs_id_20e340ecfd3ea291` FOREIGN KEY (`guide_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovation`
--

LOCK TABLES `innovation_innovation` WRITE;
/*!40000 ALTER TABLE `innovation_innovation` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovationapplication`
--

DROP TABLE IF EXISTS `innovation_innovationapplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovationapplication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_of_submission` datetime NOT NULL,
  `year_of_submission` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `abstract` varchar(100) DEFAULT NULL,
  `reviewer_id` int(11) DEFAULT NULL,
  `review` longtext NOT NULL,
  `status` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `innovation_innovationapplication_d0f17e2b` (`reviewer_id`),
  CONSTRAINT `reviewer_id_refs_id_239db9abcf39ed10` FOREIGN KEY (`reviewer_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovationapplication`
--

LOCK TABLES `innovation_innovationapplication` WRITE;
/*!40000 ALTER TABLE `innovation_innovationapplication` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovationapplication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovationapplication_team_members`
--

DROP TABLE IF EXISTS `innovation_innovationapplication_team_members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovationapplication_team_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `innovationapplication_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `innovation_innova_innovationapplication_id_ec6205019b70b1f_uniq` (`innovationapplication_id`,`person_id`),
  KEY `innovation_innovationapplication_team_members_a36a7978` (`innovationapplication_id`),
  KEY `innovation_innovationapplication_team_members_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_id_281d092b430648b5` FOREIGN KEY (`person_id`) REFERENCES `people_person` (`id`),
  CONSTRAINT `innovationapplication_id_refs_id_3baade0e2dd8fa56` FOREIGN KEY (`innovationapplication_id`) REFERENCES `innovation_innovationapplication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovationapplication_team_members`
--

LOCK TABLES `innovation_innovationapplication_team_members` WRITE;
/*!40000 ALTER TABLE `innovation_innovationapplication_team_members` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovationapplication_team_members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovationpayment`
--

DROP TABLE IF EXISTS `innovation_innovationpayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovationpayment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `innovation_id` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `expense_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `innovation_innovationpayment_8d5e685f` (`innovation_id`),
  KEY `innovation_innovationpayment_5c5bdf45` (`expense_id`),
  CONSTRAINT `expense_id_refs_id_7bfa7077cf92d95f` FOREIGN KEY (`expense_id`) REFERENCES `accounts_expense` (`id`),
  CONSTRAINT `innovation_id_refs_id_50c9017658a0bfca` FOREIGN KEY (`innovation_id`) REFERENCES `innovation_innovation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovationpayment`
--

LOCK TABLES `innovation_innovationpayment` WRITE;
/*!40000 ALTER TABLE `innovation_innovationpayment` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovationpayment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovationupdate`
--

DROP TABLE IF EXISTS `innovation_innovationupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovationupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `innovation_id` int(11) NOT NULL,
  `date_of_update` date DEFAULT NULL,
  `update` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `innovation_innovationupdate_8d5e685f` (`innovation_id`),
  CONSTRAINT `innovation_id_refs_id_2fd54d6c3bd9d4c6` FOREIGN KEY (`innovation_id`) REFERENCES `innovation_innovation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovationupdate`
--

LOCK TABLES `innovation_innovationupdate` WRITE;
/*!40000 ALTER TABLE `innovation_innovationupdate` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovationupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovationupdateimage`
--

DROP TABLE IF EXISTS `innovation_innovationupdateimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovationupdateimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `innovation_update_id` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `caption` varchar(100) NOT NULL,
  `sort_order` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `innovation_innovationupdateimage_22cf19a` (`innovation_update_id`),
  CONSTRAINT `innovation_update_id_refs_id_3d94eb2fe1b8a04d` FOREIGN KEY (`innovation_update_id`) REFERENCES `innovation_innovationupdate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovationupdateimage`
--

LOCK TABLES `innovation_innovationupdateimage` WRITE;
/*!40000 ALTER TABLE `innovation_innovationupdateimage` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovationupdateimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `innovation_innovationupdatevideo`
--

DROP TABLE IF EXISTS `innovation_innovationupdatevideo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `innovation_innovationupdatevideo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `innovation_update_id` int(11) NOT NULL,
  `video` varchar(100) NOT NULL,
  `caption` varchar(100) NOT NULL,
  `sort_order` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `innovation_innovationupdatevideo_22cf19a` (`innovation_update_id`),
  CONSTRAINT `innovation_update_id_refs_id_3dfa68c528e9597f` FOREIGN KEY (`innovation_update_id`) REFERENCES `innovation_innovationupdate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `innovation_innovationupdatevideo`
--

LOCK TABLES `innovation_innovationupdatevideo` WRITE;
/*!40000 ALTER TABLE `innovation_innovationupdatevideo` DISABLE KEYS */;
/*!40000 ALTER TABLE `innovation_innovationupdatevideo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people_person`
--

DROP TABLE IF EXISTS `people_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `billing_address` longtext NOT NULL,
  `billing_landmark` varchar(100) NOT NULL,
  `billing_city` varchar(50) NOT NULL,
  `billing_state` varchar(50) NOT NULL,
  `billing_postal_code` varchar(30) NOT NULL,
  `billing_country` varchar(50) NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `is_nitw_alumni` tinyint(1) NOT NULL DEFAULT '0',
  `course` int(11) DEFAULT NULL,
  `department` int(11) DEFAULT NULL,
  `year_of_passing` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_682974c094ae2252` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_person`
--

LOCK TABLES `people_person` WRITE;
/*!40000 ALTER TABLE `people_person` DISABLE KEYS */;
INSERT INTO `people_person` VALUES (1,2,'Plot no.-64/A, H.n0.-9-5-32, S.G.R.Colony, Champapet, Hyderabad-500059','','Hyderabad','Andhra Pradesh','500059','India','9705813440',1,0,2,2015),(2,11,'Dorm 33, Room 29, IIM Ahmedabad\r\nAhmedabad,\r\nGujarat - 380015,\r\nIndia','','Ahmedabad','Gujarat','380015','India','9173645984',1,0,1,2011),(3,10,'STAFF No: 10530, BPCL KOCHI REFINERY AMBALAMUGAL, P.B.No:2\r\nKOCHI KERALA\r\n682302 India','','Kochi','Kerala','682302','India','8943566108',1,0,3,2011),(4,9,'103 , Sri rama residency , White Field\r\nHyderabad Andhra Pradesh\r\n500084 India','','Hyderabad','Andhra Pradesh','500084','India','9000416852',1,0,2,2012),(5,8,'Village Danthala Pally, Mandal Narsimhula Pet, Warangal, 506324','','Warangal','Andhra Pradesh','506324','India','9908492435',1,0,2,2012),(6,7,'2-116,Gangatharapuram,Komal(via),Mayiladudurai(T.K),TN 609805','','Mayiladudurai','Tamil Nadu','609805','India','8861416420',1,0,2,2012),(7,6,'s/o late Karunakar, Gandharlaguda, Nambal(village), Rebbena(mandal), Adilabad, Andhra Pradesh','','Rebbena','Andhra Pradesh','504292','India','9494282480',1,0,1,2012),(8,5,'Peddagonnuru post, Mudinepalli mandal, Krishna district, Andhra Pradesh','','Mudinepalli','Andhra Pradesh','521329 ','India','9966220161',1,0,3,2012),(9,4,'chak ohanati,Industrial area, Opp G K Cotton mill, Hajipur, Vishali, Bihar 844101','','Vishali','Bihar','844101','India','9835853802',1,0,7,2012),(10,3,'Perala, Chirala, Prakasam, Andhra Pradesh - 523157','','Chirala','Andhra Pradesh','523157','India','9347630003 ',1,0,1,2012),(11,14,'c/o Lavanya Tailorings,D.No:68-10-1, Vidyuth Nagar,Kakinada, East Godavari,AP','','Kakinada','Andhra Pradesh','533003','India','8121445134',1,0,1,2013),(12,15,'D.no:5-175/1,Gundlapalli(post),Nekarikallu(mandal),Guntur(dist)','','Nekarikallu','Andhra Pradesh','','India','9177210068',1,0,1,2013),(13,16,'t.timmapuram,tuni mondel,east godavari,a.p','','Tuni','Andhra Pradesh','','India','9963629795',1,0,0,2013),(14,17,'D.NO:13-2-19,POKURU ST,NEAR MAHALAKSHMI TEMPLE,CHINNA BAZAAR,NELLORE-524001','','POKURU','Andhra Pradesh','524001','India','8125924763',1,0,0,2014),(15,18,'S/O-RAJENDRA PRASAD,VILL+PO-URK-BANGRA(HATA).DIST-GOPALGANJ,PS-THAWE,PIN-841428','','GOPALGANJ','Bihar','841428','India','9014937934',1,0,2,2014),(16,19,'NEAR VAISHNO VATIKA,SURYA VIHAR COLONY,PINTO PARK-2,MORARA,GWALIOR,M.P.','','Gwalior','Madhya Pradesh','','India','7893665571',1,0,2,2014),(17,20,'near the Jain mandir, Juna biaora, Rajgrah dist,Madhya pradesh.\r\nPINCODE 465674\r\n','','Rajgrah','Madhya Pradesh','465674','India','9700484976',1,0,3,2014),(18,21,'H.No:1/45,Gudikal,yemmiganur,kurnool, A.P,518364','','Yemmiganur','Andhra Pradesh','518364','India','8500534838',1,0,0,2014),(19,22,'D-NO.-15-7-37;C/O CH.VENKATESWARA RAO;NANDI VELUGU ROAD,KUMMARI BAZAR,OLD GUNTUR, Guntur','','Old Guntur','Andhra Pradesh','','India','9247981827',1,0,2,2014),(20,23,'yerragudi palli(v),Pulivendula(m),Kadapa','','Pulivendula','Andhra Pradesh','','India','9866791548',1,0,2,2014),(21,13,'D-NO:12-297, AUTONAGAR, ELURU ROAD, JANGAREDDIGUDEM, W.G.DIST, AP.PIN:534447','','JANGAREDDIGUDEM','Andhra Pradesh','534447','India','9948833680',1,0,1,2010),(22,12,'b-385, deepanjali nagar, ntpc-simhadri, vishakhapatnam, andhra pradesh.','','vishakhapatnam','Andhra Pradesh','','India','9494181978',1,0,3,2010);
/*!40000 ALTER TABLE `people_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people_person_preference`
--

DROP TABLE IF EXISTS `people_person_preference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_person_preference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `is_subscribed_for_newsletter` tinyint(1) NOT NULL DEFAULT '1',
  `show_donations` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  CONSTRAINT `person_id_refs_id_3277e1492409cc1c` FOREIGN KEY (`person_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_person_preference`
--

LOCK TABLES `people_person_preference` WRITE;
/*!40000 ALTER TABLE `people_person_preference` DISABLE KEYS */;
/*!40000 ALTER TABLE `people_person_preference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people_teammember`
--

DROP TABLE IF EXISTS `people_teammember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people_teammember` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `fb_link` varchar(200) DEFAULT NULL,
  `linkedin_link` varchar(200) DEFAULT NULL,
  `twitter_link` varchar(200) DEFAULT NULL,
  `blog_link` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people_teammember`
--

LOCK TABLES `people_teammember` WRITE;
/*!40000 ALTER TABLE `people_teammember` DISABLE KEYS */;
INSERT INTO `people_teammember` VALUES (1,'Anand Rajagopalan','anand','Co-founder & CEO','team_pics/Anand_Rajagopalan_png.png','<p>Anand is from the NITW class of 2008. He worked as a developer for Oracle India for three and a half years before quitting to join Lakshya as a full-time employee. </p>\r\n<p>Today, he works as Lakshya\'s CEO. He conceptualizes projects and oversees their execution. He is also responsible for improving the synergy between alumni and institute by forging new partnerships. He heads the Innovation Project team and also looks into its IPR aspects. He is involved in nearly all activities from publicity to fund raising.</p>\r\n\r\n<p>During his college days Anand was the overall student coordinator of Spring Spree, NITW\'s three day cultural festival.</p>','https://www.facebook.com/anand.rajagopalan.547','http://in.linkedin.com/in/rajagopalananand','https://twitter.com/anandr31',''),(2,'Srihari Maneru','srihari','Co-founder & Trustee','team_pics/Sri_hari_PNG.png','Srihari, NITW class of 2008, is a co-founder of Lakshya. Soon after graduation, he joined Strand Life Sciences as Associate Software Developer before moving to Rang De, a microfinance NGO, where he grew to become Vice President. He now works as Member, Technical Staff for Boltell Infomedia.\r\n<p>At Lakshya, Srihari is responsible for all new technologies the organization adopts from developing the website, integrating analytics, payment-gateways to leading teams for developing software modules to assist in transparency.</p>\r\n<p>Srihari was student council president in 2008 at NIT Warangal.</p>','https://www.facebook.com/sriharimaneru','http://www.linkedin.com/pub/srihari-maneru/17/824/943','http://www.twitter.com/sriharimaneru','http://sriharimaneru.wordpress.com/'),(3,'Rakesh Dubbudu','rakesh','Trustee','team_pics/Rakesh_Dubbudu_png.png','Rakesh, NITW class of 2005, started out working for Oracle India and also founded Bhumi, an NGO working towards sustainable transformation of communities. He resigned from Oracle in 2010 to join Abhyaas EduCorp as its Director.\r\n<p>At Lakshya, Rakesh is responsible for the Asthra project. He develops the roadmap and oversees execution for assisting the NIT Warangal administration in making its processes more transparent and efficient. Some of his work includes implementing section 4(1)(b) of the RTI Act 2005 in the institute and preparing requirements for automation of processes.</p>\r\n<p>He is better known as an RTI activist with distinguished awards such as the CNN IBN Citizen Journalist Award and the Basha Memorial Young Activist Award. His interests include studying public policy and the RTI Act.</p>','https://www.facebook.com/dubbudu','http://www.linkedin.com/pub/rakesh-reddy-dubbudu/19/409/238','',''),(4,'Shailesh Rathi','shailesh','Executive Member','team_pics/Sailesh_Rathi_png.png','After working with Microsoft for 2 years, Shailesh, NITW class of 2008, received an admit to IIM Ahmedabad for the class of 2012.\r\n<p>At Lakshya, Shailesh is responsible for raising and managing funds. His role includes setting up strategy to ensure Lakshya\'s sustainability as regards funding.</p>\r\n<p>He is now working with IIM Ahemedabad as Consultant, Fund Raising to Office of the Dean (Alumni and External Relations) to raise funds for the institute. He is an avid cricketer and was part of the inter-IIM gold medal winning volleyball team.</p>','https://www.facebook.com/shailesh.rathi2305','http://www.linkedin.com/pub/shailesh-rathi/26/794/254','',''),(5,'Vrishank Raghav','vrishank','Trustee','team_pics/Vrishank_png.png','Vrishank, NITW class of 2008, is currently pursuing his PhD in Aerospace Engineering from Georgia Institute of Technology and has worked at Toyota and Kimberly Clark.\r\n<p>At Lakshya, he is responsible for fund raising strategies, especially from the Americas. He also played a key role in establishing the Innovation Project.</p>\r\n<p>He has received several awards such as the Robert Wolfe Fellowship (2012), United Technologies Research Center Fellowship (2011) and the Vertical Flight Foundation Fellowship (2010). He was captain of the NITW basketball team and member of the institute athelitics team.</p>','https://www.facebook.com/vrishankraghav','http://www.linkedin.com/pub/vrishank-raghav/32/5a2/a65','',''),(6,'Kalyan Varma','kalyan','Executive Member','team_pics/kalyan_verma_png.png','Kalyan, NITW class of 2008, worked for Goldman Sachs immediately after graduation and, after three years, quit to found SocialHeart.in, an online marketplace to buy exclusive products from NGOs. \r\n<p>At Lakshya, Kalyan works with the executive committee to develop strategy for growing Lakshya\'s reach within college and the alumni community. His role includes devising publicity drives and networking events.</p>\r\n<p>While in college, Kalyan was the overall student coordinator for Technozion, NITW\'s three day technical festival, in 2008.</p>','https://www.facebook.com/kalyanvarmak','http://www.linkedin.com/in/kalyanvarma','',''),(7,'Jaswant Adapa','jaswant','Student Coordinator','team_pics/Jaswant_Adapa_png.png','Jaswant is Lakshya\'s Student Coordinator responsible for strategizing and executing Lakshya projects in college. He is the head of the student team and is responsible for increasing Lakshya\'s reach in the institute. He is a Mechanical Engineering student from the Class of 2013.','https://www.facebook.com/jaswantadapa','','',''),(8,'Shine Eapen','shine','Associate Student Coordinator','team_pics/Shine_MathaiPNG.png','Shine is Lakshya\'s Associate Student Coordinator. His current role includes planning and organizing Lakshya events in college and working for Lakshya\'s accounts and finances.\r\n<p>He is a Mechanical Engineering student from the Class of 2014.</p>','https://www.facebook.com/shine.eapen','','',''),(9,'Prashant Sahu','prashanth','Chief Web Developer','team_pics/Prasnth_Sahu_png.png','Prashant is Lakshya\'s Chief Web Developer responsible for developing Lakshya\'s website and other software modules for its projects. He is a Computer Science student from the Class of 2014.','https://www.facebook.com/prashantsahu13','','',''),(10,'Arogya Koirala','arogya','Chief Designer','team_pics/Arogya_png.png','Arogya is Lakshya\'s Chief Designer responsible for conceptualizing and creating graphic designs. He is a Mechanical Engineering student from the Class of 2014.','https://www.facebook.com/bandukedai','','',''),(11,'Dr.J.Ramachander Rao','jrr','Honorary Chairperson','team_pics/jrr3_png.png','Dr.J.Ramachander Rao, better known as Dr.JRR, is the Honarary Chairperson of Lakshya.\r\nHe completed his MSc.Tech and PhD from REC Warangal in 1974 and 1980 respectively.\r\n<p>His contributions in helping Lakshya strategize its projects in college during the initial days have been invaluable. Having held almost every position of responsibility in the college administration from department HoD, to Chief Warden, to the Dean, Dr.JRR is well versed with the processes required to keep an organization\'s operations transparent and efficient. </p>\r\n<p>He is curently a professor at the Department of Physics and the Chief Vigilence Officer at NIT Warangal.</p>','','','',''),(12,'Dr.A.Venu Gopal','venugopal','Faculty Head, Innovation Project','team_pics/Dr_V_Gopal_png.png','Dr.Venu Gopal is the Faculty Head for the Innovation Project. He completed his post-graduation from REC Warangal in 1990 and received his doctorate in Manufacturing Engineering from IIT Delhi in 2003.\r\n\r\n<p>His contribution to structure the innovation project has been invaluable. He uses his vast experience to frame effective models for encouraging research and innovation among students.</p>\r\n\r\n<p>Dr.Venu Gopal is a Professor in the Mechanical Engineering Department at NIT Warangal.</p>','https://www.facebook.com/venugopal.anne.5','','',''),(13,'Dr.K.Padma','padma','Managing Trustee','team_pics/padma.jpg','Dr.K.Padma is Lakshya\'s Managing Trustee. After an MA in Economics from Kakatiya University, Dr.Padma received her PhD from IIT Kharagpur in 1991. \r\n\r\n<p>She helped set up Lakshya\'s transparency and accounting frameworks. She looks after Lakshya\'s auditing and filing of returns. She is also part of Lakshya\'s administration automation team. </p>\r\n\r\n<p>She is currently Associate Professor at the NIT Warangal School of Management and has the additional charge of Deputy Registrar, Accounts at NIT Warangal.</p>','','','',''),(14,'Mr.Venkat Changavalli','venkat','Advisor','team_pics/Venkat_Changavalli.png','Mr.Venkat Changavalli completed his B.Tech from REC Warangal in 1975 followed by an MBA from IIM Ahmedabad. The highlight of his 34 years of experience was as CEO of EMRI. Under his leadership, the EMRI 108 ambulance service has responded to over 12 million emergencies and saved over 350,000 lives.\r\n\r\n<p>His leadership and experience in guiding several start-ups makes his involvement as member of Lakshya\'s advisory board all the more vital.</p>\r\n\r\n<p>Mr.Venkat Changavalli is currently a management consultant, leadership mentor, teacher, inspirational speaker and is a Director at the State Bank of Hyderabad.</p>\r\n','https://www.facebook.com/venkat.changavalli','http://www.linkedin.com/pub/venkat-changavalli/2/713/537','',''),(15,'Mr.Vasant Roy','vasanth','Advisor','team_pics/Vasant_Roy_png.png','Mr.Vasant Roy graduated from REC Warangal in 1980 with a degree in Mechanical Engineering and then received his MBA from IIM Bangalore in 1982.\r\n\r\n<p>His association with Lakshya dates back to 2010 when he personally procured high-end parts from abroad for Lakshya\'s first sponsored research project. Being an entrepreneur himself with amazing people skills, he adds immense value as advisor.</p>\r\n<p>Mr.Vasant Roy is currently the owner of EFCO Maschinenbau India Pvt Ltd.</p>','','http://www.linkedin.com/pub/vasant-roy/5/434/b7b','','');
/*!40000 ALTER TABLE `people_teammember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_familydetail`
--

DROP TABLE IF EXISTS `scholarships_familydetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_familydetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `relation` int(11) DEFAULT NULL,
  `education` varchar(100) DEFAULT NULL,
  `occupation` varchar(200) DEFAULT NULL,
  `annualincome` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_familydetail_398529ef` (`application_id`),
  CONSTRAINT `application_id_refs_id_307d040e974eb82a` FOREIGN KEY (`application_id`) REFERENCES `scholarships_scholarshipapplication` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_familydetail`
--

LOCK TABLES `scholarships_familydetail` WRITE;
/*!40000 ALTER TABLE `scholarships_familydetail` DISABLE KEYS */;
INSERT INTO `scholarships_familydetail` VALUES (1,1,'M.Venkat Reddy',0,'Uneducated','Truck Driver','50000'),(2,2,'H CHANDRASEKHAR GOWD',0,'M.A','EXPIRED',''),(3,2,'H SASIKALA',1,'8th CLASS','EXPIRED',''),(4,2,'H VEDA MURTHY GOUD',3,'B.E','',''),(5,2,'H UMA MAHESHWARI',4,'B.E','SOFTWARE ENGINEER',''),(6,15,'',0,'-','Daily Labour','40000'),(7,15,'',1,'-','-','-'),(8,16,'',0,'-','Homemade Chips Business','40000'),(9,17,'',1,'','School Teacher','72000'),(10,18,'',0,'-','Agriculture','36000'),(11,19,'',0,'','Weaver','36000'),(12,20,'',0,'','Agriculture','40000'),(13,21,'Meena Upadhyay',1,'-','Housewife',''),(14,21,'Priyanka Upadhyay',4,'M.Sc','Student',''),(15,21,'Rupal Upadhyay',5,'B.Com','Student',''),(16,21,'Asuthosh Upadhyay',3,'8th Std','Student',''),(17,22,'',0,'-','-','-'),(18,22,'',1,'-','Washer woman','28000');
/*!40000 ALTER TABLE `scholarships_familydetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_gradeupdate`
--

DROP TABLE IF EXISTS `scholarships_gradeupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_gradeupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `academic_update_id` int(11) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `grade` varchar(2) NOT NULL,
  `comments` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_gradeupdate_8366dd44` (`academic_update_id`),
  CONSTRAINT `academic_update_id_refs_id_1ec56ff4096890b1` FOREIGN KEY (`academic_update_id`) REFERENCES `scholarships_scholaracademicupdate` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_gradeupdate`
--

LOCK TABLES `scholarships_gradeupdate` WRITE;
/*!40000 ALTER TABLE `scholarships_gradeupdate` DISABLE KEYS */;
/*!40000 ALTER TABLE `scholarships_gradeupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_otherexamperformance`
--

DROP TABLE IF EXISTS `scholarships_otherexamperformance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_otherexamperformance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `exam_name` varchar(100) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_otherexamperformance_398529ef` (`application_id`),
  CONSTRAINT `application_id_refs_id_2809a1bf67b9a1ba` FOREIGN KEY (`application_id`) REFERENCES `scholarships_scholarshipapplication` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_otherexamperformance`
--

LOCK TABLES `scholarships_otherexamperformance` WRITE;
/*!40000 ALTER TABLE `scholarships_otherexamperformance` DISABLE KEYS */;
INSERT INTO `scholarships_otherexamperformance` VALUES (1,1,'EAMCET',2011,'189'),(2,2,'IIT JEE',2007,'5177'),(3,2,'EAMCET',2007,'572');
/*!40000 ALTER TABLE `scholarships_otherexamperformance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_otherscholarship`
--

DROP TABLE IF EXISTS `scholarships_otherscholarship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_otherscholarship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `comments` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_otherscholarship_398529ef` (`application_id`),
  CONSTRAINT `application_id_refs_id_2e02b64e0fd1c3a7` FOREIGN KEY (`application_id`) REFERENCES `scholarships_scholarshipapplication` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_otherscholarship`
--

LOCK TABLES `scholarships_otherscholarship` WRITE;
/*!40000 ALTER TABLE `scholarships_otherscholarship` DISABLE KEYS */;
/*!40000 ALTER TABLE `scholarships_otherscholarship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_repayment`
--

DROP TABLE IF EXISTS `scholarships_repayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_repayment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scholar_id` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date_of_repayment` date NOT NULL,
  `transacation_type` int(11) NOT NULL,
  `transaction_details` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_repayment_5371e0eb` (`scholar_id`),
  CONSTRAINT `scholar_id_refs_id_760ff51893b7c0ac` FOREIGN KEY (`scholar_id`) REFERENCES `scholarships_scholar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_repayment`
--

LOCK TABLES `scholarships_repayment` WRITE;
/*!40000 ALTER TABLE `scholarships_repayment` DISABLE KEYS */;
/*!40000 ALTER TABLE `scholarships_repayment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_scholar`
--

DROP TABLE IF EXISTS `scholarships_scholar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_scholar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `donation_fund_id` int(11) DEFAULT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_scholar_398529ef` (`application_id`),
  KEY `scholarships_scholar_ce239fc1` (`donation_fund_id`),
  KEY `scholarships_scholar_21b911c5` (`person_id`),
  CONSTRAINT `donation_fund_id_refs_id_2580696e956e2d6c` FOREIGN KEY (`donation_fund_id`) REFERENCES `accounts_donationfund` (`id`),
  CONSTRAINT `application_id_refs_id_2f0bf6d1bc047942` FOREIGN KEY (`application_id`) REFERENCES `scholarships_scholarshipapplication` (`id`),
  CONSTRAINT `person_id_refs_id_53867319ba5edbb5` FOREIGN KEY (`person_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_scholar`
--

LOCK TABLES `scholarships_scholar` WRITE;
/*!40000 ALTER TABLE `scholarships_scholar` DISABLE KEYS */;
INSERT INTO `scholarships_scholar` VALUES (1,1,7,1),(2,6,3,10),(3,21,3,16),(4,15,2,20),(5,22,9,17),(6,19,2,18),(7,18,2,13),(8,17,10,19),(9,20,8,15),(10,16,4,14),(11,13,5,11),(12,14,6,12),(13,12,1,4),(14,2,NULL,3),(15,3,NULL,2),(16,4,NULL,21),(17,5,NULL,22),(18,7,NULL,7),(19,8,NULL,6),(20,9,NULL,8),(21,10,NULL,5),(22,11,NULL,9);
/*!40000 ALTER TABLE `scholarships_scholar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_scholaracademicupdate`
--

DROP TABLE IF EXISTS `scholarships_scholaracademicupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_scholaracademicupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scholar_id` int(11) NOT NULL,
  `sgpa` decimal(4,2) NOT NULL,
  `cgpa` decimal(4,2) NOT NULL,
  `comments` longtext NOT NULL,
  `semester` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_scholaracademicupdate_5371e0eb` (`scholar_id`),
  CONSTRAINT `scholar_id_refs_id_68619427469ecefd` FOREIGN KEY (`scholar_id`) REFERENCES `scholarships_scholar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_scholaracademicupdate`
--

LOCK TABLES `scholarships_scholaracademicupdate` WRITE;
/*!40000 ALTER TABLE `scholarships_scholaracademicupdate` DISABLE KEYS */;
INSERT INTO `scholarships_scholaracademicupdate` VALUES (1,14,8.88,8.88,'',1),(2,14,8.50,8.69,'',2),(3,14,9.56,8.99,'',3),(4,14,9.15,9.03,'',4),(5,14,8.92,9.01,'',5),(6,14,9.04,9.01,'',6),(7,14,8.99,9.00,'',7),(8,14,8.88,9.00,'',8),(9,4,6.09,6.09,'',1),(10,4,6.10,6.00,'',2),(11,4,5.69,5.96,'',3),(12,10,9.30,9.30,'',1),(13,10,9.30,9.30,'',2),(14,10,8.77,9.14,'',3),(15,12,7.31,7.31,'',1),(16,12,7.12,7.22,'',2),(17,12,7.64,7.36,'',3),(18,12,7.36,7.36,'',4),(19,12,7.35,7.36,'',5),(20,8,8.00,8.00,'',1),(21,8,8.00,8.00,'',2),(22,8,7.85,7.95,'',3),(23,7,8.62,8.62,'',1),(24,7,8.58,8.60,'',2),(25,7,7.58,8.26,'',3),(26,7,7.67,8.11,'',4),(27,7,7.48,7.96,'',5),(28,6,6.38,6.38,'',1),(29,6,5.31,5.37,'',2),(30,15,8.54,8.54,'',1),(31,15,8.46,8.60,'',2),(32,15,9.00,8.68,'',3),(33,15,8.85,8.72,'',4),(34,15,8.00,8.58,'',5),(35,15,8.92,8.63,'',6),(36,15,8.62,8.63,'',7),(37,15,9.31,8.73,'',8),(38,9,7.46,7.46,'',1),(39,9,6.85,7.16,'',2),(40,9,6.54,6.95,'',3),(41,3,9.69,9.69,'',1),(42,3,9.92,9.80,'',2),(43,3,8.54,9.38,'',3),(44,17,8.42,8.42,'',1),(45,17,8.62,8.52,'',2),(46,17,8.19,8.41,'',3),(47,17,8.56,8.46,'',4),(48,17,8.35,8.42,'',5),(49,17,8.52,8.44,'',6),(50,17,8.09,8.40,'',7),(51,17,7.77,8.37,'',8),(52,16,8.12,8.12,'',1),(53,16,8.23,8.17,'',2),(54,16,8.21,8.19,'',3),(55,16,8.67,8.31,'',4),(56,16,8.73,8.39,'',5),(57,16,8.57,8.42,'',6),(58,16,8.78,8.46,'',7),(59,16,9.18,8.51,'',8),(60,13,8.88,8.88,'',1),(61,13,9.12,9.00,'',2),(62,13,8.38,8.79,'',3),(63,13,8.38,8.69,'',4),(64,13,7.92,8.54,'',5),(65,13,7.67,8.40,'',6),(66,13,7.33,8.27,'',7),(67,13,7.88,8.24,'',8),(68,20,8.69,8.69,'',1),(69,20,8.46,8.57,'',2),(70,20,8.96,8.71,'',3),(71,20,8.65,8.69,'',4),(72,20,8.42,0.00,'',5),(73,20,8.24,8.57,'',6),(74,20,9.16,8.73,'',7),(75,20,8.40,8.74,'',8),(76,21,9.31,9.31,'',1),(77,21,8.38,8.85,'',2),(78,21,8.69,8.79,'',3),(79,21,8.23,8.65,'',4),(80,21,8.96,0.00,'',5),(81,21,8.00,8.60,'',6),(82,21,7.86,8.51,'',7),(83,21,8.00,8.47,'',8),(84,5,6.77,6.77,'',1),(85,5,7.15,6.96,'',2),(86,5,7.04,6.99,'',3),(87,22,0.00,0.00,'',1),(88,22,0.00,0.00,'',2),(89,22,0.00,0.00,'',3),(90,22,0.00,0.00,'',4),(91,22,0.00,0.00,'',5),(92,22,0.00,0.00,'',6),(93,22,0.00,6.77,'',7),(94,22,7.61,6.80,'',7),(95,22,0.00,6.77,'',6),(96,22,7.75,6.88,'',8),(97,11,9.00,9.00,'',1),(98,11,9.38,9.19,'',2),(99,11,8.79,0.00,'',3),(100,11,9.07,9.06,'',4),(101,11,9.04,9.05,'',5),(102,2,9.00,9.00,'',1),(103,2,8.88,8.94,'',2),(104,2,8.78,8.89,'',3),(105,2,8.07,8.68,'',4),(106,2,8.07,8.52,'',5),(107,2,8.23,8.47,'',6),(108,20,7.86,8.40,'',7),(109,2,7.86,8.36,'',8),(110,19,9.27,9.27,'',1),(111,19,9.15,9.21,'',2),(112,19,9.00,9.14,'',3),(113,19,9.00,9.11,'',4),(114,19,9.04,0.00,'',5),(115,19,8.96,9.07,'',6),(116,19,8.71,9.03,'',7),(117,19,8.25,8.96,'',8),(118,18,7.58,7.58,'',1),(119,18,6.85,7.22,'',2),(120,18,7.68,7.49,'',3),(121,18,6.50,7.16,'',4),(122,18,7.23,0.00,'',5),(123,18,7.96,7.31,'',6),(124,18,8.62,7.46,'',7),(125,11,8.77,9.00,'',6),(126,9,7.15,7.00,'',4),(127,3,8.68,9.21,'',4),(128,12,7.50,7.38,'',6);
/*!40000 ALTER TABLE `scholarships_scholaracademicupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_scholarshipapplication`
--

DROP TABLE IF EXISTS `scholarships_scholarshipapplication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_scholarshipapplication` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `date_of_submission` datetime DEFAULT NULL,
  `year_of_submission` int(11) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `sex` int(11) DEFAULT NULL,
  `roll_num` int(11) DEFAULT NULL,
  `hostel_address` longtext,
  `parent_contact` varchar(20) DEFAULT NULL,
  `ssc_board` int(11) DEFAULT NULL,
  `ssc_batch` int(11) DEFAULT NULL,
  `ssc_percentage` decimal(5,2) DEFAULT NULL,
  `ssc_school_name` varchar(100) DEFAULT NULL,
  `ssc_school_address` longtext,
  `ssc_school_type` int(11) DEFAULT NULL,
  `intermediate_board` int(11) DEFAULT NULL,
  `intermediate_batch` int(11) DEFAULT NULL,
  `intermediate_percentage` decimal(5,2) DEFAULT NULL,
  `intermediate_college_name` varchar(100) DEFAULT NULL,
  `intermediate_college_address` longtext,
  `intermediate_college_type` int(11) DEFAULT NULL,
  `aieee_air` int(11) DEFAULT NULL,
  `has_two_wheeler` tinyint(1) NOT NULL DEFAULT '0',
  `has_four_wheeler` tinyint(1) NOT NULL DEFAULT '0',
  `has_tv` tinyint(1) NOT NULL DEFAULT '0',
  `has_fridge` tinyint(1) NOT NULL DEFAULT '0',
  `has_washing_machine` tinyint(1) NOT NULL DEFAULT '0',
  `house_ownership` int(11) DEFAULT NULL,
  `house_type` int(11) DEFAULT NULL,
  `agriculture_land` varchar(50) DEFAULT NULL,
  `other_asset` longtext,
  `question1` longtext,
  `question2` longtext,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_scholarshipapplication_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_id_574de11bc90b0c32` FOREIGN KEY (`person_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_scholarshipapplication`
--

LOCK TABLES `scholarships_scholarshipapplication` WRITE;
/*!40000 ALTER TABLE `scholarships_scholarshipapplication` DISABLE KEYS */;
INSERT INTO `scholarships_scholarshipapplication` VALUES (1,1,'2012-10-20 16:00:59',2012,'1993-10-19',1,11033,'CB306, Ladies Hostel','9966381240',1,2009,95.00,'Hyderabad Sainik School','Hyderabad, Andhra Pradesh',0,1,2011,97.00,'Narayana Junior College','Hyderabad, Andhra Pradesh',0,2509,0,0,1,0,0,1,0,'0','','Taken loan from money lender. Uncle provides surety. Uncle us into real estate. Tried for Mural Mohan scholarship, but the scheme was withdrawn.','Continue with money lender',4),(2,3,'2012-10-20 16:00:59',2012,'1990-04-02',0,7321,'Room No : 2318, 1K Mega Hall, NIT Hostels, NIT Warangal.','09886339689',0,2005,95.00,'Jawahar Navodaya Vidyalaya','Jawahar Navodaya Vidyalaya, Lepakshi, Anantapur, Andhra Pradesh',1,0,2005,95.50,'SKVS Junior Kalasala','SKVS Junior Kalasala, Vijayawada, Andhra Pradesh',0,3835,0,0,1,0,0,1,0,'1.5','','MHRD sponsored till 10th. It was minimal fee for intermediate','',4),(3,2,'2012-10-20 16:00:59',2012,'1990-07-05',0,7214,'','9989883758',0,2005,NULL,'','',0,0,2005,NULL,'','',0,NULL,0,0,0,0,0,NULL,NULL,'','','','',4),(4,21,'2012-10-20 16:00:59',2012,'1988-05-25',0,6248,'20-A, COROMANDEL PARK, COROMANDEL INTERNATIONAL, SRIHARIPURAM, MALKAPURAM POST, VISAKHAPATNAM, AP.PIN:530011','9948805648',NULL,2004,88.50,'','',0,NULL,2006,96.60,'','',0,1829,0,0,0,0,0,NULL,NULL,'','','','',4),(5,22,'2012-10-20 16:00:59',2012,'1987-04-09',0,6321,'b-385, deepanjali nagar, ntpc-simhadri, vishakhapatnam, andhra pradesh.','9493293641',0,2005,82.60,'','',0,0,2005,97.80,'','',0,3659,0,0,0,0,0,NULL,NULL,'','','','',4),(6,10,'2012-10-20 16:01:00',2012,'1991-08-23',0,8214,'1k hall,room no.1648','905220185',0,2005,94.17,'','',0,0,2005,96.30,'','',0,3863,0,0,0,0,0,NULL,NULL,'','','','',4),(7,7,'2012-10-20 16:01:00',2012,'1988-06-10',0,8226,'1K hall,NIT hostlel,NIT Warangal','9849345725',0,2005,89.40,'','',0,0,2005,83.20,'','',0,38796,0,0,0,0,0,NULL,NULL,'','','','',4),(8,6,'2012-10-20 16:01:00',2012,'1989-07-30',1,8718,'','0435 2469063',0,2005,89.20,'','',0,0,2005,93.00,'','',0,2221,0,0,0,0,0,NULL,NULL,'','','','',4),(9,8,'2012-10-20 16:01:00',2012,'1991-07-30',0,8399,'13-1-64,NIT hostels,Warangal.','8677283303',0,2005,92.30,'','',0,0,2005,95.70,'','',0,3021,0,0,0,0,0,NULL,NULL,'','','','',4),(10,5,'2012-10-20 16:01:00',2012,'1988-10-14',0,8709,'Room No. 1603, 1K hall, NITW Hostels,NITWarangal,506004.','',0,2006,94.80,'','',0,0,2008,97.40,'','',0,2368,0,0,0,0,0,NULL,NULL,'','','','',4),(11,9,'2012-10-20 16:01:00',2012,NULL,0,8873,'','',0,2005,71.00,'','',0,0,2005,61.00,'','',0,45708,0,0,0,0,0,NULL,NULL,'','','','',4),(12,4,'2012-10-20 16:01:00',2012,'1988-05-31',0,8750,'13-2-62, Rajendra Prasad Hall, NIT hostels, NITW, Warangal','',0,2005,71.00,'','',0,0,2005,75.00,'','',0,3835,0,0,0,0,0,NULL,NULL,'','','','',4),(13,11,'2012-10-20 16:01:00',2012,'1992-08-08',1,9279,'room no:RW-206,ladies hostel,NITW','9912307191',0,2005,93.10,'','',0,0,2005,97.80,'','',0,3863,0,0,0,0,0,NULL,NULL,'','','','',4),(14,12,'2012-10-20 16:01:00',2012,'1992-08-25',0,9276,'1434,1k Hall,nitw','9849939191',0,2005,92.66,'','',0,0,2005,94.00,'','',0,6502,0,0,0,0,0,NULL,NULL,'','','','',4),(15,20,'2012-10-20 16:01:00',2012,'1993-03-04',0,107159,'','9866404129',1,NULL,91.10,'','',0,1,NULL,93.20,'','',0,55549,0,0,0,0,0,NULL,NULL,'','','','',4),(16,14,'2012-10-20 16:01:00',2012,'1993-01-21',0,104214,'Room no:4-2-4, NITW Hostels,Wwarangal,A.P.','9030874230',1,NULL,86.50,'','',0,1,NULL,97.00,'','',0,2410,0,0,0,0,0,NULL,NULL,'','','','',4),(17,19,'2012-10-20 16:01:00',2012,'1993-07-16',0,107108,'ROOM NO.-4-2-16;BHABHA HALL ,NIT W','9290534853',1,NULL,91.00,'','',0,1,NULL,96.00,'','',0,7387,0,0,0,0,0,NULL,NULL,'','','','',4),(18,13,'2012-10-20 16:01:00',2012,'1992-05-24',0,9047,'room no: 1234, 1k hostel, NITW Hostels','9290920013',1,NULL,93.50,'','',0,1,NULL,97.80,'','',0,2416,0,0,0,0,0,NULL,NULL,'','','','',4),(19,18,'2012-10-20 16:01:00',2012,'1993-05-27',0,104102,'Room 6.1.9, NITW Hostels','9393675787',1,NULL,88.50,'','',0,1,NULL,94.60,'','',0,6556,0,0,0,0,0,NULL,NULL,'','','','',4),(20,15,'2012-10-20 16:01:00',2012,'1990-12-03',0,107246,'ULTRAMEGA HOSTEL ,R.NO-B8-09, NITW','8294263691',0,NULL,64.00,'','',0,0,NULL,73.00,'','',0,41605,0,0,0,0,0,NULL,NULL,'','','','',4),(21,16,'2012-10-20 16:01:00',2012,'1991-11-10',0,107239,'NITW Hostels','9200982227',1,NULL,95.40,'','',0,1,NULL,92.40,'','',0,2840,0,0,0,0,0,NULL,NULL,'','','','',4),(22,17,'2012-10-20 16:01:00',2012,'1990-09-25',0,103221,'NITW Hostels','7828311995',1,NULL,86.00,'','',0,1,NULL,80.00,'','',0,7579,0,0,0,0,0,NULL,NULL,'','','','',4);
/*!40000 ALTER TABLE `scholarships_scholarshipapplication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_scholarshippayment`
--

DROP TABLE IF EXISTS `scholarships_scholarshippayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_scholarshippayment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scholar_id` int(11) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `semester` int(11) NOT NULL DEFAULT '3',
  `payment_reason` int(11) NOT NULL DEFAULT '1',
  `expense_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_scholarshippayment_5371e0eb` (`scholar_id`),
  KEY `scholarships_scholarshippayment_5c5bdf45` (`expense_id`),
  CONSTRAINT `expense_id_refs_id_529c06dba346f167` FOREIGN KEY (`expense_id`) REFERENCES `accounts_expense` (`id`),
  CONSTRAINT `scholar_id_refs_id_2115857e191328a8` FOREIGN KEY (`scholar_id`) REFERENCES `scholarships_scholar` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_scholarshippayment`
--

LOCK TABLES `scholarships_scholarshippayment` WRITE;
/*!40000 ALTER TABLE `scholarships_scholarshippayment` DISABLE KEYS */;
/*!40000 ALTER TABLE `scholarships_scholarshippayment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_scholarshipverification`
--

DROP TABLE IF EXISTS `scholarships_scholarshipverification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_scholarshipverification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `verifier_id` int(11) NOT NULL,
  `met_applicant` tinyint(1) NOT NULL DEFAULT '0',
  `met_father` tinyint(1) NOT NULL DEFAULT '0',
  `met_mother` tinyint(1) NOT NULL DEFAULT '0',
  `met_siblings` tinyint(1) NOT NULL DEFAULT '0',
  `met_relatives` tinyint(1) NOT NULL DEFAULT '0',
  `met_neighbours` tinyint(1) NOT NULL DEFAULT '0',
  `house_ownership_type` int(11) DEFAULT NULL,
  `house_type` int(11) DEFAULT NULL,
  `has_tv` tinyint(1) NOT NULL DEFAULT '0',
  `has_fridge` tinyint(1) NOT NULL DEFAULT '0',
  `has_washing_machine` tinyint(1) NOT NULL DEFAULT '0',
  `has_air_cooler` tinyint(1) NOT NULL DEFAULT '0',
  `has_air_conditioner` tinyint(1) NOT NULL DEFAULT '0',
  `vehicles_owned` varchar(200) DEFAULT NULL,
  `father_details` longtext,
  `mother_details` longtext,
  `sibling_details` longtext,
  `question1` longtext,
  `question2` longtext,
  `aware_repayment_model` int(11) DEFAULT NULL,
  `aware_renewal_criteria` int(11) DEFAULT NULL,
  `final_recommendation` int(11) DEFAULT NULL,
  `additional_comment` longtext,
  `status` int(11) DEFAULT NULL,
  `date_of_verfication` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_scholarshipverification_398529ef` (`application_id`),
  KEY `scholarships_scholarshipverification_a7bedd26` (`verifier_id`),
  CONSTRAINT `application_id_refs_id_33788438abae255b` FOREIGN KEY (`application_id`) REFERENCES `scholarships_scholarshipapplication` (`id`),
  CONSTRAINT `verifier_id_refs_id_7e5451d5475aedf2` FOREIGN KEY (`verifier_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_scholarshipverification`
--

LOCK TABLES `scholarships_scholarshipverification` WRITE;
/*!40000 ALTER TABLE `scholarships_scholarshipverification` DISABLE KEYS */;
/*!40000 ALTER TABLE `scholarships_scholarshipverification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_scholarupdate`
--

DROP TABLE IF EXISTS `scholarships_scholarupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_scholarupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scholar_id` int(11) NOT NULL,
  `date_of_update` date DEFAULT NULL,
  `update` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_scholarupdate_5371e0eb` (`scholar_id`),
  CONSTRAINT `scholar_id_refs_id_1700089d8a20454e` FOREIGN KEY (`scholar_id`) REFERENCES `scholarships_scholar` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_scholarupdate`
--

LOCK TABLES `scholarships_scholarupdate` WRITE;
/*!40000 ALTER TABLE `scholarships_scholarupdate` DISABLE KEYS */;
INSERT INTO `scholarships_scholarupdate` VALUES (1,1,'2012-09-03','old update ad fa sdf as df asdf asd fa sdf as df sad fas df as df asdf asf as df as f sad'),(2,1,'2012-10-02','new e ad fa sdf as df asdf asd fa sdf as df sad fas df as df asdf asf as df as f sadold update ad fa sdf as df asdf asd fa sdf as df sad fas df as df asdf asf as df as f sad');
/*!40000 ALTER TABLE `scholarships_scholarupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `scholarships_sgpa`
--

DROP TABLE IF EXISTS `scholarships_sgpa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scholarships_sgpa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `application_id` int(11) NOT NULL,
  `semester` int(11) DEFAULT NULL,
  `sgpa` decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `scholarships_sgpa_398529ef` (`application_id`),
  CONSTRAINT `application_id_refs_id_317691f45b3394da` FOREIGN KEY (`application_id`) REFERENCES `scholarships_scholarshipapplication` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `scholarships_sgpa`
--

LOCK TABLES `scholarships_sgpa` WRITE;
/*!40000 ALTER TABLE `scholarships_sgpa` DISABLE KEYS */;
INSERT INTO `scholarships_sgpa` VALUES (1,2,1,8.88),(2,2,2,8.50),(3,2,3,9.56),(4,2,4,9.15),(5,2,5,8.92),(6,2,6,9.04),(7,2,7,8.99),(8,2,8,8.88),(9,3,1,8.54),(10,3,2,8.46),(11,3,3,9.00),(12,3,4,8.85),(13,3,5,8.00),(14,3,6,8.92),(15,3,7,8.62),(16,3,8,9.31),(17,4,1,8.12),(18,4,2,8.23),(19,4,3,8.21),(20,4,4,8.67),(21,4,5,8.73),(22,4,6,8.57),(23,4,7,8.78),(24,4,8,9.18),(25,5,1,8.42),(26,5,2,8.62),(27,5,3,8.19),(28,5,4,8.56),(29,5,5,8.35),(30,5,6,8.52),(31,5,7,8.09),(32,5,8,7.77),(33,6,1,9.00),(34,6,2,8.88),(35,6,3,8.78),(36,6,4,8.07),(37,6,5,8.07),(38,6,6,8.23),(39,6,7,7.86),(40,6,8,7.86),(41,7,1,7.58),(42,7,2,6.85),(43,7,3,7.68),(44,7,4,6.50),(45,7,5,7.23),(46,7,6,7.96),(47,7,7,8.62),(48,8,1,9.27),(49,8,2,9.15),(50,8,3,9.00),(51,8,4,9.00),(52,8,5,9.04),(53,8,6,8.96),(54,8,7,8.71),(55,8,8,8.25),(56,9,1,8.69),(57,9,2,8.46),(58,9,3,8.96),(59,9,4,8.65),(60,9,5,8.42),(61,9,6,8.24),(62,9,7,9.16),(63,9,8,8.40),(64,10,1,9.31),(65,10,2,8.38),(66,10,3,8.69),(67,10,4,8.23),(68,10,5,8.96),(69,10,6,8.00),(70,10,7,7.86),(71,10,8,8.00),(72,11,1,NULL),(73,11,2,6.23),(74,11,3,6.62),(75,11,4,6.69),(76,11,5,7.00),(77,11,6,6.80),(78,11,7,7.61),(79,11,8,7.75),(80,12,1,8.88),(81,12,2,9.12),(82,12,3,8.38),(83,12,4,8.38),(84,12,5,7.92),(85,12,6,7.67),(86,12,7,7.33),(87,12,8,7.88),(88,13,1,9.00),(89,13,2,9.38),(90,13,3,8.79),(91,13,4,9.07),(92,13,5,9.04),(93,14,1,7.31),(94,14,2,7.12),(95,14,3,7.64),(96,14,4,7.36),(97,14,5,7.35),(98,15,1,6.09),(99,15,2,6.10),(100,15,3,5.69),(101,16,1,9.30),(102,16,2,9.30),(103,16,3,8.77),(104,18,1,8.62),(105,18,2,8.58),(106,18,3,7.58),(107,18,4,7.67),(108,18,5,7.48),(109,19,1,6.38),(110,19,2,NULL),(111,19,3,5.31),(112,20,1,7.46),(113,20,2,6.85),(114,20,3,6.54),(115,21,1,9.69),(116,21,2,9.92),(117,21,3,8.54),(118,22,1,6.77),(119,22,2,7.15),(120,22,3,7.04);
/*!40000 ALTER TABLE `scholarships_sgpa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'people','0001_initial','2012-09-20 11:21:18'),(2,'people','0002_auto__chg_field_person_course__chg_field_person_department__chg_field_','2012-09-20 11:21:18'),(3,'people','0003_auto__add_team','2012-09-20 11:21:18'),(4,'people','0004_auto__del_team__add_teammember','2012-09-20 11:21:18'),(5,'accounts','0001_initial','2012-09-20 11:21:19'),(6,'innovation','0001_initial','2012-09-20 11:21:19'),(7,'innovation','0002_auto__chg_field_innovationapplication_abstract__chg_field_innovationap','2012-09-20 11:21:19'),(8,'innovation','0003_auto__chg_field_innovationupdateimage_image','2012-09-20 11:21:19'),(9,'innovation','0004_auto__chg_field_innovation_application__add_unique_innovation_applicat','2012-09-20 11:21:19'),(10,'scholarships','0001_initial','2012-09-20 11:21:19'),(11,'scholarships','0002_auto__chg_field_otherscholarship_amount__chg_field_otherscholarship_co','2012-09-20 11:21:20'),(12,'scholarships','0003_auto__chg_field_scholarshipapplication_date_of_submission__del_field_s','2012-09-20 11:21:21'),(13,'scholarships','0004_auto__chg_field_scholarshipverification_house_ownership_type__chg_fiel','2012-09-20 11:21:21'),(14,'scholarships','0005_auto__add_field_scholarshipverification_status','2012-09-20 11:21:21'),(15,'scholarships','0006_auto__chg_field_scholarupdate_date_of_update__add_field_scholaracademi','2012-09-20 11:21:21'),(16,'scholarships','0007_auto__del_field_familydetail_occupation_annualincome__add_field_family','2012-09-20 11:21:21'),(17,'scholarships','0008_auto__chg_field_scholarshipverification_date_of_verfication','2012-09-20 11:21:21'),(18,'scholarships','0009_auto__del_field_scholarshipverification_date_of_verfication','2012-09-20 11:21:21'),(19,'scholarships','0010_auto__add_field_scholarshipverification_date_of_verfication','2012-09-20 11:21:21'),(20,'utils','0001_initial','2012-09-20 11:21:22'),(21,'utils','0002_auto__del_lakshyaupdates__del_lakskhyatestimonials__add_lakskhyatestim','2012-09-20 11:21:22'),(22,'utils','0003_auto__add_field_lakshyaupdate_photo','2012-09-20 11:21:22'),(23,'scholarships','0011_auto__chg_field_scholar_donation_fund','2012-09-30 14:32:51'),(24,'utils','0004_auto__chg_field_lakshyaupdate_date_of_entry__chg_field_lakshyaupdate_p','2012-09-30 14:32:51'),(25,'accounts','0002_auto__add_paymenttemp','2012-10-07 18:26:03');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utils_lakshyaupdate`
--

DROP TABLE IF EXISTS `utils_lakshyaupdate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `utils_lakshyaupdate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_text` longtext,
  `date_of_entry` date DEFAULT NULL,
  `sorting` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utils_lakshyaupdate`
--

LOCK TABLES `utils_lakshyaupdate` WRITE;
/*!40000 ALTER TABLE `utils_lakshyaupdate` DISABLE KEYS */;
INSERT INTO `utils_lakshyaupdate` VALUES (1,'Mr.Venkat Changavalli (RECW 1970-1975) and Mr.Vasant Roy (RECW 1975-1980) join Lakshya\'s Board of Advisors','2012-09-20',1,0,'update_pics/vc_vr.jpg'),(2,'After the alumni poured in over Rs.50,000 on this beautiful machine through Lakshya, NITW has sanctioned funds to pay for the patent application - a first of its kind collaboration!','2012-08-13',2,0,'update_pics/hovomarine-final.jpg'),(3,'Lakshya and NITW signed an MoU to be equal stake holder in Lakshya\'s Innovation Projects.','2012-07-18',3,0,'update_pics/DSCN0034.JPG'),(4,'The following innovative ideas were selected for the Innovation Project 2012-2013. These ideas will be jointly funded by NIT Warangal and Lakshya:<br/>\r\n<br/>\r\n1. Ferro Fibre Tie Confined Self Compacting Concrete for Improving Earthquake Resistance<br/>\r\n2. Bond Characteristics of GFRP Bars in Recycled Aggregate Concrete<br/>\r\n3. Nano-Silica Inclusions for Strength and Durability of Self Compacting Concrete<br/>\r\n4. Cloudsgreen.com<br/>\r\n5. Advanced Speech Recognition System for Home Appliances<br/>\r\n<br/>','2012-09-12',4,0,'update_pics/event.jpg'),(5,'Lakshya sponsored innovation project abstract has been shortlisted for the 3rd international conference for Sustainable Construction Materials and Technologies SCMT3, Kyoto, Japan.','2012-08-13',5,0,''),(6,'Academic Survey- 2012 report can be downloaded from the below links<br/>\r\n1. <a href = \"http://www.mediafire.com/?ro27ja9h6stb42o\">Full Report</a><br/>\r\n2. <a href = \"http://www.mediafire.com/?hlzf9bmq87pgfge\">Individual Chapters</a><br/>','2012-03-29',6,0,'update_pics/academicSurvey.jpg'),(7,'Joby Yeldo shows his gratitude to his teachers and friends. His invention, the \'Hovomarine\', was mentioned by the Director in his convocation address.\r\n<p>Lakshya has initiated the patent application process for the Hovomarine - the first Lakshya sponsored innovation project. This is a first for NIT Warangal.</p>','2012-09-16',7,0,'update_pics/mentionInBrochure.jpg');
/*!40000 ALTER TABLE `utils_lakshyaupdate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utils_lakskhyatestimonial`
--

DROP TABLE IF EXISTS `utils_lakskhyatestimonial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `utils_lakskhyatestimonial` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `testimonial_text` longtext,
  `person_id` int(11) NOT NULL,
  `designation` varchar(50) NOT NULL,
  `date_of_entry` date DEFAULT NULL,
  `sorting` int(11) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `utils_lakskhyatestimonial_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_id_6937d5dd311381b7` FOREIGN KEY (`person_id`) REFERENCES `people_person` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utils_lakskhyatestimonial`
--

LOCK TABLES `utils_lakskhyatestimonial` WRITE;
/*!40000 ALTER TABLE `utils_lakskhyatestimonial` DISABLE KEYS */;
/*!40000 ALTER TABLE `utils_lakskhyatestimonial` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-10-20 21:41:27
