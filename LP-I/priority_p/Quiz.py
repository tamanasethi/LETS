import tkinter as tk
from tkinter import messagebox

# Function to check the answer
def submit_answer():
    selected_answer = answer_var.get()  # Get the selected answer
    if selected_answer == questions[current_question]["answer"]:
        messagebox.showinfo("Result", "Correct Answer!")
    else:
        messagebox.showinfo("Result", "Incorrect Answer!")
    next_question()  # Move to the next question

# Function to move to the next question
def next_question():
    global current_question
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("Quiz Completed", "You've completed the quiz!")
        root.quit()  # Close the quiz when finished

# Function to display a question
def display_question():
    question_label.config(text=questions[current_question]["question"])
    answer_var.set(None)  # Reset the selected answer
    # Update the text and value for each option button
    for idx, option in enumerate(questions[current_question]["options"]):
        option_buttons[idx].config(text=option, value=option)

# Quiz data
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Rome", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Shark"],
        "answer": "Blue Whale"
    }
]

# Initialize the root window
root = tk.Tk()
root.title("Online Quiz")
root.geometry("400x300")

# Current question index
current_question = 0

# Question label
question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=300, justify="left")
question_label.pack(pady=20)

# Answer variable for radio buttons
answer_var = tk.StringVar()

# Option buttons for multiple choices
option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=answer_var, value="", font=("Arial", 10))
    btn.pack(anchor="w", padx=20)
    option_buttons.append(btn)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack(pady=20)

# Start by displaying the first question
display_question()

# Run the main loop
root.mainloop()
