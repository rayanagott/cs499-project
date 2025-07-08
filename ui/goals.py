import tkinter as tk
from tkinter import font
from fonts import get_header_font, get_font_16, get_font_14

def open_goals(window, root):
    import navigation

    window.geometry("150x200")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)
    header_font = get_header_font()
    font_14 = get_font_14()

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
    
    header_label = tk.Label(window, text=" Goals", font=header_font, bg="pink", fg="white")
    sub_label = tk.Label(window, text="  My goals", font=font_14, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    minimize.grid(row=1, column=0)
    header_label.grid(row=0, column=1)
    sub_label.grid(row=2, column=1)
