import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance
import os
import glob
from itertools import cycle
from quiz import start_quiz
from guess_the_moment import start_guess_the_moment
from matching_game import start_matching_game
from utils import open_story

# Path to the folder containing background images
IMAGE_FOLDER = "images"

# Get all images in the folder
image_paths = glob.glob(os.path.join(IMAGE_FOLDER, "*.jpg"))
image_cycle = cycle(image_paths)  # Loop through images infinitely

def fade_in(canvas, img_label, img, alpha=0.0):
    """ Gradually increases the opacity of the image """
    if alpha < 1.0:
        img = ImageEnhance.Brightness(img).enhance(alpha)
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img
        canvas.after(50, fade_in, canvas, img_label, img, alpha + 0.05)
    else:
        canvas.after(2000, fade_out, canvas, img_label, img)  # Wait 2s before fading out

def fade_out(canvas, img_label, img, alpha=1.0):
    """ Gradually decreases the opacity of the image """
    if alpha > 0.0:
        img = ImageEnhance.Brightness(img).enhance(alpha)
        tk_img = ImageTk.PhotoImage(img)
        img_label.config(image=tk_img)
        img_label.image = tk_img
        canvas.after(50, fade_out, canvas, img_label, img, alpha - 0.05)
    else:
        load_next_image(canvas, img_label)  # Load next image when fully faded out

def load_next_image(canvas, img_label):
    """ Load the next image in the cycle """
    img_path = next(image_cycle)
    img = Image.open(img_path).resize((400, 400))  # Resize as needed
    fade_in(canvas, img_label, img)

def main_menu():
    root = tk.Tk()
    root.title("Anniversary Mini-Game")
    root.geometry("400x400")

    # Create a canvas for background
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack(fill="both", expand=True)

    # Background Image Label
    img_label = tk.Label(root)
    img_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Start background fading
    load_next_image(canvas, img_label)

    # UI Elements (on top of the background)
    tk.Label(root, text="Welcome, Syasya! ❤️", font=("Arial", 16), bg="white").pack(pady=20)
    tk.Button(root, text="Relationship Quiz", command=lambda: start_quiz(root)).pack(pady=10)
    tk.Button(root, text="Guess the Moment", command=lambda: start_guess_the_moment(root)).pack(pady=10)
    tk.Button(root, text="Matching Game", command=lambda: start_matching_game(root)).pack(pady=10)
    tk.Button(root, text="View Our Love Story ❤️", command=open_story).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
