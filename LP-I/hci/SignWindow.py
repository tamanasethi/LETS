import tkinter as tk

def submit_signup():
    print("Username:", username_var.get())
    print("Password:", password_var.get())  # In a real application, avoid printing passwords!
    print("Confirm Password:", confirm_password_var.get())
    print("Email ID:", email_var.get())
    print("Phone Number:", phone_var.get())
    print("Address:", address_text.get("1.0", "end-1c"))
    print("\nSign-up successful\n")

# Root window
root = tk.Tk()
root.title("Sign-up Form")
root.geometry("400x450")  # Set size to accommodate all fields

# Variables
username_var = tk.StringVar()
password_var = tk.StringVar()
confirm_password_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()

# Labels and entries for sign-up form
tk.Label(root, text="Username").place(x=20, y=20)
tk.Entry(root, textvariable=username_var).place(x=150, y=20)

tk.Label(root, text="Password").place(x=20, y=60)
tk.Entry(root, textvariable=password_var, show="*").place(x=150, y=60)  # Hide password with "*"

tk.Label(root, text="Confirm Password").place(x=20, y=100)
tk.Entry(root, textvariable=confirm_password_var, show="*").place(x=150, y=100)

tk.Label(root, text="Email ID").place(x=20, y=140)
tk.Entry(root, textvariable=email_var).place(x=150, y=140)

tk.Label(root, text="Phone Number").place(x=20, y=180)
tk.Entry(root, textvariable=phone_var).place(x=150, y=180)

tk.Label(root, text="Address").place(x=20, y=220)
address_text = tk.Text(root, width=30, height=3)
address_text.place(x=150, y=220)

# Submit button
tk.Button(root, text="Sign Up", command=submit_signup).place(x=150, y=300)

root.mainloop()
