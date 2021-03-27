# ICS 32 - Fall 2017

# Project #5: The Width of a Circle (Part 2)

# Name: Ankit Jain
# ID: 96065117
# UCINetID: jaina2

# GUI Module

'''
This module is to allow the
game to be played between the
two users
'''

import tkinter
import othello_logic_gui
from tkinter import ttk

class StartGame:
    def __init__(self):
        '''
        Class to obtain the nessecary requirements
        to create the board to play the game
        '''
        self.decision_box = tkinter.Toplevel()
        self.decision_box.title('Othello Full Game')
        self.font = ('Times New Roman', 16)
        self.rows = 0
        self.cols = 0
        self.player = ''
        self.winning = ''
        frame = tkinter.Frame(master = self.decision_box)
        frame.grid(
            row = 6, column = 1, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)
        self.ready_button = tkinter.Button(
            master = frame, text = 'Ready to Play?', font = self.font,
            command = self.ready)
        self.ready_button.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.clicked = 0
        self.decision_box.rowconfigure(3,weight = 1)
        self.decision_box.columnconfigure(3,weight = 1)
        self.rows_label = tkinter.Label(master= self.decision_box, text='Choose Number of Rows:',font = self.font)
        self.rows_label.grid(row= 1, column= 1, padx= 20, sticky= tkinter.W)
        options = ('4','6','8','10','12','14','16')
        self.return_rows = ttk.Combobox(master=self.decision_box,
                                             values= options, width= 6)
        self.return_rows.grid(row=1, column=2, padx=10)
        self.cols_label = tkinter.Label(master= self.decision_box, text='Choose Number of Columns:',font = self.font)
        self.cols_label.grid(row= 2, column= 1, padx= 20, sticky= tkinter.W)
        self.return_cols = ttk.Combobox(master=self.decision_box,
                                             values = options, width= 6)
        self.return_cols.grid(row=2, column=2, padx=10)
        self.first_label = tkinter.Label(master= self.decision_box, text='Choose First Player:',font = self.font)
        self.first_label.grid(row= 3, column= 1, padx= 20, sticky= tkinter.W)
        options = ('Black','White')
        self.return_first = ttk.Combobox(master=self.decision_box,
                                             values = options, width= 6)
        self.return_first.grid(row=3, column=2, padx=10)
        self.winning_label = tkinter.Label(master= self.decision_box, text='Choose Winning Condition:',font = self.font)
        self.winning_label.grid(row= 4, column= 1, padx= 20, sticky= tkinter.W)
        options = ('Max','Min')
        self.return_winning = ttk.Combobox(master=self.decision_box,
                                             values = options, width= 6)
        self.return_winning.grid(row=4, column=2, padx=10)

    def ready(self):
        '''
        Obtains the required conditions
        in the appropriate form to play the game
        '''
        self.clicked += 1
        self.rows = int(self.return_rows.get())
        self.cols = int(self.return_cols.get())
        if self.return_first.get() == 'Black':
            self.player = 'B'
        else:
            self.player = 'W'
        if self.return_winning.get() == 'Max':
            self.winning = '>'
        else:
            self.winning = '<'
        self.decision_box.destroy()

    def display(self):
        '''
        Displays the window till the
        button is clicked to destroy
        the window
        '''
        self.decision_box.grab_set()
        self.decision_box.wait_window()

class PlayGame:
    def __init__(self):
        '''
        Class is used to initialize the game
        by first displaying the rules and
        starting off the game off with the
        options menus and then destroying those
        windows to actually play the game
        '''
        self.start_window = tkinter.Tk()
        self.start_window.title('Othello Full Game')
        self.rules_text = 'Othello is a strategy board game for two players, played on an uncheckered board\nTry to get most or least of your disks on the board to win\nContinue playing until every space on the board is occupied or no one can make another move.\nYou will select the board dimensions, first player and winning condition in the next step'
        self.rules_label = tkinter.Label(master = self.start_window, text = self.rules_text,
                                     font = ('Times New Roman', 14))
        self.next_button = tkinter.Button(master = self.start_window, text = 'Choose Options!', width = 14, height = 1,
                                      font = ('Times New Roman', 14), command = self.decide)
        self.rules_label.grid(row = 0, padx = 10, pady = 10)
        self.next_button.grid(row = 1, padx = 10, pady = 10)
        self.start_window.rowconfigure(0, weight = 3)
        self.start_window.rowconfigure(1, weight = 1)
        self.start_window.columnconfigure(0, weight = 1)
    def decide(self):
        '''
        Displays the options menu to choose
        and then enables users to play the game
        till the winner is achieved
        '''
        decider = StartGame()
        decider.display()
        if decider.clicked > 0:
            self.start_window.destroy()
            play_game = othello_logic_gui.GameState(decider.rows,decider.cols,decider.winning,decider.player)
            play_game.play()
    def play(self):
        '''
        Initializes tkinter mainloop for everything to take place
        '''
        self.start_window.mainloop()
        
if __name__ == '__main__':
    PlayGame().play()

    

        
        
