# update_deceased_form.py
import tkinter as tk
from tkinter import ttk

class UpdateDeceasedForm:
    def __init__(self, parent, db_connection, log_listbox):
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