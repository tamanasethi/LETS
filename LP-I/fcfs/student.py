import tkinter as tk

def submit_form():
    print("Student Name:", name_var.get())
    print("Father's Name:", father_name_var.get())
    print("Gender:", gender_var.get())
    print("Languages Known:", ", ".join([lang for lang, var in languages.items() if var.get()]))
    print("Email ID:", email_var.get())
    print("Phone Number:", phone_var.get())
    print("Address:", address_text.get("1.0", "end-1c"))
    print("\nForm submitted successfully\n")

# Root window
root = tk.Tk()
root.title("Registration Form")

# Variables
name_var = tk.StringVar()
father_name_var = tk.StringVar()
gender_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
languages = {
    "English": tk.BooleanVar(),
    "Hindi": tk.BooleanVar(),
    "Other": tk.BooleanVar()
}

# Labels and entries
tk.Label(root, text="Student Name").place(x=20, y=20)
tk.Entry(root, textvariable=name_var).place(x=150, y=20)

tk.Label(root, text="Father's Name").place(x=20, y=60)
tk.Entry(root, textvariable=father_name_var).place(x=150, y=60)

tk.Label(root, text="Gender").place(x=20, y=100)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=150, y=100)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=220, y=100)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").place(x=290, y=100)

tk.Label(root, text="Languages Known").place(x=20, y=140)
tk.Checkbutton(root, text="English", variable=languages["English"]).place(x=150, y=140)
tk.Checkbutton(root, text="Hindi", variable=languages["Hindi"]).place(x=220, y=140)
tk.Checkbutton(root, text="Other", variable=languages["Other"]).place(x=290, y=140)

tk.Label(root, text="Email ID").place(x=20, y=180)
tk.Entry(root, textvariable=email_var).place(x=150, y=180)

tk.Label(root, text="Phone Number").place(x=20, y=220)
tk.Entry(root, textvariable=phone_var).place(x=150, y=220)

tk.Label(root, text="Address").place(x=20, y=260)
address_text = tk.Text(root, width=30, height=3)
address_text.place(x=150, y=260)

# Submit button
tk.Button(root, text="Submit", command=submit_form).place(x=150, y=320)

root.mainloop()
