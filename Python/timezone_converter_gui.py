import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import pytz

def convert_time(time_str, from_tz_str, to_tz_str):
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)
    
    # Parse the time string into a datetime object
    naive_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
    # Localize the naive datetime object to the from_tz
    localized_time = from_tz.localize(naive_time)
    
    # Convert the localized time to the target time zone
    converted_time = localized_time.astimezone(to_tz)
    
    return converted_time

def on_convert():
    time_str = entry_time.get()
    from_tz_str = combobox_from_tz.get()
    to_tz_str = combobox_to_tz.get()
    
    try:
        converted_time = convert_time(time_str, from_tz_str, to_tz_str)
        messagebox.showinfo("Converted Time", f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M:%S')} in {to_tz_str}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Time Zone Converter")

# Create and place the labels and entry widgets
tk.Label(root, text="Enter the date and time (YYYY-MM-DD HH:MM:SS):").grid(row=0, column=0, padx=10, pady=10)
entry_time = tk.Entry(root)
entry_time.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="From Time Zone:").grid(row=1, column=0, padx=10, pady=10)
combobox_from_tz = ttk.Combobox(root, values=pytz.all_timezones)
combobox_from_tz.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="To Time Zone:").grid(row=2, column=0, padx=10, pady=10)
combobox_to_tz = ttk.Combobox(root, values=pytz.all_timezones)
combobox_to_tz.grid(row=2, column=1, padx=10, pady=10)

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=on_convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
