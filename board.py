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
        self.DrawHorizontal()
        self.DrawVertical()
        print('\n')

    def DrawHorizontal(self):
        print('+---' * self.col, end='')
        print('+')

    def DrawVertical(self):
        end = 2
        for i in range(self.col * self.row):
            print('| {} '.format(self.BoardPieces[i]), end='')
            if i == end:
                print('|')
                self.DrawHorizontal()
                end+=3

    def PlacePiece(piece):
        BoardPieces[piece - 1] = 'x'