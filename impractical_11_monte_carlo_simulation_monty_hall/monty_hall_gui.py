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


    def create_widgets(self):
        """
        create label, buttoms and text widgets for game
        """
        # create label widget to hold image of doors
        img = tk.PhotoImage(file='all_closed.png')
        self.photo_lbl = tk.Label(self.parent, image=img, text='', borderwidth = 0)
        self.photo_lbl.grid(row=0, column=0, columnspan=10, sticky='w')
        self.photo_lbl.image = img

        # create the instruction label
        instr_input = [
            ('Behind the door is cash', 1, 0, 5,'W'),
            ('Behind the other doors are goats',2,0,5,'W'),
            ('Pick a door:', 1,3,11,'E')
            ]
        for text, row, column, columnspan, sticky in instr_input:
            instr_lbl = tk.Label(self.parent, text=text)
            instr_lbl.grid(row=row, column=column, columnspan=columnspan, sticky=sticky, ipadx=30)

    
        # create radio buttons for getting initial user choice 
        self.door_choice = tk.StringVar()
        self.door_choice.set(None)

        a = tk.Radiobutton(self.parent, text='A', variable = self.door_choice, value = 'a', command= self.win_reveal)
        b = tk.Radiobutton(self.parent, text='B', variable = self.door_choice, value = 'b', command= self.win_reveal)
        c = tk.Radiobutton(self.parent, text='C', variable = self.door_choice, value = 'c',
        command= self.win_reveal)


        # create widgets for changing door choice
        self.change_door = tk.Label(self.parent, text='Change doors?')
        self.change_door.set(None)  

        instr_lbl = tk.Label(self.parent, text='Change doors?')
        instr_lbl.grid(row=2, column=3, columnspan=1, sticky='E')

        # yes and no buttons to change choice. init state is disabled. 
        self.yes = tk.Radiobutton(self.parent, state='disabled', text='Y', variable=self.change_door, value='y', command=self.show_final)
        self.no = tk.Radiobutton(self.parent, state='disabled', text='N', variable=self.change_door, value='n', command=self.show_final)

        # create text widgets for win statistics 
        defaultbg = self.parent.cgnet('bg')         # get the background color of the root window
        self.unchanged_win_txt = tk.Text(self.parent, width=20, height=1, wrap=tk.WORD, bg=defaultbg, fg='black', borderwidth=0)    # the text string will be added in show_final()
        self.changed_win_txt = tk.Text(self.parent, width=20, height=1, wrap=tk.WORD, bg=defaultbg, fg='black', borderwidth=0)
        
        # place the widgets in the frame 
        a.grid(row=1, column=4, stick='W', padx=20)             # left
        b.grid(row=1, column=4, sticky='N', padx=20)            # centre    
        c.grid(row=1, column=4, sticky='E', padx=20)            # right
        self.yes.grid(row=2, column=4, sticky='W', padx=20)
        self.no.grid(row=2, column=4, sticky='N', padx=20)
        self.unchanged_wins_txt.grid(row=1, column=5, columnspan=5)
        self.changed_wins_txt.grid(rows=2, column=5,columnspan=5)

        def update_image(self):
            """
            update current door images
            """
            img = tk.PhotoImage(file=self.img_file)    # self.img_files will be updated other methods
            self.photo_lbl.configure(image=img)        
            # label already exist. use configure() to reassign
            self.photo_lbl.image = img                  # to keep the img handle to avoid gc

        def win_reveal():
            """
            randomly pick winner door and reveal one of the unchosen door with a goat
            """
            door_list = list(self.doors)
            self.choice = self.door_choice.get()
            self.winner = random.choice(door_list)
            
            door_list.remove(self.winner)
            if self.choice in door_list:    # wrong guess
                 # open the remaining door other than chosen or winner door
                door_list.remove(self.choice)  
                self.reveal = door_list[0]
            else:                           # correct guess
                # open any door other than winner door
                self.reveal = random.choice(door_list)

        
            # enable switch buttons
            self.yes.config(state='normal')
            self.no.config(state = 'normal')
            self.change_door.set(None)

            # close doors 2 seconds after openning
            self.img_file = 'all_closed.png'
            self.parent.after(2000, self.update_image)
            
        def show_final():
            return


        


































