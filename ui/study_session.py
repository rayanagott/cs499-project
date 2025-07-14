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
        command=lambda: navigation.open_home(root),  
        borderwidth=0, 
        relief="flat"
    )
    start_button = tk.Button(
    window,
    text="Start",
    font=header_font,
    bg="white",
    fg="pink",
    command=lambda: run_timer(int(timer_entry.get()), subject_entry.get())
    )
    label = tk.Label(window, text="Study", font=header_font, bg="pink", fg="white")
    timer_header = tk.Label(window, text="Set Time (min)", font=header_font, bg="pink", fg="white")
    timer_entry =  tk.Entry(window, font=font_14)
    subject_header = tk.Label(window, text="Set Subject", font=header_font, bg="pink", fg="white")
    subject_entry = tk.Entry(window, font=font_14)
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
    subject_header.grid(row=1, column=1, columnspan=1)
    subject_entry.grid(row=2, column=1, columnspan=1)
    timer_header.grid (row=3, column=1)
    timer_entry.grid(row=4, column=1, columnspan=1)
    start_button.grid(row=5, column=1, columnspan=1, pady=10)


