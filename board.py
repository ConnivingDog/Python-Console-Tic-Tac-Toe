#!/bin/python3

import os
import sys
import time

class Board():

    row = 3
    col = 3
    piece = 0

    BoardPieces = [' ', ' ', ' ',
                   ' ', ' ', ' ',
                   ' ', ' ', ' ', ]

    def __init__(self):
        self.Draw()
    
    def Draw(self):
        for i in range(self.row):
            self.DrawHorizontal(i)
            self.DrawVertical(i)
        self.DrawHorizontal(i)
        print('\n')

    def DrawHorizontal(self, i):
        print('+---' * self.col, end="")
        print('+')

    def DrawVertical(self, i):
        print('| {} '.format( * self.col, self.BoardPieces[i]), end="")
        print('|')

    def DisplayPiece(self, i):
        return self.BoardPieces

    def PlacePiece(piece):
        BoardPieces[piece - 1] = 'x'