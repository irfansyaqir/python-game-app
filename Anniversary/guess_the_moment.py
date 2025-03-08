import tkinter as tk
from PIL import Image, ImageTk  # Install using `pip install pillow`

moments = [
    ("moment1.jpg", "First Date"),
    ("moment2.jpg", "First Trip"),
    ("moment3.jpg", "Proposal Day")
]

def start_guess_the_moment(root):
    game_window = tk.Toplevel(root)
    game_window.title("Guess the Moment")

    current_moment = 0

    def check_answer():
        nonlocal current_moment
        if entry.get().lower() == moments[current_moment][1].lower():
            result_label.config(text="Correct! ❤️", fg="green")
        else:
            result_label.config(text="Try Again!", fg="red")
        current_moment += 1
        if current_moment < len(moments):
            load_moment()
        else:
            result_label.config(text="Game Over! 🎉")

    def load_moment():
        img = Image.open(f"images/{moments[current_moment][0]}")
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)
        img_label.config(image=photo)
        img_label.image = photo
        entry.delete(0, tk.END)

    img_label = tk.Label(game_window)
    img_label.pack()
    
    entry = tk.Entry(game_window)
    entry.pack()
    
    submit_btn = tk.Button(game_window, text="Submit", command=check_answer)
    submit_btn.pack()

    result_label = tk.Label(game_window, text="")
    result_label.pack()

    load_moment()
