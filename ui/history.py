import tkinter as tk
from fonts import get_header_font, get_font_16, get_font_14
from db import get_all_goals, get_completed_goals, get_study_sessions, delete_goal
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def show_study_chart(parent, sessions):
    subjects = [s[0] for s in sessions]
    minutes = [s[1] for s in sessions]

    fig = Figure(figsize=(2.9, 2), dpi=100)
    ax = fig.add_subplot(111)

    # Horizontal bar chart
    ax.barh(subjects, minutes, color='pink', edgecolor='grey')

    ax.set_xlabel("Minutes", fontsize=8)
    ax.set_ylabel("Subject", fontsize=8)
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="x", pady=2)



def open_history(window, root):
    import navigation

    window.geometry("350x450")
    window.title("History")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)

    header_font = get_header_font()
    font_14 = get_font_14()
    font_16 = get_font_16()

    # Grid config
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)

    # Top navigation bar
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
    minimize.pack(side="left", padx=(5, 0))

    # Header
    header_label = tk.Label(window, text="History", font=header_font, bg="pink", fg="white")
    header_label.grid(row=0, column=1, columnspan=2, sticky="n", pady=5)

    # Divider
    pink_line = tk.Frame(window, bg="hot pink", height=2)
    pink_line.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0, 10))

    # Scrollable setup 
    canvas = tk.Canvas(window, bg="pink", highlightthickness=0)
    scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scroll_frame = tk.Frame(canvas, bg="pink")

    scroll_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
    scrollbar.grid(row=3, column=2, sticky="ns")

    # Study 
    def refresh_study_sessions():
        study_header = tk.Label(scroll_frame, text="Study Sessions", font=header_font, bg="pink", fg="white")
        study_header.pack(anchor="w", padx=5, pady=(10, 2))

        sessions = get_study_sessions()
        if sessions:
            show_study_chart(scroll_frame, sessions)
        else:
            tk.Label(scroll_frame, text="No study sessions yet!", font=font_16, bg="pink", fg="white").pack()

    # Show completed goals
    def refresh_completed_goals():
        goal_header = tk.Label(scroll_frame, text="Completed Goals", font=header_font, bg="pink", fg="white")
        goal_header.pack(anchor="w", padx=5, pady=(20, 2))

        # Calculate percent completed
        all_goals = get_all_goals()
        completed_goals = get_completed_goals()

        if all_goals:
            percentage = (len(completed_goals) / len(all_goals)) * 100
            percentage_text = f" • {percentage:.0f}% completed"
        else:
            percentage_text = "No goals yet"

        percentage_label = tk.Label(scroll_frame, text=percentage_text, font=font_16, bg="pink", fg="white")
        percentage_label.pack(anchor="w", padx=5, pady=(5, 10))

        # Completed goals list
        if completed_goals:
            for goal_id, description, completed in completed_goals:
                goal_row = tk.Frame(scroll_frame, bg="pink")

                label = tk.Label(goal_row, text=description, font=font_14, bg="pink", fg="white", anchor="w")
                label.pack(side="left", padx=5)

                del_btn = tk.Button(
                    goal_row, text="x", font=font_14, bg="pink", fg="red",
                    borderwidth=0, relief="flat",
                    command=lambda gid=goal_id: [delete_goal(gid), refresh_all()]
                )
                del_btn.pack(side="right")

                goal_row.pack(fill="x", pady=2)
        else:
            tk.Label(scroll_frame, text="No completed goals!", font=font_14, bg="pink", fg="white").pack()

    # Refresh
    def refresh_all():
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        refresh_study_sessions()
        refresh_completed_goals()

    refresh_all()
