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
    Vygenerovat souhrný report, který bude obsahovat smysluplná agregovaná data z alespoň tří tabulek Vaší databáze. Report musí mít hlavičku a patičku.
    Import dat do min. dvou tabulek z formátu CSV, XML nebo JSON.
    Nastavit celý program v konfiguračním souboru config.ini.
"""

# Importy
import tkinter as tk
from tkinter import ttk, simpledialog
import mysql.connector

root = tk.Tk()
root.title("Funeral Service")

# Set the style for the GUI
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="black")
style.configure("TLabel", font=("Arial", 12), foreground="black")
style.configure("TEntry", font=("Arial", 12), foreground="black")

# Set the colors for the GUI
root.configure(bg="#F0F0F0")
style.configure("TButton", background="#4CAF50", foreground="black")
style.configure("TLabel", background="#F0F0F0")
style.configure("TEntry", background="white", foreground="black")

name_entry = ttk.Entry(root)
surname_entry = ttk.Entry(root)
date_of_birth_entry = ttk.Entry(root)
date_of_death_entry = ttk.Entry(root)
deceased_listbox = tk.Listbox(root)
log_listbox = tk.Listbox(root)


# připojení do databáze
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="funeral_db"
)

cursor = db_connection.cursor()

# Vložení, smazání a úprava nějaké informace, záznamu, který se ukládá do více než jedné tabulky.
class FuneralApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Funeral Database App")
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(self.root, text="Insert Deceased", command=self.show_insert_deceased).grid(row=0, column=0, sticky="w")
        ttk.Button(self.root, text="Delete Deceased", command=self.show_delete_deceased).grid(row=0, column=1, sticky="w")
        ttk.Button(self.root, text="Update Deceased", command=self.show_update_deceased).grid(row=0, column=2, sticky="w")

        ttk.Button(self.root, text="Summary Report", command=self.show_summary_report).grid(row=1, column=0, sticky="w")

        cursor.execute("SELECT * FROM `log_view`")
        log_list = cursor.fetchall()
        for log in log_list:
            log_listbox.insert(tk.END, log[1])

        log_listbox.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        log_listbox.configure(width=50, height=10)

    def show_insert_deceased(self):
        form = InsertDeceasedForm(self.root)

    def show_delete_deceased(self):
        form = DeleteDeceasedForm(self.root)

    def show_update_deceased(self):
        form = UpdateDeceasedForm(self.root)

    def show_summary_report(self):
        report = SummaryReport(self.root)
        report.generate_report()
# Vygenerovat souhrný report, který bude obsahovat smysluplná agregovaná data z alespoň tří tabulek Vaší databáze. Report musí mít hlavičku a patičku.
class SummaryReport:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Summary Report")

        self.report_label = ttk.Label(self.top, text="Summary Report")
        self.report_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.top.configure(bg="#F0F0F0")
        style.configure("TLabel", background="#F0F0F0")

    def generate_report(self):
        try:
            cursor.execute("SELECT AVG(`price`) FROM `funeral_service`")
            average_price = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM `deceased`")
            deceased_count = cursor.fetchone()[0]

            cursor.execute("SELECT AVG(DATEDIFF(`date_of_death`, `date_of_birth`)) FROM `deceased`")
            average_age = cursor.fetchone()[0]

            self.report_label["text"] = f"Average price of funeral service: {average_price}\n" \
                                        f"Number of deceased: {deceased_count}\n" \
                                        f"Average age of deceased: {average_age}"
            
        except Exception as e:
            self.report_label["text"] = f"Error: {str(e)}"
            log_listbox.insert(tk.END, f"Error during report generation: {str(e)}")
            
class InsertDeceasedForm:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Insert Deceased Form")

        self.name_label = ttk.Label(self.top, text="Name")
        self.surname_label = ttk.Label(self.top, text="Surname")
        self.date_of_birth_label = ttk.Label(self.top, text="Date of Birth")
        self.date_of_death_label = ttk.Label(self.top, text="Date of Death")

        self.name_entry = ttk.Entry(self.top)
        self.surname_entry = ttk.Entry(self.top)
        self.date_of_birth_entry = ttk.Entry(self.top)
        self.date_of_death_entry = ttk.Entry(self.top)

        self.insert_button = ttk.Button(self.top, text="Insert", command=self.insert_deceased)
        self.cancel_button = ttk.Button(self.top, text="Cancel", command=self.top.destroy)

        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.surname_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.date_of_birth_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.date_of_death_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        
        self.name_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.surname_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.date_of_birth_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        self.date_of_death_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        self.insert_button.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.cancel_button.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        self.top.configure(bg="#F0F0F0")
        style.configure("TButton", background="#4CAF50", foreground="black")
        style.configure("TLabel", background="#F0F0F0")
        style.configure("TEntry", background="white", foreground="black")

    def insert_deceased(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        date_of_death = self.date_of_death_entry.get()

        if name and surname and date_of_birth and date_of_death:
            cursor.execute("INSERT INTO `deceased` (`name`, `surname`, `date_of_birth`, `date_of_death`) VALUES (%s, %s, %s, %s)", (name, surname, date_of_birth, date_of_death))
            db_connection.commit()
            cursor.execute("INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Inserted deceased: {} {}')".format(name, surname))
            db_connection.commit()
            log_listbox.insert(tk.END, f"Inserted deceased: {name} {surname}")

        else:
            cursor.execute("INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Failed to insert deceased because of missing some filled out fields')")
            log_listbox.insert(tk.END, "All fields are required")

class DeleteDeceasedForm:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Delete Deceased Form")

        self.deceased_label = ttk.Label(self.top, text="Select Deceased")
        self.deceased_listbox = tk.Listbox(self.top)

        self.delete_button = ttk.Button(self.top, text="Delete", command=self.delete_deceased)
        self.cancel_button = ttk.Button(self.top, text="Cancel", command=self.top.destroy)

        self.deceased_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.deceased_listbox.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.delete_button.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.cancel_button.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.top.configure(bg="#F0F0F0")
        style.configure("TButton", background="#4CAF50", foreground="black")
        style.configure("TLabel", background="#F0F0F0")
        style.configure("TEntry", background="white", foreground="black")

        self.load_deceased()

    def load_deceased(self):
        cursor.execute("SELECT `deceasedID`, `name`, `surname` FROM `deceased`")
        deceased_list = cursor.fetchall()
        for deceased in deceased_list:
            self.deceased_listbox.insert(tk.END, f"{deceased[0]} - {deceased[1]} {deceased[2]}")

    def delete_deceased(self):
        selected_deceased = self.deceased_listbox.get(tk.ACTIVE)
        if selected_deceased:
            deceased_id = selected_deceased.split(" - ")[0]
            cursor.execute("DELETE FROM `deceased` WHERE `deceasedID` = %s", (deceased_id,))
            db_connection.commit()
            cursor.execute("INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Deleted deceased: {}')".format(selected_deceased))
            db_connection.commit()
            log_listbox.insert(tk.END, f"Deleted deceased: {selected_deceased}")
            self.deceased_listbox.delete(tk.ACTIVE)

class UpdateDeceasedForm:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Update Deceased Form")

        self.deceased_label = ttk.Label(self.top, text="Select Deceased")
        self.deceased_listbox = tk.Listbox(self.top)

        self.update_button = ttk.Button(self.top, text="Update", command=self.update_deceased)
        self.cancel_button = ttk.Button(self.top, text="Cancel", command=self.top.destroy)

        self.deceased_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.deceased_listbox.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.update_button.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.cancel_button.grid(row=2, column=1, sticky="w", padx=10, pady=10)

        self.top.configure(bg="#F0F0F0")
        style.configure("TButton", background="#4CAF50", foreground="black")
        style.configure("TLabel", background="#F0F0F0")
        style.configure("TEntry", background="white", foreground="black")

        self.load_deceased()

    def load_deceased(self):
        cursor.execute("SELECT `deceasedID`, `name`, `surname` FROM `deceased`")
        deceased_list = cursor.fetchall()
        for deceased in deceased_list:
            self.deceased_listbox.insert(tk.END, f"{deceased[0]} - {deceased[1]} {deceased[2]}")

    def update_deceased(self):
        selected_deceased = self.deceased_listbox.get(tk.ACTIVE)
        if selected_deceased:
            deceased_id = selected_deceased.split(" - ")[0]
            form = UpdateDeceasedDetailsForm(self.top, deceased_id)

class UpdateDeceasedDetailsForm:
    def __init__(self, parent, deceased_id):
        self.top = tk.Toplevel(parent)
        self.top.title("Update Deceased Details Form")

        self.name_label = ttk.Label(self.top, text="Name")
        self.surname_label = ttk.Label(self.top, text="Surname")
        self.date_of_birth_label = ttk.Label(self.top, text="Date of Birth")
        self.date_of_death_label = ttk.Label(self.top, text="Date of Death")

        self.name_entry = ttk.Entry(self.top)
        self.surname_entry = ttk.Entry(self.top)
        self.date_of_birth_entry = ttk.Entry(self.top)
        self.date_of_death_entry = ttk.Entry(self.top)

        self.update_button = ttk.Button(self.top, text="Update", command=self.update_deceased_details)
        self.cancel_button = ttk.Button(self.top, text="Cancel", command=self.top.destroy)

        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.surname_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.date_of_birth_label.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.date_of_death_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        
        self.name_entry.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.surname_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)
        self.date_of_birth_entry.grid(row=2, column=1, sticky="w", padx=10, pady=10)
        self.date_of_death_entry.grid(row=3, column=1, sticky="w", padx=10, pady=10)

        self.update_button.grid(row=4, column=0, sticky="w", padx=10, pady=10)
        self.cancel_button.grid(row=4, column=1, sticky="w", padx=10, pady=10)

        self.top.configure(bg="#F0F0F0")
        style.configure("TButton", background="#4CAF50", foreground="black")
        style.configure("TLabel", background="#F0F0F0")
        style.configure("TEntry", background="white", foreground="black")

        # Uložení identifikátoru zemřelého
        self.deceased_id = deceased_id

        # Načtení informací o zemřelém do formuláře
        self.load_deceased_details(deceased_id)

    def load_deceased_details(self, deceased_id):
        cursor.execute("SELECT `name`, `surname`, `date_of_birth`, `date_of_death` FROM `deceased` WHERE `deceasedID` = %s", (deceased_id,))
        deceased_details = cursor.fetchone()
        if deceased_details:
            self.name_entry.insert(tk.END, deceased_details[0])
            self.surname_entry.insert(tk.END, deceased_details[1])
            self.date_of_birth_entry.insert(tk.END, deceased_details[2])
            self.date_of_death_entry.insert(tk.END, deceased_details[3])

    def update_deceased_details(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        date_of_death = self.date_of_death_entry.get()

        try:
            # Zahájit transakci
            db_connection.start_transaction()

            # Aktualizovat informace v tabulce `deceased`
            if name and surname and date_of_birth and date_of_death and self.deceased_id:
                cursor.execute(
                    "UPDATE `deceased` SET `name` = %s, `surname` = %s, `date_of_birth` = %s, `date_of_death` = %s WHERE `deceasedID` = %s",
                    (name, surname, date_of_birth, date_of_death, self.deceased_id)
                )

            # Vložit záznam do tabulky `log`
            cursor.execute(
                "INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Updated deceased details: {} {}')".format(name, surname)
            )

            # Uložit změny v databázi
            db_connection.commit()

            # Zobrazit v log_listbox
            log_listbox.insert(tk.END, f"Updated deceased details: {name} {surname}")

        except Exception as e:
            # Pokud dojde k chybě, vrátit transakci do původního stavu
            db_connection.rollback()

            # Zobrazit chybu v log_listbox
            log_listbox.insert(tk.END, f"Error during update: {str(e)}")

        finally:
            # Uzavřít transakci
            db_connection.close()


if __name__ == "__main__":
    app = FuneralApp(root)
    root.geometry("800x600")
    root.mainloop()

