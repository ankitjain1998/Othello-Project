# ICS 32 - Fall 2017

# Project #5: The Width of a Circle (Part 2)

# Name: Ankit Jain
# ID: 96065117
# UCINetID: jaina2

# Game Logic Module

'''
This module consists of functions
and classes which formulate the main
logic and algorithm which help in
basically playing the game and creates
the window where the game is basically
played as per what information the user
inputs
'''

import tkinter

class GameState:
    '''
    This class represents the current
    state of the game, basically this
    class is updated each time a move
    is made
    '''
    def __init__(self,rows:int,columns:int,winning_condition:str,first_turn:str):
        '''
        The class is initialized
        by the number of rows, columns
        winning condition and first turn
        ,which is entered by the user in
        the user interface module
        '''
        self._rows = rows
        self._col = columns
        self._gamestate = self.create_board()
        self._first_player = BoardElement(first_turn)
        self._player = BoardElement(first_turn)
        self._winning = winning_condition
        self.changer = 0
        self.height = 60
        self.width = 60
        self.ready = False
        self.game_end = False
        self.first_turn_text = ''
        self.play_text = 'Placed Black Discs\nPlace White now!'
        self.canvas_width = self.width * self._col
        self.canvas_height = self.height * self._rows
        self.default_font = ('Times New Roman', 16)
        self.root_window = tkinter.Tk()
        self.create_window()
        
    def get_gameState(self) -> list:
        '''
        Returns the current
        gamestate of the board
        '''
        return self._gamestate
    
    def create_board(self) -> list:
        '''
        Creates the two dimensional list board
        as per the board dimensions so given
        '''
        rows = self._rows
        columns = self._col
        board = []
        for row in range(rows):
            column = [BoardElement('.')]*columns
            board.append(column)
        return board
    
    def _get_count(self) -> list:
        '''
        Method returns a list of different
        counts of the various elements on the
        board 
        '''
        board_list = self.get_gameState()
        black_count = 0
        white_count = 0
        empty_count = 0
        for row in board_list:
            for element in row:
                if element._get_element() == 'B':
                    black_count += 1
                if element._get_element() == 'W':
                    white_count += 1
                if element._get_element() == '.':
                    empty_count += 1
        counts = [black_count, white_count, empty_count]
        return counts
    
    def print_board(self):
        '''
        Method is used to print the board in appropriate
        form along with the count of the black and white
        elements
        '''
        board_list = self.get_gameState()
        board = ''
        counts = self._get_count()
        black_count = counts[0]
        white_count = counts[1]
        for row in board_list:
            for element in row:
                if row.index(element) == len(row) - 1:
                    board += element._get_element() 
                else:
                    board += element._get_element() + ' '
            if board_list.index(row) == len(board_list) - 1:
                continue
            else:
                board += '\n'
        print('B: {}  W: {}'.format(black_count,white_count))
        print(board)
        
    def play_move(self,turn:str,move:list):
        '''
        Method is used to implement the changes as per
        the move entered for the player whose turn it is
        to play
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object.check_valid_move(board_list,move) == True:
            board_list = self._change_east(turn,move)
            board_list = self._change_west(turn,move)
            board_list = self._change_north(turn,move)
            board_list = self._change_south(turn,move)
            board_list = self._change_southeast(turn,move)
            board_list = self._change_northwest(turn,move)
            board_list = self._change_northeast(turn,move)
            board_list = self._change_southwest(turn,move)
            self._gamestate = board_list
            return self._gamestate
        else:
            return self._gamestate
        
    def _change_east(self,turn:str,move:list) -> list:
        '''
        Method used to change all the elements
        in the east direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_east(board_list,move) == True:
            max_col_index = len(board_list[0])-1
            element = turn_object._get_element()
            row = move[0] - 1
            column = move[1] - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while column != max_col_index:
                column = column + 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_west(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the west direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_west(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while column != 0:
                column = column - 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_north(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the north direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_north(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while row != 0:
                row = row - 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_south(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the south direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_south(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            max_row_index = len(board_list) - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while row != max_row_index:
                row = row + 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_southeast(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the southeast direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_southeast(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            max_row_index = len(board_list) - 1
            max_col_index = len(board_list[0]) - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while row != max_row_index and column != max_col_index:
                row = row + 1
                column = column + 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_northwest(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the northwest direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_northwest(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while row != 0 and column != 0:
                row = row - 1
                column = column - 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_northeast(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the northeast direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_northeast(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            max_col_index = len(board_list[0]) - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while row != 0 and column != max_col_index:
                row = row - 1
                column = column + 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def _change_southwest(self,turn:str,move:list)->list:
        '''
        Method used to change all the elements
        in the southwest direction as per the turn
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        if turn_object._check_southwest(board_list,move) == True:
            row = move[0] - 1
            column = move[1] - 1
            max_row_index = len(board_list) - 1
            board_list[row][column] = board_list[row][column]._switch_to(turn)
            while column != 0 and row != max_row_index:
                row = row + 1
                column = column - 1
                if board_list[row][column]._get_element() == turn_object._get_element():
                    break
                else:
                    board_list[row][column] = board_list[row][column]._switch_to(turn)
            return board_list
        else:
            return board_list
        
    def check_moves_left(self,turn:str) -> bool:
        '''
        Method to check if the player has
        any valid moves left in the current gamestate
        '''
        board_list = self.get_gameState()
        turn_object = BoardElement(turn)
        validator = []
        for row in range(len(board_list)):
            for col in range(len(board_list[0])):
                if board_list[row][col]._get_element() == '.':
                    if turn_object.check_valid_move(board_list,[row + 1,col + 1]) == True:
                        validator.append([row + 1,col + 1])
                    else:
                        pass
                else:
                    pass
        if len(validator) == 0:
            return False
        else:
            return True
        
    def game_over(self) -> bool:
        '''
        Method to test whether game is
        over or not
        '''
        board_list = self.get_gameState()
        counts = self._get_count()
        empty_count = counts[2]
        if empty_count == 0:
            return True
        else:
            if self.check_moves_left('B') == False and self.check_moves_left('W') == False:
                return True
            else:
                return False
            
    def winner(self):
        '''
        Method which outputs the winner
        when game is over
        '''
        mode = self._winning
        board_list = self.get_gameState()
        counts = self._get_count()
        black_count = counts[0]
        white_count = counts[1]
        if self.game_over() == True:
            if mode == '>':
                if black_count == white_count:
                    return 'None'
                elif black_count > white_count:
                    return 'Black'
                elif white_count > black_count:
                    return 'White'
            if mode == '<':
                if black_count == white_count:
                    return 'None'
                elif black_count < white_count:
                    return 'Black'
                elif white_count < black_count:
                    return 'White'
        else:
            pass
        
    def create_window(self):
        '''
        Creates the window onto to which
        the entire game will be played
        '''
        self.root_window.title('Othello Full Game')
        sticky_stuff = tkinter.N + tkinter.S + tkinter.W + tkinter.E
        self._window = tkinter.Canvas(master = self.root_window, width = self.canvas_width, height = self.canvas_height,background = 'green')
        self._window.grid(row = 2, column = 1, padx = 0, pady = 0,sticky = sticky_stuff)
        self._current = tkinter.Canvas(master = self.root_window, width = self.canvas_width, height = self.height,background = 'white')
        self._current.grid( row = 1, column = 1, padx = 0, pady = 0, sticky = sticky_stuff)
        self.turn = tkinter.Canvas(master = self.root_window, width = self.canvas_width, height = self.height/2,background = 'white')
        self.turn.grid(row = 3, column = 1, padx = 0, pady = 0,sticky = sticky_stuff)
        self._window.bind('<Configure>', self.resize)
        self._player = BoardElement('B')
        self._window.bind('<Button-1>',self.place_initial)
        self.root_window.rowconfigure(2, weight = 2)
        self.root_window.columnconfigure(1, weight = 1)
        self.root_window.rowconfigure(1, weight = 1)
        self.display_canvas()
        self.display_gamestate()

    def display_gamestate(self):
        '''
        Method displays the count of the gamestate
        at that current point of time
        '''
        counter = self._get_count()
        message = tkinter.Label(master = self.root_window, text = 'Othello',font = self.default_font,background = 'white')
        black_count = tkinter.Label(master = self.root_window, text = 'Black: {}  '.format(counter[0]),
                                    font = self.default_font, justify = tkinter.RIGHT,background = 'white')
        white_count = tkinter.Label(master = self.root_window, text = 'White: {}  '.format(counter[1]),
                                    font = self.default_font, justify = tkinter.LEFT,background = 'white')
        message.grid(row = 1,column = 1)
        black_count.grid(row = 1, column = 1, sticky = tkinter.W)
        white_count.grid(row = 1, column = 1, sticky = tkinter.E)
        if self.game_end == False:
            if self.ready == True:
                self.turn.destroy()
                if self._player._get_element() == 'B':
                    turn_text = 'Turn: Black'
                else:
                    turn_text = 'Turn: White'
                self.turn = tkinter.Label(master = self.root_window, text = turn_text, justify = tkinter.CENTER, font = self.default_font)
                self.turn.grid(row = 3, column = 1)
        else:
            winner = 'Winner: ' + self.winner()
            winner_label = self.turn = tkinter.Label(master = self.root_window, text = winner, justify = tkinter.CENTER, font = self.default_font)
            winner_label.grid(row = 3, column = 1)
        
    def form_grid(self):
        '''
        Method forms the grid onto which actions
        are later made
        '''
        rows = self._rows
        col = self._col
        for i in range(col):
            self._window.create_line(i*self.width, 0,i*self.width,rows*self.height,width = 2)
        for j in range(rows):
            self._window.create_line(0,j*self.height,col*self.width,j*self.height,width = 2)

    def display_canvas(self):
        '''
        Displays the game window as per the moves
        so made
        '''
        self.form_grid()
        row = self._rows
        col = self._col
        board = self._gamestate
        for rows in range(row):
            for columns in range(col):
                if board[rows][columns]._get_element() != '.':
                    self._window.create_rectangle(int((columns*self.width)+self.width*0.05) ,
                                                int((rows*self.height)+self.height*0.05) ,
                                                int(((columns+1)*self.width)-self.width*0.075) ,
                                                int(((rows+1)*self.height)-self.height*0.075) ,
                                                fill = board[rows][columns]._get_color(), outline = board[rows][columns]._get_color())
                    

    def resize(self,event: tkinter.Event):
        '''
        Enables resizing of the overall window
        '''
        self._window.delete(tkinter.ALL)
        self.height = self._window.winfo_height()/self._rows
        self.width = self._window.winfo_width()/self._col
        self.display_canvas()
        self._current.delete(tkinter.ALL)
        self.display_gamestate()

    def place_initial(self,event:tkinter.Event):
        '''
        Enables the placing of the initial elements to start the game
        '''
        y = int(event.x/self.width)
        x = int(event.y/self.height)
        player = self._player._get_element()
        self._gamestate[x][y] = BoardElement(player)
        self.next_button = tkinter.Button(master = self.root_window, text = self.play_text, width = 3, height = 2,
                                      font = ('Times New Roman', 12), command = self.player_changer)
        self.next_button.grid(row = 5,column = 1, sticky = tkinter.N+tkinter.E+tkinter.W+tkinter.S)
        self.display_canvas()
        self.display_gamestate()

    def player_changer(self):
        '''
        Command which changes the player to white
        to enable to place the white elements when
        changer is zero, and when it is when it disables
        the initializing button and allows the game to be started
        with the first player putting in the first move
        '''
        if self.changer == 0:
            self.changer += 1
            self._player = BoardElement('W')
            if self._first_player._get_element() == 'B':
                self.first_turn_text = ' Black Goes First'
            else:
                self.first_turn_text = ' White Goes First'
            self.play_text = 'Placed White Discs! Lets play!\n' + self.first_turn_text 
        else:
            self.next_button['state'] = tkinter.DISABLED
            self.ready = True
            self._player = self._first_player
            self._window.bind('<Button-1>',self.click_move)
        
    def click_move(self,event:tkinter.Event):
        '''
        Method to enable the click event and
        play the game when clicked and update
        the board as per the click so made
        '''
        y = int(event.x/self.width)
        x = int(event.y/self.height)
        if self.game_over() == False:
            if self.check_moves_left(self._player._get_element()) == True:
                if self._player.check_valid_move(self._gamestate,[x + 1,y + 1]) == True:
                    self._gamestate = self.play_move(self._player._get_element(),[x + 1,y + 1])
                    if self._player._get_element() == 'B':
                        self._player = self._player._switch_to('W')
                    else:
                        self._player = self._player._switch_to('B')
                    self.display_canvas()
                    self.display_gamestate()
                else:
                    self.display_invalid()
            else:
                self.display_no_valid_moves_left()
                if self._player._get_element() == 'B':
                    self._player = self._player._switch_to('W')
                else:
                    self._player = self._player._switch_to('B')
                self.display_canvas()
                self.display_gamestate()
        else:
            self.game_end = True
            self._gamestate = self.play_move(self._player._get_element(),[x + 1,y + 1])
            self.display_canvas()
            self.display_gamestate()
            self.display_winner()

    def display_no_valid_moves_left(self):
        '''
        Displays a window for when there are no moves
        left for the player to make
        '''
        self.none_left = tkinter.Tk()
        self.none_left.title('No Valid Moves Left')
        if self._player._get_element() == 'B':
            none_text = 'Player Black Has No Valid Moves!'
        else:
            none_text = 'Player White Has No Valid Moves!'
        none_label = tkinter.Label(master = self.none_left, text = none_text,
                                     font = ('Times New Roman', 12))
        none_label.grid(row = 0, padx = 10, pady = 10, sticky = tkinter.N+tkinter.E+tkinter.W+tkinter.S)
        okay = tkinter.Button(master = self.none_left, text = 'Okay', width = 4, height = 1,
                                      font = ('Times New Roman', 10), command = self.none_okay)
        okay.grid(row = 1, padx = 10, pady = 10)

    def none_okay(self):
        '''
        Destroys the no valid moves left window
        '''
        self.none_left.destroy()

    def display_invalid(self):
        '''
        Acts as a pop up to show that there
        are the move so made was invalid
        '''
        self.invalid_window = tkinter.Tk()
        self.invalid_window.title('Invalid Move')
        invalid_label = tkinter.Label(master = self.invalid_window, text = 'Invalid Move!\nTry Again!',
                                     font = ('Times New Roman', 12))
        invalid_label.grid(row = 0, padx = 10, pady = 10, sticky = tkinter.N+tkinter.E+tkinter.W+tkinter.S)
        okay = tkinter.Button(master = self.invalid_window, text = 'Okay', width = 4, height = 1,
                                      font = ('Times New Roman', 10), command = self.invalid_okay)
        okay.grid(row = 1, padx = 10, pady = 10)

    def invalid_okay(self):
        '''
        Destroys invalid move window
        '''
        self.invalid_window.destroy()

    def display_winner(self):
        '''
        Displays the winner in a window
        when the game is over
        '''
        winner = 'Winner: ' + self.winner()
        self.winner_window = tkinter.Tk()
        winner_label = tkinter.Label(master = self.winner_window, text = winner,
                                     font = ('Times New Roman', 24))
        winner_label.grid(row = 0, padx = 50, pady = 50, sticky = tkinter.N+tkinter.E+tkinter.W+tkinter.S)
        end_game = tkinter.Button(master = self.winner_window, text = 'Click To Exit!', width = 10, height = 3,
                                      font = self.default_font, command = self.bye)
        end_game.grid(row = 1, padx = 10, pady = 10)

    def bye(self):
        '''
        Destroys the main root window and
        winner window when the game is over
        '''
        self.root_window.destroy()
        self.winner_window.destroy()
            
    def play(self):
        '''
        To initialize the tkinter mainloop and enable
        the entire game to be played
        '''
        self.root_window.mainloop()
        
                            
class BoardElement:
    '''
    Gamestate is a list of BoardElements
    on which actions are made
    '''
    def __init__(self,element:str):
        '''
        Initialized by a string as
        per the player element
        '''
        self._element = element
    def _get_element(self) -> str:
        '''
        Returns the string element of the object which
        defines the object
        '''
        return self._element
    def _switch_to(self,turn:str) -> str:
        '''
        Switches the element to which ever requested
        '''
        return BoardElement(turn)
    def _check_north(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in north direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            element = self._get_element()
            if row - 1 < 0:
                return False
            else:
                north_element = board_list[row - 1][column]._get_element()
                if north_element != element and north_element != '.':
                    assert row - 2 >= 0
                    checker_element = board_list[row - 2][column]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while row != 0:
                            row = row - 1
                            norther_element = board_list[row][column]._get_element()
                            if norther_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False
        
    def _check_south(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in south direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            max_row_index  = len(board_list) - 1
            element = self._get_element()
            if row + 1 > max_row_index:
                return False
            else:
                south_element = board_list[row + 1][column]._get_element()
                if south_element != element and south_element != '.':
                    assert row + 2 <= max_row_index
                    checker_element = board_list[row + 2][column]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while row != max_row_index:
                            row = row + 1
                            souther_element = board_list[row][column]._get_element()
                            if souther_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False
        
    def _check_east(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in east direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            max_col_index  = len(board_list[0]) - 1
            element = self._get_element()
            if column + 1 > max_col_index:
                return False
            else:
                east_element = board_list[row][column + 1]._get_element()
                if east_element != element and east_element != '.':
                    assert column + 2 <= max_col_index
                    checker_element = board_list[row][column + 2]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while column != max_col_index:
                            column = column + 1
                            easter_element = board_list[row][column]._get_element()
                            if easter_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False

    def _check_west(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in west direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            element = self._get_element()
            if column - 1 < 0:
                return False
            else:
                west_element = board_list[row][column - 1]._get_element()
                if west_element != element and west_element != '.':
                    assert column - 2 >= 0
                    checker_element = board_list[row][column - 2]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while column != 0:
                            column = column - 1
                            wester_element = board_list[row][column]._get_element()
                            if wester_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False
        
    def _check_southeast(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in southeast direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            max_row_index  = len(board_list) - 1
            max_col_index = len(board_list[0]) - 1
            element = self._get_element()
            if row + 1 > max_row_index or column + 1 > max_col_index:
                return False
            else:
                southeast_element = board_list[row + 1][column + 1]._get_element()
                if southeast_element != element and southeast_element != '.':
                    assert row + 2 <= max_row_index
                    assert column - 2 <= max_col_index
                    checker_element = board_list[row + 2][column + 2]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while row != max_row_index and column != max_col_index:
                            row = row + 1
                            column = column + 1
                            souther_element = board_list[row][column]._get_element()
                            if souther_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False
        
    def _check_northwest(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in northwest direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            element = self._get_element()
            if row - 1 < 0 or column - 1 < 0:
                return False
            else:
                northwest_element = board_list[row - 1][column - 1]._get_element()
                if northwest_element != element and northwest_element != '.':
                    assert row - 2 >= 0
                    assert column - 2 >= 0
                    checker_element = board_list[row - 2][column - 2]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while row != 0 and column != 0:
                            row = row - 1
                            column = column - 1
                            northwester_element = board_list[row][column]._get_element()
                            if northwester_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False
        
    def _check_northeast(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in northeast direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            element = self._get_element()
            max_col_index = len(board_list[0])
            if row - 1 < 0 or column + 1 > max_col_index:
                return False
            else:
                northeast_element = board_list[row - 1][column + 1]._get_element()
                if northeast_element != element and northeast_element != '.':
                    assert row - 2 >= 0
                    assert column + 2 <= max_col_index
                    checker_element = board_list[row - 2][column + 2]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while row != 0 and column != max_col_index:
                            row = row - 1
                            column = column + 1
                            northeaster_element = board_list[row][column]._get_element()
                            if northeaster_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False
        
    def _check_southwest(self,board_list:list,move:list) -> bool:
        '''
        Checks if move is valid in southwest direction
        '''
        try:
            row = move[0] - 1
            column = move[1] - 1
            max_row_index  = len(board_list) - 1
            element = self._get_element()
            if row + 1 > max_row_index or column - 1 < 0:
                return False
            else:
                southwest_element = board_list[row + 1][column - 1]._get_element()
                if southwest_element != element and southwest_element != '.':
                    assert row + 2 <= max_row_index
                    assert column - 2 >= 0
                    checker_element = board_list[row + 2][column - 2]._get_element()
                    if checker_element != '.':
                        iterator = 0
                        while row != max_row_index and column != 0:
                            row = row + 1
                            column = column - 1
                            southwester_element = board_list[row][column]._get_element()
                            if southwester_element == element:
                                iterator += 1
                                break
                            else:
                                pass
                        if iterator != 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        except:
            return False

    def check_valid_move(self,board_list:list,move:list) -> bool:
        '''
        Checks if requested move is valid in any of the
        8 directions
        '''
        try:
            assert move[0] <= len(board_list)
            assert move[1] <= len(board_list[0])
            row = move[0] - 1
            column = move[1] - 1
            validator = 0
            if board_list[row][column]._get_element() == '.':
                if self._check_north(board_list,move) == True:
                    validator += 1
                if self._check_south(board_list,move) == True:
                    validator += 1
                if self._check_east(board_list,move) == True:
                    validator += 1
                if self._check_west(board_list,move) == True:
                    validator += 1
                if self._check_southeast(board_list,move) == True:
                    validator += 1
                if self._check_northwest(board_list,move) == True:
                    validator += 1
                if self._check_northeast(board_list,move) == True:
                    validator += 1
                if self._check_southwest(board_list,move) == True:
                    validator += 1
                if validator >= 1:
                    return True
                else:
                    return False                
            else:
                return False
        except:
            return False

    def _get_color(self):
        '''
        Returns appropriate color
        as per the element disc
        '''
        if self._get_element() == 'B':
            color = 'black'
        if self._get_element() == 'W':
            color = 'white'
        return color



