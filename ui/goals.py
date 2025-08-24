import tkinter as tk
from fonts import get_header_font, get_font_16, get_font_14
from db import add_goal, get_all_goals, toggle_goal_completion, delete_goal

def open_goals(window, root):
    import navigation  # Delayed import to avoid circular dependencies

    window.geometry("200x300")
    window.title("Goals")
    window.configure(bg="pink")
    window.attributes("-toolwindow", True)

    header_font = get_header_font()
    font_14 = get_font_14()
    font_16 = get_font_16()

    # Grid layout
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)

    # Navigation BAr
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

    # header
    header_label = tk.Label(window, text="Goals", font=header_font, bg="pink", fg="white")
    header_label.grid(row=0, column=1, columnspan=2, sticky="n", pady=5)

    # Divider
    pink_line = tk.Frame(window, bg="hot pink", height=2)
    pink_line.grid(row=1, column=0, columnspan=3, sticky="ew", pady=(0,10))

    # Goals
    sub_label = tk.Label(window, text="My Goals", font=header_font, bg="pink", fg="white")
    sub_label.grid(row=2, column=0, columnspan=3, pady=(5,5))


    # Frame for goals
    goals_frame = tk.Frame(window, bg="pink")
    goals_frame.grid(row=2, column=0, columnspan=3, pady=5)

    # Create new goal
    new_goal = tk.Label(window, text="New Goal", font=header_font, bg="pink", fg="white")
    new_goal.grid(row=3, column=0, columnspan=3, pady=(10,2))

    goal_entry = tk.Entry(window, font=font_16, justify="center")
    goal_entry.grid(row=4, column=0, columnspan=2, pady=5, ipadx=10)

    create_button = tk.Button(
        window, text="Create", font=header_font, bg="white", fg="pink",
        command=lambda: [add_goal(goal_entry.get()), goal_entry.delete(0, tk.END), refresh_goals()]
    )
    create_button.grid(row=5, column=0, columnspan=3, pady=10)

    # Refresh
    def refresh_goals():
        for widget in goals_frame.winfo_children():
            widget.destroy()

        goals = get_all_goals()
        if goals:
            for goal in goals:
                goal_id, description, completed = goal
                if completed == 1:  # skip completed goals
                    continue

                var = tk.BooleanVar(value=(completed == 1))

                def on_toggle(gid=goal_id, var=var):
                    toggle_goal_completion(gid, var.get())
                    refresh_goals()

                def on_delete(gid=goal_id):
                    delete_goal(gid)
                    refresh_goals()

                goal_row = tk.Frame(goals_frame, bg="pink")

                # check (mark as completed)
                chk = tk.Checkbutton(
                    goal_row, text=description, variable=var, font=font_14,
                    bg="pink", fg="white", anchor="w", selectcolor="pink",
                    command=on_toggle
                )
                chk.pack(side="left", anchor="w")

                # option to delete
                del_btn = tk.Button(
                    goal_row, text="x", font=font_16, bg="pink", fg="red",
                    borderwidth=0, relief="flat", command=on_delete
                )
                del_btn.pack(side="right")

                goal_row.pack(fill="x", pady=2)
        else:
            empty_label = tk.Label(goals_frame, text="No goals yet!", font=font_14, bg="pink", fg="white")
            empty_label.pack()

    refresh_goals()
