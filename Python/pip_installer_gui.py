import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

def install_package():
    package_name = entry_package.get()
    if package_name:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            messagebox.showinfo("Success", f"Package '{package_name}' installed successfully.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", f"Failed to install package '{package_name}'.")
    else:
        messagebox.showwarning("Input Error", "Please enter a package name.")

def show_installed_packages():
    try:
        result = subprocess.check_output([sys.executable, "-m", "pip", "list"], text=True)
        messagebox.showinfo("Installed Packages", result)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to retrieve installed packages.")

# Create the main window
root = tk.Tk()
root.title("Pip Package Installer")

# Create and place the labels and entry widgets
tk.Label(root, text="Enter the package name to install:").grid(row=0, column=0, padx=10, pady=10)
entry_package = tk.Entry(root)
entry_package.grid(row=0, column=1, padx=10, pady=10)

# Create and place the install button
install_button = tk.Button(root, text="Install Package", command=install_package)
install_button.grid(row=1, column=0, columnspan=2, pady=10)

# Create and place the show installed packages button
show_button = tk.Button(root, text="Show Installed Packages", command=show_installed_packages)
show_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
