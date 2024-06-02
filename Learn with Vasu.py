import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Learn with Vasu")
root.geometry("400x300")

# Welcome label
welcome_label = tk.Label(root, text="Welcome to Learn with Vasu", font=("Arial", 16))
welcome_label.pack(pady=20)

# Function to start the quiz
def start_quiz():
    response = player_entry.get().lower()
    if response != "yes":
        messagebox.showinfo("Quit", "You chose not to play. Exiting...")
        root.quit()
    else:
        player_label.pack_forget()
        player_entry.pack_forget()
        start_button.pack_forget()
        question_label.pack(pady=10)
        answer_entry.pack(pady=5)
        submit_button.pack(pady=10)
        next_question()

# Function to check the answer
def check_answer():
    global current_question, correct_answers, wrong_answers
    answer = answer_entry.get().strip()
    correct_answer = questions[current_question][1]
    if answer.lower() == correct_answer.lower():
        correct_answers += 1
        messagebox.showinfo("Result", "Correct")
    else:
        wrong_answers += 1
        messagebox.showinfo("Result", f"Incorrect. The correct answer is {correct_answer}")
    current_question += 1
    if current_question < len(questions):
        next_question()
    else:
        show_results()

# Function to show the next question
def next_question():
    answer_entry.delete(0, tk.END)
    question_label.config(text=questions[current_question][0])

# Function to show the final results
def show_results():
    messagebox.showinfo("Quiz Completed", f"You've completed the quiz!\n\nCorrect Answers: {correct_answers}\nIncorrect Answers: {wrong_answers}")
    root.quit()

# Initial player input for starting the quiz
player_label = tk.Label(root, text="Do you want to play? (yes/no)", font=("Arial", 12))
player_label.pack(pady=10)
player_entry = tk.Entry(root)
player_entry.pack(pady=5)
start_button = tk.Button(root, text="Start", command=start_quiz)
start_button.pack(pady=10)

# Question and answer widgets (initially hidden)
question_label = tk.Label(root, text="", font=("Arial", 12))
answer_entry = tk.Entry(root)
submit_button = tk.Button(root, text="Submit", command=check_answer)

# Questions and answers list
questions = [
    ("What is the value of π (pi) rounded to two decimal places?", "3.14"),
    ("If a triangle has angles measuring 30°, 60°, and 90°, what type of triangle is it?", "right triangle"),
    ("What is the square root of 144?", "12"),
    ("Solve for x: 2x + 5 = 17", "6"),
    ("What is the area of a rectangle with length 8 units and width 5 units?", "40"),
    ("If a circle has a radius of 6 cm, what is its diameter?", "12"),
    ("What is the next number in the Fibonacci sequence after 0, 1, 1, 2, 3, 5, 8, ...?", "13"),
    ("What is the sum of the interior angles of a hexagon?", "720"),
    ("If a car travels at a constant speed of 60 miles per hour, how far will it travel in 3 hours?", "180 miles"),
    ("What is the value of 5 factorial (5!)?", "120")
]
current_question = 0
correct_answers = 0
wrong_answers = 0

# Start the main event loop
root.mainloop()
