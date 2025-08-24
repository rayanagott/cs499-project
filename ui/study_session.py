import tkinter as tk 
from ui.timer import run_timer
from fonts import get_header_font, get_font_14

def open_study(window, root):
    import navigation 

    window.geometry("200x300")
    window.title("Study")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)

    header_font = get_header_font()
    font_14 = get_font_14()

    # grid layout
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    # Navigation bar
    nav_frame = tk.Frame(window, bg="pink")
    nav_frame.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    back = tk.Button(
        nav_frame, text="<", font=header_font, bg="pink", fg="white",
        command=lambda: navigation.open_home(root), borderwidth=0, relief="flat"
    )
    back.pack(side="left")

    minimize = tk.Button(
        nav_frame, text="-", font=header_font, bg="pink", fg="white",
        command=lambda: navigation.minimize_to_tray(window), borderwidth=0, relief="flat"
    )
    minimize.pack(side="left", padx=(5,0))

    label = tk.Label(window, text="Study", font=header_font, bg="pink", fg="white")
    label.grid(row=0, column=1, columnspan=2, sticky="n", pady=5)
    
    # Divider
    pink_line = tk.Frame(window, bg="hot pink", height=2)
    pink_line.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0,10))

    # Set study subject
    subject_header = tk.Label(window, text="Set Subject", font=header_font, bg="pink", fg="white")
    subject_header.grid(row=2, column=0, columnspan=3, pady=(5,2))

    subject_entry = tk.Entry(window, font=font_14, justify="center")
    subject_entry.grid(row=3, column=0, columnspan=3, pady=5, ipadx=10)

    white_line2 = tk.Frame(window, bg="white", height=2)
    #white_line2.grid(row=4, column=0, columnspan=3, sticky="ew", pady=10)

    # Set time
    timer_header = tk.Label(window, text="Set Time (min)", font=header_font, bg="pink", fg="white")
    timer_header.grid(row=5, column=0, columnspan=3, pady=(5,2))

    timer_entry = tk.Entry(window, font=font_14, justify="center")
    timer_entry.grid(row=6, column=0, columnspan=3, pady=5, ipadx=10)

    # Start button
    start_button = tk.Button(
        window, text="Start", font=header_font,
        bg="white", fg="pink",
        command=lambda: run_timer(int(timer_entry.get()), subject_entry.get())
    )
    start_button.grid(row=7, column=0, columnspan=3, pady=15)

    white_line1 = tk.Frame(window, bg="white", height=2)
    #white_line1.grid(row=8, column=0, columnspan=3, sticky="ew", pady=5)
