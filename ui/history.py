import tkinter as tk
from tkinter import font

# function to open window
def open_history(window, root):
    import navigation

    window.geometry("150x200")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)
    
    new_font = font.Font(family="Courier New", size=-18, weight="bold")
    
     # buttons and labels
    back = tk.Button(
        window, 
        text="<", 
        font="new_font", 
        bg="pink", 
        fg="white", 
        command=lambda: navigation.open_home(root), 
        borderwidth=0, 
        relief="flat"
    )
    
    label = tk.Label(window, text=" History", font=new_font, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
