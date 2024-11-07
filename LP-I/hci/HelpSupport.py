import tkinter as tk

# Function to display a thank-you message when the contact button is clicked
def contact_us():
    print("Thank you for reaching out! We will contact you soon.")

# Root window
root = tk.Tk()
root.title("App Help Screen")
root.geometry("500x500")  # Setting the window size

# Heading
tk.Label(root, text="Help & Support", font=("Arial", 16, "bold")).pack(pady=10)

# Instructions
instructions = """
Welcome to the Help section! Here, you’ll find answers to common questions 
and instructions on how to use the app. If you have further queries, 
please feel free to reach out to us.
"""
tk.Label(root, text=instructions, wraplength=450, justify="center").pack(pady=10)

# FAQs
tk.Label(root, text="Frequently Asked Questions", font=("Arial", 12, "bold")).pack(pady=5)

# FAQ Content - centered
faq_frame = tk.Frame(root)  # Frame to hold FAQ items
faq_frame.pack(pady=10)

faqs = [
    ("Q1: How do I reset my password?", 
     "To reset your password, go to the login screen, click on 'Forgot Password,' and follow the instructions."),
    ("Q2: How do I update my profile?", 
     "Go to 'Settings' -> 'Profile' and click on 'Edit Profile' to update your information."),
    ("Q3: How do I contact customer support?", 
     "You can contact us using the form below or through our email at support@example.com."),
]

# Displaying centered FAQs
for question, answer in faqs:
    tk.Label(faq_frame, text=question, font=("Arial", 10, "bold")).pack(anchor="center", pady=2)
    tk.Label(faq_frame, text=answer, wraplength=450, justify="center").pack(anchor="center", pady=5)

# Contact Us Section
tk.Label(root, text="Contact Us", font=("Arial", 12, "bold")).pack(pady=15)
tk.Label(root, text="If you still need help, please provide your email and click 'Contact Us'").pack()

# Email entry field
tk.Label(root, text="Your Email").pack(pady=5)
email_var = tk.StringVar()
tk.Entry(root, textvariable=email_var, width=30).pack()

# Contact Us button
tk.Button(root, text="Contact Us", command=contact_us).pack(pady=10)

root.mainloop()
