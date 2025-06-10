import tkinter as tk
from tkinter import font

# function to open window
def open_study():
    study_session=tk.Toplevel()
    study_session.geometry("150x200")
    study_session.configure(bg="pink")
    study_session.attributes("-toolwindow", True)

    new_font = font.Font(family="Courier New", size=-32, weight="bold") 

    label = tk.Label(study_session, text="Study", font=new_font, bg="pink", fg="white")
    label.pack(pady=10)

