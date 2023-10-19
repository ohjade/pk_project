#Prototype of input GUI to make things more end-user friendly.
#I need to figure out how to pass the user input on to the correct variables in the model

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Enter values")

#Input fields
input_fields = {}
input_titles = [
    "Dose(t)",
    "Volume of central compartment(mL)", 
    "Volume of peripheral compartment 1 (mL)",
    "Clearance/elimination rate from central compartment (mL/h)",
    "Transition rate between central and peripheral compartments (mL/h)"]

for title in input_titles:
    label = tk.Label(root, text=f"{title}:")
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    input_fields[title] = entry

def print_inputs():
    for title, input_fields in input_fields.items():
        user_input = input_fields.get()
        values = float(user_input)
    if values:
        for title, value in values.items():
            message += f"{title}: {value}\n"
        messagebox.showinfo("User Input", message)

# Button to submit input
button = tk.Button(root, text="Run", command=print_inputs)
button.pack()

# Mainloop to run the GUI
root.mainloop()