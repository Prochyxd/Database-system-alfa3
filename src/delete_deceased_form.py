# delete_deceased_form.py
import tkinter as tk
from tkinter import ttk

class DeleteDeceasedForm:
    def __init__(self, parent, db_connection, log_listbox):
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