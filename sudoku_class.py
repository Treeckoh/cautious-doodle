# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:46:08 2023

@author: Tom
"""
import random
import datetime
import copy

class Sudoku():
    def __init__(self):
        self.difficulty = None
        self.complete_board = None
        self._timeout = 1
        self.difficulties = {
            'test_comp':80,
            'easy': 39,
            'medium': 31,
            'hard' : 29}
        
    def _bb(self):
        return [[0 for i in range(9)] for i in range(9)]
    
    def valid_check(self, value, a, b):
        for i in range(9):
            for j in range(9):
                if (i == a and j != b) or (i != a and j == b):
                    if self.complete_board[i][j] == value:
                        return False
                if i != a and j != b and i // 3 == a // 3 and j // 3 == b // 3 and self.complete_board[i][j] == value:
                    return False    
        return True
    
    def generate_new(self):
        start_time = datetime.datetime.now()
        self.complete_board = self._bb()
        number_lst = [i for i in range(1,10)]
        random.shuffle(number_lst)
        for i in range(0,9):
            while 0 in self.complete_board[i]:
                time_dif = datetime.datetime.now() - start_time
                if time_dif.seconds > self._timeout:
                    self.complete_board = None
                    return
                random.shuffle(number_lst)
                for j in range(9):
                    for value in number_lst:
                        if self.valid_check(value,i,j):
                            self.complete_board[i][j] = value 
                        
    def set_sudoku(self, difficulty:str):
        self.playing_board = copy.deepcopy(self.complete_board)
        for num in range(81-self.difficulties[difficulty]):
            removed = False
            while not removed:
                i = random.choice([num for num in range(9)])
                j = random.choice([num for num in range(9)])
                if self.playing_board[i][j] != 0:
                    self.playing_board[i][j] = 0
                    removed = True
                    
    def create_game(self, difficulty):
        while not self.complete_board:
            self.generate_new()
        self.set_sudoku(difficulty = difficulty)

if __name__ == '__main__':
    test_sudoku = Sudoku()
    test_sudoku.create_game(45)
    for i in test_sudoku.complete_board:
        print(i)