#!/bin/python3

import os
import sys
import time

from board import Board

def PlayerMove():
    playermove = int(input('Enter your move [1-9] : '))
    Board.PlacePiece(playermove)

def AppHeader():
    print('*' * 25)
    print('* T I C - T A C - T O E *')
    print('*' * 25 + '\n')
    
def main():
    os.system('cls')
    AppHeader()
    Board()
    PlayerMove()

main()