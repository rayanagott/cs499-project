import tkinter as tk
from tkinter import font
from study_session import open_study
from goals import open_goals
from history import open_history

# TO-DO: def a funct to be opened in main.py

# window set-up (size, colors, font)
window = tk.Tk()
window.geometry("150x200")
window.configure(bg="pink")
window.attributes("-toolwindow", True)
font = font.Font(family="Courier New", size=-22, weight="bold") 

# buttons and labels
# TO-DO: make the emji colors visible
study_button = tk.Button(window, text="\U0001F550  Study ", font=font, command=open_study, bg="pink", fg="white",  borderwidth=0, relief="flat")
goals_button = tk.Button(window, text= "\U0001F31F  Goals ", font=font, command=open_goals, bg="pink", fg="white",  borderwidth=0, relief="flat")
history_button = tk.Button(window, text="\U0001F4DC History", font=font, command=open_history, bg="pink", fg="white",  borderwidth=0, relief="flat")

# TO-DO: make window header
# button + label grid location
study_button.grid(row=2, column=2)
goals_button.grid(row=3, column=2)
history_button.grid(row=4, column=2)

window.mainloop()