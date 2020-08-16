#sudoku.py
"""
Implementation of a Sudoku solver.
@Author: AlexG.
"""

import numpy as np

class SudokuBoard:

    def __init__(self):
        """ Initialize with empty board.
        0 indicates empty.
        """
        self.board = np.zeros((9, 9))
        
    def __str__(self):
        return np.array2string(self.board)
        
    def __iter__(self):
        for values in self.board:
            yield values
            
    def initialize(self, board):
        """ Initialize with predefined board. """
        self.board = board
            
    def isEmpty(self, row, col):
        """ Check if no number is yet specified.
        0 indicates empty. """
        return self.board[row, col] == 0
        
    def setNumber(self, row, col, value):
        self.board[row, col] = value
        
    def rowContains(self, row, value):
        """ Check if row already contains number. """
        return np.any(self.board[row, :] == value)
      
    def colContains(self, col, value):
        """ Check if column already contains number. """
        return np.any(self.board[:, col] == value)
        
    def blkContains(self, row, col, value):
        """ Check if block already contains number. """
        yb = (row // 3) * 3
        xb = (col // 3) * 3
        return np.any(self.board[yb:yb+3, xb:xb+3] == value)
        
    def isValidNumber(self, row, col, value):
        """ Number is in [1, 9] and does not yet exist in 
        row, column and block. """
        return value >= 1 and value <= 9 and \
            not self.rowContains(row, value) and \
            not self.colContains(col, value) and \
            not self.blkContains(row, col, value)
            
    def getValidNumbers(self, row, col):
        """ Get all possible valid numbers for position. """
        return [value for value in range(1, 9+1)
            if self.isValidNumber(row, col, value)]

    def copy(self):
        """ Copy class. """
        board = SudokuBoard()
        board.initialize(np.copy(self.board))
        return board            
        
def solve(board, callback=print):
    """ Get all possible solutions for given SudokuBoard. """
    for row, values in enumerate(board):
        for col, value in enumerate(values):
            if board.isEmpty(row, col):
                for guess in board.getValidNumbers(row, col):
                    board.setNumber(row, col, guess)
                    solve(board, callback=callback)
                    board.setNumber(row, col, 0)
                # if the code gets here, the board is unsolvable
                # or has been solved already on a different path
                return
    # if the code gets here, the board is solved.
    callback(board.copy())
    return
    
if __name__ == "__main__": 

    board = SudokuBoard()
    board.initialize(np.array([
        [6, 0, 5, 7, 2, 0, 0, 3, 9],
        [4, 0, 0, 0, 0, 5, 1, 0, 0],
        [0, 2, 0, 1, 0, 0, 0, 0, 4],
        [0, 9, 0, 0, 3, 0, 7, 0, 6],
        [1, 0, 0, 8, 0, 9, 0, 0, 5],
        [2, 0, 4, 0, 5, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 3, 0, 2, 0],
        [0, 0, 2, 9, 0, 0, 0, 0, 1],
        [3, 5, 0, 0, 6, 7, 4, 0, 8]]
        ))  
        
    solutions = []
    solve(board, callback = lambda board : solutions.append(board))
    for solution in solutions:
        print(solution)
       