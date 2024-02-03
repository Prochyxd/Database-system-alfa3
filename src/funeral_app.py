# funeral_app.py
import tkinter as tk
from tkinter import ttk
from insert_deceased_form import InsertDeceasedForm
from delete_deceased_form import DeleteDeceasedForm
from update_deceased_form import UpdateDeceasedForm
from summary_report import SummaryReport

class FuneralApp:
    def __init__(self, root, db_connection, log_listbox):
        self.root = root
        self.root.title("Funeral Database App")
        self.db_connection = db_connection
        self.log_listbox = log_listbox
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