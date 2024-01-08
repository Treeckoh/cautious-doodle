# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:58:52 2023

@author: Tom
"""

from sudoku_class import *
from sudoku_gui import *

def Main():
    sudoku = Sudoku()
    sudoku.create_game('test_comp')
    #for row in sudoku.playing_board:
    #    print(row)
    #print('\n')
    gui = sudoku_gui()
    for i in range(9):
        for j in range(9):
            gui.create_text_area(sudoku.playing_board[i][j], i, j)
    
    completion_state = tk.StringVar()
    completion_label = tk.Label(gui.window, 
                                textvariable = completion_state,
                                bg = 'light blue',
                                height = 5,
                                width = 13,
                                bd = 2)
    completion_label.grid(row = 1, column = 10)
    
    def btn_script():
        gui.check_completion(sudoku.complete_board, completion_state)
    
    complete_button = tk.Button(gui.window, text = "Check Completion", 
                                command = btn_script,
                                bg = 'light green',
                                height = 5)
    complete_button.grid(row = 0, 
                         column = 10)
    gui.setup_gui()
    
if __name__ == '__main__':
    
    Main()