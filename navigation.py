# shared file for navigation buttons
import tkinter as tk
import ui.home as home
import ui.study_session as study
import ui.goals as goals
import ui.history as history
import ui.pet_widget as pet

active_window = None

def open_home(root):
    global active_window
    if active_window:
        active_window.destroy()

    active_window = tk.Toplevel(root)
    home.open_home(active_window, root)

def open_study(root):
    global active_window
    if active_window:
        active_window.destroy() # destory old windows on every navigation

    active_window = tk.Toplevel(root)
    study.open_study(active_window, root)

def open_goals(root):
    global active_window
    if active_window:
        active_window.destroy()

    active_window = tk.Toplevel(root)
    goals.open_goals(active_window, root)

def open_history(root):
    global active_window
    if active_window:
        active_window.destroy()

    active_window = tk.Toplevel(root)
    history.open_history(active_window, root)

def open_pet(root):
    import ui.pet_widget as pet
    pet.open_pet(root)