"""
Database:

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
"""

"""
Uživatelské rozhraní nebo API musí umožňovat:

    Vložení, smazání a úpravu nějaké informace, záznamu, který se ukládá do více než jedné tabulky.
    Provést transakci nad více než jednou tabulkou. Například převod kreditních bodů mezi dvěma účty apod.
    Vygenerovat souhrný report, který bude obsahovat smysluplná agregovaná data z alespoň tří tabulek Vaší databáze, např. počet součty nákupů podle měst apod. Report musí mít hlavičku a patičku.
    Import dat do min. dvou tabulek z formátu CSV, XML nebo JSON.
    Nastavit celý program v konfiguračním souboru config.ini.
"""

# Importy
import tkinter as tk
from tkinter import ttk
import mysql.connector

# Vytvoření okna
window = tk.Tk()
window.title("Funeral Services")
window.geometry("800x600")

# Vytvoření tabů
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab8 = ttk.Frame(tab_control)
tab9 = ttk.Frame(tab_control)
tab10 = ttk.Frame(tab_control)
tab11 = ttk.Frame(tab_control)
tab12 = ttk.Frame(tab_control)
tab13 = ttk.Frame(tab_control)
tab14 = ttk.Frame(tab_control)
tab15 = ttk.Frame(tab_control)
tab16 = ttk.Frame(tab_control)
tab17 = ttk.Frame(tab_control)
tab18 = ttk.Frame(tab_control)
tab19 = ttk.Frame(tab_control)
tab20 = ttk.Frame(tab_control)
tab21 = ttk.Frame(tab_control)
tab22 = ttk.Frame(tab_control)
tab23 = ttk.Frame(tab_control)
tab24 = ttk.Frame(tab_control)
tab25 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Deceased")
tab_control.add(tab2, text="Funeral Service")
tab_control.add(tab3, text="Participants")
tab_control.add(tab4, text="Cemetery")
tab_control.add(tab5, text="Funeral")
tab_control.add(tab6, text="Log")
tab_control.add(tab7, text="Funeral View")
tab_control.add(tab8, text="Log View")
tab_control.add(tab9, text="Insert Deceased")
tab_control.add(tab10, text="Insert Funeral Service")
tab_control.add(tab11, text="Insert Participant")
tab_control.add(tab12, text="Insert Cemetery")
tab_control.add(tab13, text="Insert Funeral")
tab_control.add(tab14, text="Insert Log")
tab_control.add(tab15, text="Update Deceased")
tab_control.add(tab16, text="Update Funeral Service")
tab_control.add(tab17, text="Update Participant")
tab_control.add(tab18, text="Update Cemetery")
tab_control.add(tab19, text="Update Funeral")
tab_control.add(tab20, text="Update Log")
tab_control.add(tab21, text="Delete Deceased")
tab_control.add(tab22, text="Delete Funeral Service")
tab_control.add(tab23, text="Delete Participant")
tab_control.add(tab24, text="Delete Cemetery")
tab_control.add(tab25, text="Delete Funeral")


# připojení do databáze
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="funeral_db"
)

cursor = db_connection.cursor()

# Vložení, smazání a úprava nějaké informace, záznamu, který se ukládá do více než jedné tabulky.
def insert_deceased():
    name = name_entry.get()
    surname = surname_entry.get()
    date_of_birth = date_of_birth_entry.get()
    date_of_death = date_of_death_entry.get()

    cursor.execute("INSERT INTO deceased (name, surname, date_of_birth, date_of_death) VALUES (%s, %s, %s, %s)", (name, surname, date_of_birth, date_of_death))
    db_connection.commit()

    log_message = f"Deceased {name} {surname} was inserted into the database."
    cursor.execute("INSERT INTO log (date, message) VALUES (NOW(), %s)", (log_message,))
    db_connection.commit()

    log_listbox.insert(tk.END, log_message)


