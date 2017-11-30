from tkinter import *
from tkinter import ttk

class Calculator:

    calc_value = 0.0

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def __init__(self, root):

        self.entry_value = StringVar(root, value="")

        root.title("Calculator")

        root.geometry("400x400")

        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton",
                        font="Serif 15",
                        padding=10)

        style.configure("TEntry",
                        font="Serif 18",
                        padding=10)

        self.number_entry = ttk.Entry(root,
                                      textvariable=self.entry_value, width=50)

        self.number_entry.grid(row=0, columnspan=4)

        self.button7 = ttk.Button(root, text="7",
                                 command=lambda: self.button_press('7'))