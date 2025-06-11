import tkinter as tk
from tkinter import font
from navigation import open_home

# function to open window
def open_history():
    history = tk.Toplevel()
    history.geometry("150x200")
    history.configure(bg="pink")
    history.attributes("-toolwindow", True)
    
    new_font = font.Font(family="Courier New", size=-18, weight="bold")
    
     # buttons and labels
    back = tk.Button(history, text="<", font="new_font", bg="pink", fg="white", command=open_home, borderwidth=0, relief="flat")
    label = tk.Label(history, text=" History", font=new_font, bg="pink", fg="white")
    
    # layout
    back.grid(row=0, column=0)
    label.grid(row=0, column=1)
