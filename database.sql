-- Procházka Adam, C4c, prochazka7@spsejecna.cz
-- Databáze pro Pohřebnictví v MySQL workbench 8.0 CE

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

INSERT INTO `deceased` (`name`, `surname`, `date_of_birth`, `date_of_death`)
VALUES ('Jan', 'Novák', '1980-01-01', '2020-01-01'),
('Petr', 'Svoboda', '1970-01-01', '2020-01-01'),
('Marie', 'Kovářová', '1990-01-01', '2020-01-01'),
('Jana', 'Nováková', '1985-01-01', '2020-01-01'),
('Pavel', 'Svoboda', '1975-01-01', '2020-01-01'),
('Josef', 'Kovář', '1995-01-01', '2020-01-01'),
('Jiří', 'Novák', '1980-01-01', '2020-01-01'),
('Petr', 'Svoboda', '1970-01-01', '2020-01-01'),
('Marie', 'Kovářová', '1990-01-01', '2020-01-01'),
('Jana', 'Nováková', '1985-01-01', '2020-01-01'),
('Pavel', 'Svoboda', '1975-01-01', '2020-01-01'),
('Josef', 'Kovář', '1995-01-01', '2020-01-01');

INSERT INTO `funeral_service` (`name`, `price`)
VALUES ('Základní', 1000),
('Standardní', 2000),
('Luxusní', 3000);

INSERT INTO `participants` (`name`, `surname`, `relationship`)
VALUES ('Petr', 'Novák', 'family'),
('Marie', 'Svobodová', 'family'),
('Jana', 'Kovářová', 'family'),
('Pavel', 'Novák', 'friend'),
('Josef', 'Svoboda', 'friend'),
('Jiří', 'Kovář', 'friend'),
('Petr', 'Novák', 'family'),
('Marie', 'Svobodová', 'family'),
('Jana', 'Kovářová', 'family'),
('Pavel', 'Novák', 'other'),
('Josef', 'Svoboda', 'friend'),
('Jiří', 'Kovář', 'friend');

INSERT INTO `cemetery` (`name`, `address`)
VALUES ('Hřbitov', 'Praha'),
('Hřbitov', 'Brno'),
('Hřbitov', 'Ostrava'),
('Hřbitov', 'Plzeň'),
('Hřbitov', 'Liberec'),
('Hřbitov', 'Olomouc'),
('Hřbitov', 'Ústí nad Labem'),
('Hřbitov', 'Hradec Králové'),
('Hřbitov', 'Pardubice'),
('Hřbitov', 'Zlín'),
('Hřbitov', 'Jihlava'),
('Hřbitov', 'České Budějovice');

INSERT INTO `funeral` (`deceasedID`, `serviceID`, `cemeteryID`, `date`, `participantID`)
VALUES (1, 1, 1, '2020-01-01 12:00:00', 1),
(2, 2, 2, '2020-01-01 12:00:00', 2),
(3, 3, 3, '2020-01-01 12:00:00', 3),
(4, 1, 4, '2020-01-01 12:00:00', 4),
(5, 2, 5, '2020-01-01 12:00:00', 5),
(6, 3, 6, '2020-01-01 12:00:00', 6),
(7, 1, 7, '2020-01-01 12:00:00', 7),
(8, 2, 8, '2020-01-01 12:00:00', 8),
(9, 3, 9, '2020-01-01 12:00:00', 9),
(10, 1, 10, '2020-01-01 12:00:00', 10),
(11, 2, 11, '2020-01-01 12:00:00', 11),
(12, 3, 12, '2020-01-01 12:00:00', 12);
