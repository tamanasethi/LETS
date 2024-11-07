import tkinter as tk

def submit_transaction():
    print("Sender's Name:", sender_name_var.get())
    print("Sender's Account Number:", sender_account_var.get())
    print("Receiver's Name:", receiver_name_var.get())
    print("Receiver's Account Number:", receiver_account_var.get())
    print("Transfer Amount:", amount_var.get())
    print("Transaction Note:", note_text.get("1.0", "end-1c"))
    print("\nTransaction submitted successfully\n")

# Root window
root = tk.Tk()
root.title("Fund Transfer Form")
root.geometry("400x450")  # Adjust size for a better layout

# Variables
sender_name_var = tk.StringVar()
sender_account_var = tk.StringVar()
receiver_name_var = tk.StringVar()
receiver_account_var = tk.StringVar()
amount_var = tk.StringVar()

# Labels and entries
tk.Label(root, text="Sender's Name").place(x=20, y=20)
tk.Entry(root, textvariable=sender_name_var).place(x=200, y=20)

tk.Label(root, text="Sender's Account Number").place(x=20, y=60)
tk.Entry(root, textvariable=sender_account_var).place(x=200, y=60)

tk.Label(root, text="Receiver's Name").place(x=20, y=100)
tk.Entry(root, textvariable=receiver_name_var).place(x=200, y=100)

tk.Label(root, text="Receiver's Account Number").place(x=20, y=140)
tk.Entry(root, textvariable=receiver_account_var).place(x=200, y=140)

tk.Label(root, text="Transfer Amount").place(x=20, y=180)
tk.Entry(root, textvariable=amount_var).place(x=200, y=180)

tk.Label(root, text="Transaction Note").place(x=20, y=220)
note_text = tk.Text(root, width=30, height=3)
note_text.place(x=200, y=220)

# Submit button
tk.Button(root, text="Submit Transaction", command=submit_transaction).place(x=150, y=320)

root.mainloop()
