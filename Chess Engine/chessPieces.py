from config import HEIGHT, WIDTH
import pygame
from copy import deepcopy


class Piece:

    def __init__(self, color):
        self.hasMoved = False # Need to make True later on
        self.color = color

    def __str__(self):
        return f"{self.color[0]}{self.symbol}"

    def __repr__(self):
        return self.__str__()
class Pawn(Piece):
    symbol = "p"

    def legalMoves(self, board, row, col):
        moves = []
        tempboard = deepcopy(board)
        # move up one square

        if row+1<8 and board[row+1][col]==None: #if the potential move is in bounds, and the square is empty
            tempboard[row][col]=None
            tempboard[row+1][col]=board[row][col]
            moves.append(tempboard)
            print("Reached")
        tempboard = deepcopy(board)

        #to move up two squares
        if not self.hasMoved: # if the pawn has not moved
            print(row)
            if row+2<8 and board[row+2][col] is None and board[row+1][col] is None: # if the potential move is in bounds, and the square is empty
                tempboard[row][col]=None
                tempboard[row+2][col]=board[row][col]
                moves.append(tempboard)
        return moves


