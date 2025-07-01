import tkinter as tk
from tkinter import font
from fonts import get_header_font, get_font_16, get_font_14

# function to open window
def open_history(window, root):
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
    
    label = tk.Label(window, text=" History", font=header_font, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
