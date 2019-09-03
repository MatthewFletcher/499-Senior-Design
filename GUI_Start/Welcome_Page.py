import tkinter as tk
from tkinter import ttk

# Declare the window 
start_window = tk.Tk()

# Add details 
start_window.title("Welcome")
start_window.geometry("600x600")

# Labels 
title = ttk.Label(text="Welcome to the _____. \nChoose how you'd like to enter your data.")
title.grid(column=2, row=2)

# Buttons 
csv_Button = ttk.Button(text="Import CSV File")
csv_Button.grid(column=2, row=3)

manual_Input_Button = ttk.Button(text="Manual Input")
manual_Input_Button.grid(column=2, row=4)

# Main loop
start_window.mainloop()