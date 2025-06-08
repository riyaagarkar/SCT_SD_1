import tkinter as tk
from tkinter import ttk, messagebox

# Function to convert temperature
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = combo_from.get()
        if unit == "Celsius":
            f = (temp * 9/5) + 32
            k = temp + 273.15
            result.set(f"Fahrenheit: {f:.2f} °F\nKelvin: {k:.2f} K")
        elif unit == "Fahrenheit":
            c = (temp - 32) * 5/9
            k = (temp - 32) * 5/9 + 273.15
            result.set(f"Celsius: {c:.2f} °C\nKelvin: {k:.2f} K")
        elif unit == "Kelvin":
            c = temp - 273.15
            f = (temp - 273.15) * 9/5 + 32
            result.set(f"Celsius: {c:.2f} °C\nFahrenheit: {f:.2f} °F")
        else:
            result.set("Invalid unit selected.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create GUI window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("350x250")
window.configure(bg="#e6f2ff")

# Input
tk.Label(window, text="Enter Temperature:", bg="#e6f2ff").pack(pady=5)
entry_temp = tk.Entry(window)
entry_temp.pack()

# Dropdown for unit
tk.Label(window, text="Select Unit:", bg="#e6f2ff").pack(pady=5)
combo_from = ttk.Combobox(window, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_from.current(0)
combo_from.pack()

# Button
tk.Button(window, text="Convert", command=convert_temperature, bg="#4da6ff", fg="white").pack(pady=10)

# Result
result = tk.StringVar()
tk.Label(window, textvariable=result, bg="#e6f2ff", font=("Arial", 12)).pack(pady=10)

# Run GUI
window.mainloop()