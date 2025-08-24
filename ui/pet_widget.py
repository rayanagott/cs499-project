import tkinter as tk
from PIL import Image, ImageTk
from itertools import cycle
import random

def click_pet(event=None):
    print("test")

class Pet:
    def __init__(self, window, canvas, x, y, walk_animations):
        self.window = window
        self.canvas = canvas
        self.x = x
        self.y = y
        self.direction = "right"
        self.speed = 3
        self.walk_animations = walk_animations
        self.current_frame = None
        self.image_obj = None
        self.switch_frame()  # set initial image

    def switch_frame(self):
        frame = next(self.walk_animations[self.direction])
        self.current_frame = frame
        if self.image_obj is None:
            self.image_obj = self.canvas.create_image(0, 0, anchor="nw", image=frame)
        else:
            self.canvas.itemconfig(self.image_obj, image=frame)

    def random_walk_left(self):
        return random.randint(10, 80)

    def random_walk_right(self):
        return random.randint(110, 150)
    
    def move(self):
        screen_width = self.window.winfo_screenwidth()
        random_int_left = self.random_walk_left()
        random_int_right = self.random_walk_right()

        if self.direction == "right":
            self.x += self.speed
            if self.x > random_int_right:  # right edge
                self.direction = "left"
        else:
            self.x -= self.speed
            if self.x < random_int_left:  # left edge
                self.direction = "right"

        # update frame + position
        self.switch_frame()
        self.window.geometry(f"+{self.x}+{self.y}")

        # schedule next update
        self.window.after(200, self.move)


def open_pet(root):
    pet_window = tk.Toplevel(root)
    pet_window.overrideredirect(True)  # remove title bar
    pet_window.wm_attributes("-topmost", True)  # always on top
    pet_window.wm_attributes("-transparentcolor", "green")  # transparency

    # walking animations
    walk_animations = {
        "left": cycle([
            tk.PhotoImage(file="assets/walk_left.png"),
            tk.PhotoImage(file="assets/walk_left1.png")
        ]),
        "right": cycle([
            tk.PhotoImage(file="assets/walk_right.png"),
            tk.PhotoImage(file="assets/walk_right1.png")
        ])
    }

    # Canvas for transparent bg
    canvas = tk.Canvas(pet_window, width=100, height=100, bg="green", highlightthickness=0)
    canvas.pack()

    # click area
    canvas.tag_bind("click_area", "<Button-1>", click_pet)
    canvas.create_rectangle(0, 0, 100, 100, outline="", fill="", tags="click_area")

    # Position near bottom
    screen_height = pet_window.winfo_screenheight()
    y = screen_height - 75

    # Create pet
    pet = Pet(pet_window, canvas, x=20, y=y, walk_animations=walk_animations)

    # start moving
    pet.move()

    tk.mainloop()