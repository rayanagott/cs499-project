import tkinter as tk
from tkinter import StringVar, font
import time

# window set-up
window = tk.Tk()
window.geometry("175x60")
window.title("Study Timer")
window.configure(bg="white")

# timer font
font = font.Font(family="Courier New", size=-32, weight="bold")

# timer variables
hour=StringVar()
minute=StringVar()
second=StringVar()

label = tk.Label(window, text="01:23:45", font=font, fg="hot pink", bg="white")
label.grid(row=0, column=0, sticky="ew")
label.pack()


window.mainloop()