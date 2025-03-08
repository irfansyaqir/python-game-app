import tkinter as tk

questions = [
    ("Where did we first meet?", ["Cafe", "Mall", "Park", "Library"], 0),
    ("What is our favorite song?", ["Song A", "Song B", "Song C", "Song D"], 2),
    ("When is our anniversary?", ["Jan 1", "Feb 14", "Mar 3", "Apr 20"], 3)
]

def start_quiz(root):
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Relationship Quiz")

    score = 0
    current_q = 0

    def next_question(selected_index):
        nonlocal current_q, score
        if selected_index == questions[current_q][2]:
            score += 1
        current_q += 1
        if current_q < len(questions):
            load_question()
        else:
            tk.Label(quiz_window, text=f"Quiz finished! Your score: {score}/{len(questions)}").pack()

    def load_question():
        q_text, options, _ = questions[current_q]
        for widget in quiz_window.winfo_children():
            widget.destroy()
        tk.Label(quiz_window, text=q_text, font=("Arial", 14)).pack(pady=10)
        for i, option in enumerate(options):
            tk.Button(quiz_window, text=option, command=lambda i=i: next_question(i)).pack(pady=5)

    load_question()
