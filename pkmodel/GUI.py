#Prototype of input GUI to make things more end-user friendly.

import tkinter as tk
from tkinter import messagebox
from pkmodel import Model

root = tk.Tk()
root.title("Enter values")

#Input fields
input_fields = {}
input_titles = [
    "Dose Amount (mL)",
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

# Checkboxes for intravenous or subcutaneous dosage
intravenous_check_value = tk.BooleanVar()
intravenous_check = tk.Checkbutton(root, text="intravenous dosing")

subcutaneous_check_value = tk.BooleanVar()
subcutaneous_check = tk.Checkbutton(root, text="subcutaneous dosing")

intravenous_check.pack()
subcutaneous_check.pack()
# It's possible for user to check both options so need to figure out how to make it only one box is clickable

# Prevent continuing if neither dosing method is checked (? Or we can just set default to one of them?)
if intravenous_check_value == False and subcutaneous_check_value == False:
    messagebox.showerror("Error", "Please choose a dosing method")

def pass_to_model():
    """Function to pass user inputted values to our pkmodel"""
    user_values = {}
    for title, input_fields in input_fields.items():
        try: 
            user_values[title] = float(input_fields)
        except ValueError:
            messagebox.showerror("error", f"Invalid input in {title}")

    dosing_method = None
    if intravenous_check_value == True:
        dosing_method = "intravenous"
    elif subcutaneous_check_value == True:
        dosing_method = "subcutaneous"

    if user_values and dosing_method:
        model = Model(
            name = "Your model",
            ncomp =
            method = dosing_method[]
            Q_p = 
            V_c = user_values["Volume of central compartment(mL)"]
            V_p = user_values["Volume of peripheral compartment 1 (mL)"]
            CL = user_values["Clearance/elimination rate from central compartment (mL/h)"]
            X = user_values["Dose Amount"]
        )

# Button to submit input
button = tk.Button(root, text="Run", command=pass_to_model)
button.pack()

# Mainloop to run the GUI
root.mainloop()