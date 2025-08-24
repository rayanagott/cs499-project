import tkinter as tk
from tkinter import font
from datetime import datetime
from fonts import get_font_16, get_header_font

def get_greeting():
    time = datetime.now()
    hour = time.hour
    
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def open_home(window, root):
    import navigation  

    window.title("Home")
    window.geometry("200x300")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)
    font_16 = get_font_16()
    header_font = get_header_font()

    # Greeting
    greeting = get_greeting()
    greeting_label = tk.Label(
        window, text=greeting,
        font=("Courier New", -18, "bold"),
        bg="pink", fg="white"
    )
    greeting_label.pack(pady=(20, 10))

    # Separator
    pink_line1 = tk.Frame(window, bg="hot pink", height=2, width=200)
    pink_line1.pack(pady=(0, 10))

    # Buttons
    study_button = tk.Button(
        window, text="\U0001F550  Study ",
        font=header_font, bg="pink", fg="white",
        borderwidth=0, relief="flat",
        command=lambda: navigation.open_study(root)
    )
    study_button.pack(pady=5)

    # Seperator
    white_line1 = tk.Frame(window, bg="white", height=2, width=150)
    white_line1.pack(pady=(0, 10))

    goals_button = tk.Button(
        window, text="\U0001F31F  Goals ",
        font=header_font, bg="pink", fg="white",
        borderwidth=0, relief="flat",
        command=lambda: navigation.open_goals(root)
    )
    goals_button.pack(pady=5)

    # Seperator
    white_line2 = tk.Frame(window, bg="white", height=2, width=150)
    white_line2.pack(pady=(0, 10))

    history_button = tk.Button(
        window, text="\U0001F4DC History",
        font=header_font, bg="pink", fg="white",
        borderwidth=0, relief="flat",
        command=lambda: navigation.open_history(root)
    )
    history_button.pack(pady=5)

    # Bottom separator
    pink_line2 = tk.Frame(window, bg="hot pink", height=2, width=200)
    pink_line2.pack(pady=(10, 10))

    # TO-DO
    # Possibly have random quotes displayed
