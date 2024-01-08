# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:31:46 2023

@author: Tom
"""

import tkinter as tk

class sudoku_gui():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Sudoku.exe')
        self.height = 900
        self.width = 1600
        self.window.geometry(f"{self.width}x{self.height}")
        self.font_size = 13
        
    def draw_window(self):
        tk.mainloop()
        
    def create_text_area(self,value,i,j):
        text_frame = tk.Frame(self.window, width=5, height=10)
        text_frame.grid_propagate(False)
        
        t1 = tk.Text(self.window,height = 5, width = 10)
        
        t1.grid(row = i, column = j)
        
        if value !=0:
            t1.insert("end-1c", value)
            t1.tag_configure("tag_name",justify='center')
            t1.tag_add("tag_name", "1.0", "end")
            t1.config(font=('Times New Roman', self.font_size, 'bold'))
            t1.config(state=tk.DISABLED)
        else:
            t1.config(font=('Times New Roman', self.font_size))
            t1.insert("end-1c", ' ')
            t1.tag_configure("tag_name",justify='center')
            t1.tag_add("tag_name", "1.0", "end")
        if ((i // 3 == 0 or i // 3 == 2) and (j // 3 == 0 or j // 3 == 2)) or (i // 3 == 1 and j // 3 == 1):
            t1.config(bg = 'light blue')
        else:
            t1.config(bg = 'light grey')
    def check_completion(self,complete_board,completion_var):
        current_state = []
        for i in range(9):
            row_lst = []
            for j in range(9):
                value = self.window.grid_slaves(i,j)[0].get("1.0",tk.END).replace('\n','').replace(' ','')
                if value != '':
                    row_lst.append(int(value))
                else:
                    row_lst.append(0)
            current_state.append(row_lst)
        #for row in current_state:
        #   print(row)
        
        if complete_board == current_state:
            completion_var.set('Correct!')
            return True
        else:
            completion_var.set('Wrong!')
            return False
        
    def setup_gui(self):
        self.draw_window()
        
if __name__ == '__main__':
    gui = sudoku_gui()
    for i in range(9):
        for j in range(9):
            gui.create_text_area(1, i, j)
    test_board = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    print(gui.check_completion(complete_board = test_board))
    
    gui.setup_gui()