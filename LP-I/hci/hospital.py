import tkinter as tk

def submit_form():
    print("Customer Name:", name_var.get())
    print("Gender:", gender_var.get())
    print("Email ID:", email_var.get())
    print("Phone Number:", phone_var.get())
    print("Food Quality Rating:", food_quality_var.get())
    print("Comments:", comments_var.get())
    print("\nFeedback submitted successfully\n")

# Root window
root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x400")  # Set a size for better layout

# Variables
name_var = tk.StringVar()
gender_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
food_quality_var = tk.StringVar()
comments_var = tk.StringVar()

# Labels and entries
tk.Label(root, text="Customer Name").place(x=20, y=20)
tk.Entry(root, textvariable=name_var).place(x=150, y=20)

tk.Label(root, text="Gender").place(x=20, y=60)
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").place(x=150, y=60)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").place(x=220, y=60)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other").place(x=290, y=60)

tk.Label(root, text="Email ID").place(x=20, y=100)
tk.Entry(root, textvariable=email_var).place(x=150, y=100)

tk.Label(root, text="Phone Number").place(x=20, y=140)
tk.Entry(root, textvariable=phone_var).place(x=150, y=140)

tk.Label(root, text="Food Quality Rating").place(x=20, y=180)
tk.Radiobutton(root, text="Excellent", variable=food_quality_var, value="Excellent").place(x=150, y=180)
tk.Radiobutton(root, text="Average", variable=food_quality_var, value="Average").place(x=250, y=180)
tk.Radiobutton(root, text="Poor", variable=food_quality_var, value="Poor").place(x=350, y=180)

tk.Label(root, text="Comments").place(x=20, y=220)
tk.Entry(root, textvariable=comments_var).place(x=150, y=220)

# Submit button
tk.Button(root, text="Submit", command=submit_form).place(x=150, y=260)

root.mainloop()
