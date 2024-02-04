import tkinter as tk
from tkinter import ttk, simpledialog
import mysql.connector
from configparser import ConfigParser
import configparser
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

config_path = os.path.join(script_dir, '..', 'config', 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)

db_config = {
    'host': config.get('Database', 'host'),
    'user': config.get('Database', 'user'),
    'password': config.get('Database', 'password'),
    'database': config.get('Database', 'database'),
}

db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

root = tk.Tk()
root.title("Funeral Service")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="black")
style.configure("TLabel", font=("Arial", 12), foreground="black")
style.configure("TEntry", font=("Arial", 12), foreground="black")

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


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="funeral_db"
)

cursor = db_connection.cursor()

class FuneralApp:
    """
    Represents a Funeral Database App.

    Attributes:
        root (Tk): The root window of the app.

    Methods:
        __init__(self, root): Initializes the FuneralApp object.
        create_widgets(self): Creates the widgets for the app.
        show_insert_deceased(self): Shows the form for inserting a deceased.
        show_delete_deceased(self): Shows the form for deleting a deceased.
        show_update_deceased(self): Shows the form for updating a deceased.
        show_summary_report(self): Shows the summary report.
    """
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

class SummaryReport:
    """
    Represents a Summary Report.

    Attributes:
        top (Toplevel): The top-level window of the report.

    Methods:
        __init__(self, parent): Initializes the SummaryReport object.
        generate_report(self): Generates a report with the average price of funeral service, number of deceased, and average age of deceased.
    """
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("Summary Report")

        self.report_label = ttk.Label(self.top, text="Summary Report")
        self.report_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)

        self.top.configure(bg="#F0F0F0")
        style.configure("TLabel", background="#F0F0F0")

    def generate_report(self):
        """
        Generates a report with the average price of funeral service, number of deceased, and average age of deceased.
        If an error occurs during report generation, it displays the error message.
        """
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
    """
    Represents a form for inserting a deceased.

    Attributes:
        top (Toplevel): The top-level window of the form.

    Methods:
        __init__(self, parent): Initializes the InsertDeceasedForm object.
        insert_deceased(self): Inserts a new deceased record into the database.
    """
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
        """
        Inserts a new deceased record into the database.

        Retrieves the name, surname, date of birth, and date of death from the corresponding entry fields.
        If all fields are filled out, the method inserts the record into the 'deceased' table and logs the action.
        If any of the fields are missing, it logs the failure to insert and displays an error message.

        Args:
            None

        Returns:
            None
        """
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
    """
    Represents a form for deleting a deceased.

    Attributes:
        top (Toplevel): The top-level window of the form.

    Methods:
        __init__(self, parent): Initializes the DeleteDeceasedForm object.
        delete_deceased(self): Deletes a deceased record from the database.
    """
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
        """
        Fetches deceased records from the database and populates the deceased listbox.

        Returns:
            None
        """
        cursor.execute("SELECT * FROM `deceased`")
        deceased_list = cursor.fetchall()

        for deceased in deceased_list:
            self.deceased_listbox.insert(tk.END, f"{deceased[0]} {deceased[1]}")

    def delete_deceased(self):
        """
        Deletes a deceased record from the database.

        Retrieves the selected deceased from the listbox.
        If a deceased is selected, the method deletes the record from the 'deceased' table and logs the action.
        If no deceased is selected, it logs the failure to delete and displays an error message.

        Args:
            None

        Returns:
            None
        """
        selected_deceased = self.deceased_listbox.get(tk.ACTIVE)

        if selected_deceased:
            name, surname = selected_deceased.split()
            cursor.execute("DELETE FROM `deceased` WHERE `name` = %s AND `surname` = %s", (name, surname))
            db_connection.commit()
            cursor.execute("INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Deleted deceased: {} {}')".format(name, surname))
            db_connection.commit()
            log_listbox.insert(tk.END, f"Deleted deceased: {name} {surname}")

        else:
            cursor.execute("INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Failed to delete deceased because no deceased is selected')")
            log_listbox.insert(tk.END, "Please select a deceased to delete")
        cursor.execute("SELECT `deceasedID`, `name`, `surname` FROM `deceased`")
        deceased_list = cursor.fetchall()
        for deceased in deceased_list:
            self.deceased_listbox.insert(tk.END, f"{deceased[0]} - {deceased[1]} {deceased[2]}")

    def delete_deceased(self):
            """
            Deletes the selected deceased from the database.

            Retrieves the selected deceased from the listbox and extracts the deceased ID.
            Executes a SQL query to delete the deceased from the 'deceased' table.
            Commits the changes to the database.
            Inserts a log entry for the deletion operation.
            Updates the log listbox with the deletion message.
            Removes the selected deceased from the deceased listbox.
            """
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
            """
            Fetches the deceased records from the database and populates the deceased listbox.

            Returns:
                None
            """
            cursor.execute("SELECT `deceasedID`, `name`, `surname` FROM `deceased`")
            deceased_list = cursor.fetchall()
            for deceased in deceased_list:
                self.deceased_listbox.insert(tk.END, f"{deceased[0]} - {deceased[1]} {deceased[2]}")

    def update_deceased(self):
        """
        Update the details of a deceased person.

        Retrieves the selected deceased person from the listbox and extracts the deceased ID.
        Opens the UpdateDeceasedDetailsForm with the extracted deceased ID.
        """
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

        self.deceased_id = deceased_id

        self.load_deceased_details(deceased_id)

    def load_deceased_details(self, deceased_id):
            """
            Loads the details of a deceased person from the database and populates the corresponding entry fields.

            Parameters:
            - deceased_id (int): The ID of the deceased person.

            Returns:
            None
            """
            cursor.execute("SELECT `name`, `surname`, `date_of_birth`, `date_of_death` FROM `deceased` WHERE `deceasedID` = %s", (deceased_id,))
            deceased_details = cursor.fetchone()
            if deceased_details:
                self.name_entry.insert(tk.END, deceased_details[0])
                self.surname_entry.insert(tk.END, deceased_details[1])
                self.date_of_birth_entry.insert(tk.END, deceased_details[2])
                self.date_of_death_entry.insert(tk.END, deceased_details[3])

    def update_deceased_details(self):
        """
        Update the details of a deceased person in the database.

        Retrieves the name, surname, date of birth, and date of death from the corresponding entry fields.
        Executes an SQL UPDATE statement to update the deceased person's details in the database.
        Inserts a log entry with the updated details and the current date and time.
        Commits the transaction and displays a success message in the log listbox.
        If an error occurs, rolls back the transaction, logs the error, and displays an error message in the log listbox.
        Finally, closes the database connection.

        :return: None
        """
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        date_of_birth = self.date_of_birth_entry.get()
        date_of_death = self.date_of_death_entry.get()

        try:
            db_connection.start_transaction()

            if name and surname and date_of_birth and date_of_death and self.deceased_id:
                cursor.execute(
                    "UPDATE `deceased` SET `name` = %s, `surname` = %s, `date_of_birth` = %s, `date_of_death` = %s WHERE `deceasedID` = %s",
                    (name, surname, date_of_birth, date_of_death, self.deceased_id)
                )

            cursor.execute(
                "INSERT INTO `log` (`date`, `message`) VALUES (NOW(), 'Updated deceased details: {} {}')".format(name, surname)
            )

            db_connection.commit()

            log_listbox.insert(tk.END, f"Updated deceased details: {name} {surname}")

        except Exception as e:
            db_connection.rollback()

            log_listbox.insert(tk.END, f"Error during update: {str(e)}")

        finally:
            db_connection.close()


if __name__ == "__main__":
    app = FuneralApp(root)
    root.geometry("800x600")
    root.mainloop()