import tkinter as tk
from tkinter import font
from datetime import datetime
from fonts import get_header_font, get_font_16, get_font_14
from db import add_goal


def open_goals(window, root):
    import navigation

    window.geometry("150x200")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)
    header_font = get_header_font()
    font_14 = get_font_14()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # change from datetime to text


    # buttons and labels
    back = tk.Button(
        window,
        text="<",
        font=header_font,
        bg="pink",
        fg="white",
        command=lambda: navigation.open_home(root),
        borderwidth=0,
        relief="flat"
    )

    minimize = tk.Button(
        window,
        text="-",
        font=header_font,
        bg="pink",
        fg="white",
        command=lambda: navigation.minimize_to_tray(window),
        borderwidth=0,
        relief="flat"
    )
    create_button = tk.Button(
    window,
    text="Create",
    font=header_font,
    bg="white",
    fg="pink",
    command=lambda: add_goal(goal_entry.get())
    )
    
    header_label = tk.Label(window, text=" Goals", font=header_font, bg="pink", fg="white")
    sub_label = tk.Label(window, text="  My Goals", font=font_14, bg="pink", fg="white")
    new_goal = tk.Label(window, text=" New Goal", font=font_14, bg="pink", fg="white")
    goal_entry = tk.Entry(window, font=font_14)

    # layout
    back.grid(row=0, column=0)
    minimize.grid(row=1, column=0)
    header_label.grid(row=0, column=1)
    sub_label.grid(row=2, column=1)
    new_goal.grid(row=4, column=1)
    goal_entry.grid(row=5, column=1)
    create_button.grid(row=6, column=1)
