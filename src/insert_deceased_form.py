# insert_deceased_form.py
import tkinter as tk
from tkinter import ttk

class InsertDeceasedForm:
    def __init__(self, parent, db_connection, log_listbox):
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