import tkinter as tk
from navigation import open_home
from navigation import open_pet

root = tk.Tk()
root.withdraw() # hide blank window

open_home(root)
open_pet(root)

tk.mainloop()
