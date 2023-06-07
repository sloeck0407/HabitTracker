import tkinter as tk

def on_checkbox_toggle():
    if checkbox_var.get():
        status_label.config(text="Habit completed!")
    else:
        status_label.config(text="Habit not completed.")

# Create the main window
window = tk.Tk()

# Create a checkbox variable
checkbox_var = tk.BooleanVar()

# Create the checkbox widget
checkbox = tk.Checkbutton(window, text="Mark as done", variable=checkbox_var, command=on_checkbox_toggle)
checkbox.pack()

# Create a label to display the status
status_label = tk.Label(window, text="Habit not completed.")
status_label.pack()

# Start the GUI event loop
window.mainloop()

print(on_checkbox_toggle())