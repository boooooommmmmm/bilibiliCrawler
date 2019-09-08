--
-- Table structure for table `bilibili_user_info_backup`
--

DROP TABLE IF EXISTS `bilibili_user_info_backup`;

CREATE TABLE `bilibili_user_info_backup` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mid` int(20) unsigned NOT NULL,
  `name` varchar(45) NOT NULL,
  `sex` varchar(45) NOT NULL,
  `rank` varchar(45) NOT NULL,
  `face` varchar(200) NOT NULL,
  `regtime` varchar(45) NOT NULL,
  `spacesta` varchar(45) NOT NULL,
  `birthday` varchar(45) NOT NULL,
  `sign` varchar(300) NOT NULL,
  `level` varchar(45) NOT NULL,
  `OfficialVerifyType` varchar(45) NOT NULL,
  `OfficialVerifyDesc` varchar(100) NOT NULL,
  `vipType` varchar(45) NOT NULL,
  `vipStatus` varchar(45) NOT NULL,
  `toutu` varchar(200) NOT NULL,
  `toutuId` int(20) unsigned NOT NULL,
  `coins` int(20) unsigned NOT NULL,
  `following` int(20) unsigned NOT NULL,
  `fans` int(20) unsigned NOT NULL,
  `archiveview` int(20) unsigned NOT NULL,
  `article` int(20) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bilibili_user_info_backup`
--

LOCK TABLES `bilibili_user_info_backup` WRITE;
/*!40000 ALTER TABLE `bilibili_user_info_backup` DISABLE KEYS */;
/*!40000 ALTER TABLE `bilibili_user_info_backup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
