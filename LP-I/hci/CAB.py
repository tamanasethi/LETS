import tkinter as tk

def submit_booking():
    print("Passenger Name:", passenger_name_var.get())
    print("Phone Number:", phone_var.get())
    print("Pickup Location:", pickup_location_var.get())
    print("Destination:", destination_var.get())
    print("Cab Type:", cab_type_var.get())
    print("Booking Time:", booking_time_var.get())
    print("Payment Method:", ", ".join([method for method, var in payment_methods.items() if var.get()]))
    print("Additional Comments:", comments_text.get("1.0", "end-1c"))
    print("\nBooking submitted successfully\n")

# Root window
root = tk.Tk()
root.title("Cab/Auto Booking App")

# Variables
passenger_name_var = tk.StringVar()
phone_var = tk.StringVar()
pickup_location_var = tk.StringVar()
destination_var = tk.StringVar()
cab_type_var = tk.StringVar()
booking_time_var = tk.StringVar()
payment_methods = {
    "Cash": tk.BooleanVar(),
    "Card": tk.BooleanVar(),
    "UPI": tk.BooleanVar()
}

# Labels and entries
tk.Label(root, text="Passenger Name").place(x=20, y=20)
tk.Entry(root, textvariable=passenger_name_var).place(x=150, y=20)

tk.Label(root, text="Phone Number").place(x=20, y=60)
tk.Entry(root, textvariable=phone_var).place(x=150, y=60)

tk.Label(root, text="Pickup Location").place(x=20, y=100)
tk.Entry(root, textvariable=pickup_location_var).place(x=150, y=100)

tk.Label(root, text="Destination").place(x=20, y=140)
tk.Entry(root, textvariable=destination_var).place(x=150, y=140)

tk.Label(root, text="Cab Type").place(x=20, y=180)
tk.Radiobutton(root, text="Sedan", variable=cab_type_var, value="Sedan").place(x=150, y=180)
tk.Radiobutton(root, text="SUV", variable=cab_type_var, value="SUV").place(x=220, y=180)
tk.Radiobutton(root, text="Auto", variable=cab_type_var, value="Auto").place(x=290, y=180)

tk.Label(root, text="Booking Time (HH:MM)").place(x=20, y=220)
tk.Entry(root, textvariable=booking_time_var).place(x=150, y=220)

tk.Label(root, text="Payment Method").place(x=20, y=260)
tk.Checkbutton(root, text="Cash", variable=payment_methods["Cash"]).place(x=150, y=260)
tk.Checkbutton(root, text="Card", variable=payment_methods["Card"]).place(x=220, y=260)
tk.Checkbutton(root, text="UPI", variable=payment_methods["UPI"]).place(x=290, y=260)

tk.Label(root, text="Additional Comments").place(x=20, y=300)
comments_text = tk.Text(root, width=30, height=3)
comments_text.place(x=150, y=300)

# Submit button
tk.Button(root, text="Submit Booking", command=submit_booking).place(x=150, y=380)

root.mainloop()
