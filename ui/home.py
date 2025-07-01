import tkinter as tk
from tkinter import font
from datetime import datetime

def get_greeting():
    time = datetime.now()
    hour = time.hour
    
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

def open_home(window, root):
    import navigation  

    # window set-up (size, colors, font)
    #window = tk.Toplevel(root)
    window.title("Home")
    window.geometry("150x200")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)
    new_font = font.Font(family="Courier New", size=-16, weight="bold") 

    # buttons and labels
    greeting = get_greeting()
    greeting_label = tk.Label(window, text=greeting, font=("Courier New",-16, "bold"), bg="pink", fg="white")
    study_button = tk.Button(window, text="\U0001F550  Study ", font=new_font, command=lambda: navigation.open_study(root), bg="pink", fg="white",  borderwidth=0, relief="flat")
    goals_button = tk.Button(window, text= "\U0001F31F  Goals ", font=new_font, command=lambda: navigation.open_goals(root), bg="pink", fg="white",  borderwidth=0, relief="flat")
    history_button = tk.Button(window, text="\U0001F4DC History", font=new_font, command=lambda: navigation.open_history(root), bg="pink", fg="white",  borderwidth=0, relief="flat")
    
    pink_line1 = tk.Frame(window, bg="hot pink", height=2, width=150)
    pink_line2 = tk.Frame(window, bg="hot pink", height=2, width=150)
    white_line1 = tk.Frame(window, bg="white", height=1, width=100)
    white_line2 = tk.Frame(window, bg="white", height=1, width=100)
    white_line3 = tk.Frame(window, bg="white", height=1, width=100)

    # layout
    pink_line1.grid(row=0, column=0, columnspan=3)
    greeting_label.grid(row=1, column=0, columnspan=3)
    pink_line2.grid(row=2, column=0, columnspan=3, pady=5)
    
    study_button.grid(row=3, column=0, columnspan=3)
    white_line1.grid(row=4, column=1, columnspan=1, pady=10)
    
    goals_button.grid(row=5, column=0, columnspan=3)
    white_line2.grid(row=6, column=1, columnspan=1, pady=10)
    
    history_button.grid(row=7, column=0, columnspan=3)    
    white_line3.grid(row=8, column=1, columnspan=1, pady=10)
