import tkinter as tk

def login():
    print("Username:", username_var.get())
    print("Password:", password_var.get())
    print("\nLogin Successful\n")

# Root window
root = tk.Tk()
root.title("Login Window")
root.geometry("300x200")  # Set window size

# Variables
username_var = tk.StringVar()
password_var = tk.StringVar()

# Labels and entries for username and password
tk.Label(root, text="Username").place(x=20, y=40)
tk.Entry(root, textvariable=username_var).place(x=100, y=40)

tk.Label(root, text="Password").place(x=20, y=80)
tk.Entry(root, textvariable=password_var, show="*").place(x=100, y=80)

# Login button
tk.Button(root, text="Login", command=login).place(x=100, y=120)

root.mainloop()
