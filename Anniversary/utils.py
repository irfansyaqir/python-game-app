import webbrowser
import os

def open_story():
    file_path = os.path.abspath("index.html")
    webbrowser.open(f"file://{file_path}")
