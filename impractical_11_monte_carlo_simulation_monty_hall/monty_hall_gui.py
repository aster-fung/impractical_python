import random
import tkinter as tk

class Game(tk.Frame):
    """
    GUI application for Monty Hall Problem game
    """

    doors = ('a','b','c') # use immutable tuples to store class attributes

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.img_file = 'all_closed.png'
        self.choice = ''
        self.winner = ''
        self.reveal = ''
        self.first_choice_wins = 0
        self.pick_change_wins = 0
        self.create_widgets()

































