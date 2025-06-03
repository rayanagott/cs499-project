import tkinter as tk

class PetWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="🐾", font=("Arial", 30))
        self.label.pack()
        self.label.bind("<Button-1>", self.pet_clicked)

    def pet_clicked(self, event):
        print("The pet says hi!")