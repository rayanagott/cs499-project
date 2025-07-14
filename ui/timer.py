import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from db import insert_study_session

def run_timer(minutes, subject):
    seconds = minutes * 60
    print(f"Starting timer for '{subject}' ({minutes} min)")

    def countdown():
        nonlocal seconds
        if seconds > 0:
            seconds -= 1
            root.after(1000, countdown)
        else:
            messagebox.showinfo("Time's up!", f"Study session for '{subject}' is complete!")

    # create a mini window 
    root = tk.Toplevel()
    root.title("Timer")
    label = tk.Label(root, text=f"{minutes:02d}:00", font=("Courier New", 24), fg="black")
    label.pack(pady=20)

    def update_label():
        mins = seconds // 60
        secs = seconds % 60
        label.config(text=f"{mins:02d}:{secs:02d}")

    def tick():
        nonlocal seconds
        if seconds >= 0:
            update_label()
            seconds -= 1
            root.after(1000, tick)
        else:
            date = datetime.now()
            insert_study_session(subject, minutes, date)
            messagebox.showinfo("Time's up!", f"Done studying {subject}!")
            root.destroy()

    tick()
