import tkinter as tk
from tkinter import font
from ui.timer import run_timer
from fonts import get_header_font, get_font_16, get_font_14

def open_study(window, root):
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
        command=lambda: navigation.open_home(root),  # ✅ reference it here
        borderwidth=0, 
        relief="flat"
    )
    label = tk.Label(window, text=" Study", font=header_font, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
