
-- Databáze pro Pohřebnictví  v MySQL workbench 8.0 CE

-- Vytvoř 6 tabulek s různými datovými typy (float, bool, enum, string, datetime).
-- Implementuj alespoň jednu M:N vazbu mezi tabulkami.
-- Vytvoř alespoň dva pohledy (views).

CREATE DATABASE IF NOT EXISTS `funeral_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_czech_ci;

USE `funeral_db`;

CREATE TABLE IF NOT EXISTS `deceased` (
    `deceasedID` INT AUTO_INCREMENT PRIMARY KEY,
    `name` NVARCHAR(100) NOT NULL,
    `surname` NVARCHAR(100) NOT NULL,
    `date_of_birth` DATE NOT NULL,
    `date_of_death` DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS `funeral_service` (
    `serviceID` INT AUTO_INCREMENT PRIMARY KEY,
    `name` NVARCHAR(100) NOT NULL,
    `price` FLOAT NOT NULL
);

CREATE TABLE IF NOT EXISTS `participants` (
    `participantID` INT AUTO_INCREMENT PRIMARY KEY,
    `name` NVARCHAR(100) NOT NULL,
    `surname` NVARCHAR(100) NOT NULL,
    `relationship` ENUM('family', 'friend', 'other') NOT NULL
);

CREATE TABLE IF NOT EXISTS `cemetery` (
    `cemeteryID` INT AUTO_INCREMENT PRIMARY KEY,
    `name` NVARCHAR(100) NOT NULL,
    `address` NVARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS `funeral` (
    `funeralID` INT AUTO_INCREMENT PRIMARY KEY,
    `deceasedID` INT NOT NULL,
    `serviceID` INT NOT NULL,
    `cemeteryID` INT NOT NULL,
    `date` DATETIME NOT NULL,
    `participantID` INT,
    FOREIGN KEY (`deceasedID`) REFERENCES `deceased`(`deceasedID`),
    FOREIGN KEY (`serviceID`) REFERENCES `funeral_service`(`serviceID`),
    FOREIGN KEY (`cemeteryID`) REFERENCES `cemetery`(`cemeteryID`),
    FOREIGN KEY (`participantID`) REFERENCES `participants`(`participantID`)
);

CREATE TABLE IF NOT EXISTS `log` (
    `logID` INT AUTO_INCREMENT PRIMARY KEY,
    `date` DATETIME NOT NULL,
    `message` TEXT NOT NULL
);

CREATE VIEW `funeral_view` AS
SELECT `funeral`.`funeralID`, `deceased`.`name` AS `deceased_name`, `deceased`.`surname` AS `deceased_surname`, `funeral_service`.`name` AS `service_name`, `cemetery`.`name` AS `cemetery_name`, `funeral`.`date`
FROM `funeral`
JOIN `deceased` ON `funeral`.`deceasedID` = `deceased`.`deceasedID`
JOIN `funeral_service` ON `funeral`.`serviceID` = `funeral_service`.`serviceID`
JOIN `cemetery` ON `funeral`.`cemeteryID` = `cemetery`.`cemeteryID`;

CREATE VIEW `log_view` AS
SELECT `log`.`logID`, `log`.`date`, `log`.`message`
FROM `log`;