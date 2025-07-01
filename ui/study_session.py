import tkinter as tk
from tkinter import font
from ui.timer import run_timer

def open_study(root):
    import navigation 

    study_session = tk.Toplevel(root)
    study_session.geometry("150x200")
    study_session.configure(bg="pink")
    study_session.attributes("-toolwindow", True)
    new_font = font.Font(family="Courier New", size=-18, weight="bold") 

    # buttons and labels
    back = tk.Button(
        study_session, 
        text="<", 
        font=new_font, 
        bg="pink", 
        fg="white", 
        command=lambda: navigation.open_home(root),  # ✅ reference it here
        borderwidth=0, 
        relief="flat"
    )
    label = tk.Label(study_session, text=" Study", font=new_font, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
