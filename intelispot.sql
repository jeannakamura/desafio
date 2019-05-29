CREATE DATABASE IF NOT EXISTS intelipost;
USE intelipost;

DROP TABLE IF EXISTS `deploy_info`;

CREATE TABLE `deploy_infos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `component` varchar(30) NOT NULL,
  `version` varchar(30) NOT NULL,
  `owner` varchar(30) NOT NULL,
  `start` datetime DEFAULT NULL,
  `data` datetime DEFAULT NULL,
  `finish` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
)