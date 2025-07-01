import tkinter as tk
from PIL import Image, ImageTk

def click_pet(event=None):
    print("test")

def open_pet(root):
    pet_window = tk.Toplevel(root)
    pet_window.overrideredirect(True) # remove title bar
    pet_window.wm_attributes("-topmost", True) # pet is always on top
    pet_window.wm_attributes("-transparentcolor", "green") # make the background transparent (in green areas)

    image = Image.open("assets/stand_left.png").convert("RGBA")
    scale_factor = 2.5  # re-size by 2.5

    # new dimensions
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    image = image.resize((new_width, new_height), Image.NEAREST)

    standing_left = ImageTk.PhotoImage(image) #starting 'state'

    # use canvas
    canvas = tk.Canvas(pet_window, width=new_width, height=new_height, bg="green", highlightthickness=0)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=standing_left)

    # transparent clickable rectangle over image
    canvas.tag_bind("click_area", "<Button-1>", click_pet)
    canvas.create_rectangle(0, 0, new_width, new_height, outline="", fill="", tags="click_area")

    # corner positioning - get screen info
    screen_width = pet_window.winfo_screenwidth()
    screen_height = pet_window.winfo_screenheight()
    window_width = standing_left.width()
    window_height = standing_left.height()
    x = 20
    y = screen_height - window_height - 35 # pet sits above nav bar on my own computer
    pet_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # base state

    # all states

    tk.mainloop()
