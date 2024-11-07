import tkinter as tk

def proceed():
    welcome_label.config(text="Welcome to the Registration Form!", font=("Arial", 14, "bold"))
    proceed_button.place_forget()  # Hide the "Proceed" button

# Root window
root = tk.Tk()
root.title("Welcome Screen")
root.geometry("400x200")  # Adjust the size as needed

# Welcome message
welcome_label = tk.Label(root, text="Welcome to the Application!", font=("Arial", 16, "bold"))
welcome_label.pack(pady=40)  # Add some space around the label

# Proceed button
proceed_button = tk.Button(root, text="Proceed", command=proceed)
proceed_button.pack()

root.mainloop()
