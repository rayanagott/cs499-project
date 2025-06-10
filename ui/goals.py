import tkinter as tk
from tkinter import font

# function to open window
def open_goals():
    goals=tk.Toplevel()
    goals.geometry("150x200")
    goals.configure(bg="pink")
    goals.attributes("-toolwindow", True)

    new_font = font.Font(family="Courier New", size=-32, weight="bold") 

    label = tk.Label(goals, text="Goals", font=new_font, bg="pink", fg="white")
    label.pack(pady=10)

