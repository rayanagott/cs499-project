import tkinter as tk
from tkinter import font

# window set-up (size, colors, font)
window = tk.Tk()
window.geometry("150x200")
window.overrideredirect(True) # remove title bar
window.configure(bg="pink")
font = font.Font(family="Courier New", size=-32, weight="bold") 




window.mainloop()