import tkinter as tk

def submit_form():
    print("Student Name:", name_var.get())
    print("Father's Name:", father_name_var.get())
    print("Gender:", gender_var.get())
    print("Age Group:", age_group_var.get())
    print("Sports Interested:", ", ".join([sport for sport, var in sports.items() if var.get()]))
    print("Email ID:", email_var.get())
    print("Phone Number:", phone_var.get())
    print("Address:", address_text.get("1.0", "end-1c"))
    print("Medical Conditions:", medical_conditions_var.get())
    print("\nForm submitted successfully\n")

# Root window
root = tk.Tk()
root.title("Sports Academy Registration Form")

# Variables
name_var = tk.StringVar()
father_name_var = tk.StringVar()
gender_var = tk.StringVar()
age_group_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
medical_conditions_var = tk.StringVar()

sports = {
    "Football": tk.BooleanVar(),
    "Basketball": tk.BooleanVar(),
    "Tennis": tk.BooleanVar(),
    "Swimming": tk.BooleanVar(),
    "Cricket": tk.BooleanVar()
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

tk.Label(root, text="Age Group").place(x=20, y=140)
tk.Radiobutton(root, text="Under 18", variable=age_group_var, value="Under 18").place(x=150, y=140)
tk.Radiobutton(root, text="18-25", variable=age_group_var, value="18-25").place(x=220, y=140)
tk.Radiobutton(root, text="Above 25", variable=age_group_var, value="Above 25").place(x=290, y=140)

tk.Label(root, text="Sports Interested").place(x=20, y=180)
tk.Checkbutton(root, text="Football", variable=sports["Football"]).place(x=150, y=180)
tk.Checkbutton(root, text="Basketball", variable=sports["Basketball"]).place(x=220, y=180)
tk.Checkbutton(root, text="Tennis", variable=sports["Tennis"]).place(x=290, y=180)
tk.Checkbutton(root, text="Swimming", variable=sports["Swimming"]).place(x=150, y=220)
tk.Checkbutton(root, text="Cricket", variable=sports["Cricket"]).place(x=220, y=220)

tk.Label(root, text="Email ID").place(x=20, y=260)
tk.Entry(root, textvariable=email_var).place(x=150, y=260)

tk.Label(root, text="Phone Number").place(x=20, y=300)
tk.Entry(root, textvariable=phone_var).place(x=150, y=300)

tk.Label(root, text="Address").place(x=20, y=340)
address_text = tk.Text(root, width=30, height=3)
address_text.place(x=150, y=340)

tk.Label(root, text="Medical Conditions (if any)").place(x=20, y=400)
tk.Entry(root, textvariable=medical_conditions_var).place(x=150, y=400)

# Submit button
tk.Button(root, text="Submit", command=submit_form).place(x=150, y=440)

root.mainloop()
