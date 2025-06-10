import tkinter as tk
from tkinter import font

# function to open window
def open_history():
    history = tk.Toplevel()
    history.geometry("150x200")
    history.configure(bg="pink")
    history.attributes("-toolwindow", True)
    
    new_font = font.Font(family="Courier New", size=-32, weight="bold")
    
    label = tk.Label(history, text="History", font=new_font, bg="pink", fg="white")
    label.pack(pady=10)
