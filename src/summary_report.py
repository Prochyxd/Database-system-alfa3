# summary_report.py
import tkinter as tk
from tkinter import ttk

class SummaryReport:
    def __init__(self, parent, db_connection, log_listbox):
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