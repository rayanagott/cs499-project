# shared file for navigation buttons
import tkinter as tk
import ui.home as home
import ui.study_session as study
import ui.goals as goals
import ui.history as history
import ui.pet_widget as pet
import pystray
import threading
from PIL import Image

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

def create_tray_icon(window):
    def on_show():
        window.after(0, window.deiconify)

    def on_quit():
        icon.stop()
        window.destroy()

    image = Image.open("assets/stand_right.png")  # use a small square icon (like 32x32)

    icon = pystray.Icon("study_pet",
                        icon=image,
                        menu=pystray.Menu(
                            pystray.MenuItem("Show", on_show),
                            pystray.MenuItem("Quit", on_quit)
                        ))

    # Run tray in background
    threading.Thread(target=icon.run, daemon=True).start()

def minimize_to_tray(window):
    window.withdraw()  # hide the window
    create_tray_icon(window)