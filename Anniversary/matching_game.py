import tkinter as tk
import random

pairs = [
    ("Favorite Food", "Pizza"),
    ("Favorite Trip", "Bali"),
    ("First Gift", "Teddy Bear")
]

def start_matching_game(root):
    game_window = tk.Toplevel(root)
    game_window.title("Matching Game")

    shuffled_pairs = pairs[:]
    random.shuffle(shuffled_pairs)

    left_side = [p[0] for p in shuffled_pairs]
    right_side = [p[1] for p in shuffled_pairs]
    random.shuffle(right_side)

    selected = {}

    def check_match(btn, text):
        if len(selected) < 2:
            selected[btn] = text
        if len(selected) == 2:
            keys = list(selected.keys())
            if pairs[left_side.index(selected[keys[0]])][1] == selected[keys[1]]:
                result_label.config(text="Match! 🎉", fg="green")
            else:
                result_label.config(text="Wrong Match!", fg="red")
            selected.clear()

    for i, text in enumerate(left_side):
        tk.Button(game_window, text=text, command=lambda text=text: check_match(text, text)).grid(row=i, column=0)
    for i, text in enumerate(right_side):
        tk.Button(game_window, text=text, command=lambda text=text: check_match(text, text)).grid(row=i, column=1)

    result_label = tk.Label(game_window, text="")
    result_label.grid(row=len(pairs), columnspan=2)
