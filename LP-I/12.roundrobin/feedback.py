import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_feedback():
    name = entry_name.get()
    comments = text_comments.get("1.0", tk.END)
    food_quality = food_quality_var.get()
    dining_experience = "Yes" if dining_experience_var.get() else "No"

    if name.strip() == "" or comments.strip() == "":
        messagebox.showwarning("Incomplete Form", "Please complete all fields.")
        return

    feedback_summary = (
        f"Name: {name}\n"
        f"Food Quality: {food_quality}\n"
        f"Dining Experience: {dining_experience}\n"
        f"Comments:\n{comments}"
    )

    # Display feedback summary
    messagebox.showinfo("Feedback Submitted", feedback_summary)

    # Clear the form fields after submission
    entry_name.delete(0, tk.END)
    text_comments.delete("1.0", tk.END)
    food_quality_var.set("Good")
    dining_experience_var.set(0)

# Create the main application window
root = tk.Tk()
root.title("Hotel Food Feedback Form")
root.geometry("400x500")

# Title label
label_title = tk.Label(root, text="Customer Feedback Form", font=("Arial", 16))
label_title.place(x=100, y=10)

# Name label and entry
label_name = tk.Label(root, text="Name:")
label_name.place(x=20, y=50)
entry_name = tk.Entry(root, width=30)
entry_name.place(x=120, y=50)

# Food quality label and options
label_food_quality = tk.Label(root, text="How was the quality of the food?")
label_food_quality.place(x=20, y=90)

food_quality_var = tk.StringVar(value="Good")  # Default selection
radio_good = tk.Radiobutton(root, text="Good", variable=food_quality_var, value="Good")
radio_good.place(x=40, y=120)
radio_average = tk.Radiobutton(root, text="Average", variable=food_quality_var, value="Average")
radio_average.place(x=40, y=150)
radio_poor = tk.Radiobutton(root, text="Poor", variable=food_quality_var, value="Poor")
radio_poor.place(x=40, y=180)

# Dining experience checkbox
dining_experience_var = tk.IntVar()  # 0 for No, 1 for Yes
check_dining = tk.Checkbutton(root, text="Did you dine in?", variable=dining_experience_var)
check_dining.place(x=20, y=220)

# Comments label and text box
label_comments = tk.Label(root, text="Additional Comments:")
label_comments.place(x=20, y=260)
text_comments = tk.Text(root, height=5, width=30)
text_comments.place(x=20, y=290)

# Submit button
button_submit = tk.Button(root, text="Submit Feedback", command=submit_feedback)
button_submit.place(x=150, y=400)

# Run the Tkinter event loop
root.mainloop()
