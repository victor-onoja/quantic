import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_days():
    try:
        date_format = "%m/%d/%Y"
        date1 = datetime.strptime(entry_date1.get(), date_format)
        date2 = datetime.strptime(entry_date2.get(), date_format)
        days_difference = abs((date2 - date1).days) + 1  # Include both start and end dates
        messagebox.showinfo("Result", f"The number of days between the dates is: {days_difference}")
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter the dates in the correct format (MM/DD/YYYY).")

# Create the main window
root = tk.Tk()
root.title("Date Difference Calculator")

# Create and place the labels and entry widgets
tk.Label(root, text="Enter the first date (MM/DD/YYYY):").grid(row=0, column=0, padx=10, pady=10)
entry_date1 = tk.Entry(root)
entry_date1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the second date (MM/DD/YYYY):").grid(row=1, column=0, padx=10, pady=10)
entry_date2 = tk.Entry(root)
entry_date2.grid(row=1, column=1, padx=10, pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate Days", command=calculate_days)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
