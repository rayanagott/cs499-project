import tkinter as tk
from tkinter import font
from ui.timer import run_timer

def open_study(window, root):
    import navigation 

    window.geometry("150x200")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)
    new_font = font.Font(family="Courier New", size=-18, weight="bold") 

    # buttons and labels
    back = tk.Button(
        window, 
        text="<", 
        font=new_font, 
        bg="pink", 
        fg="white", 
        command=lambda: navigation.open_home(root),  # ✅ reference it here
        borderwidth=0, 
        relief="flat"
    )
    label = tk.Label(window, text=" Study", font=new_font, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
