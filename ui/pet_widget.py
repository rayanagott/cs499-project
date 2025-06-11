import tkinter as tk
from PIL import Image, ImageTk

def open_pet():
    root = tk.Tk()
    root.overrideredirect(True) # remove title bar
    root.wm_attributes("-topmost", True) # pet is always on top
    root.wm_attributes("-transparentcolor", "green") # make the background transparent (in green areas)

    image = Image.open("assets/stand_left.png").convert("RGBA")
    scale_factor = 2.5  # re-size by 2.5

    # new dimensions
    new_width = int(image.width * scale_factor)
    new_height = int(image.height * scale_factor)
    image = image.resize((new_width, new_height), Image.NEAREST)

    standing_left = ImageTk.PhotoImage(image) #starting 'state'

    label = tk.Label(root, image = standing_left, bg="green") # keep referene to photo
    label.image = standing_left
    label.pack()

    # corner positioning - get screen info
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = standing_left.width()
    window_height = standing_left.height()
    x = 20
    y = screen_height - window_height - 35 # pet sits above nav bar on my own computer
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # idle pet logic

#    interactive pet logic

