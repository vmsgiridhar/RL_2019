# -*- coding: utf-8 -*-

# This is from the PluralSight course

import numpy as np

N = 8

board_state_memory = {}

board = np.zeros((N, N), np.int8)

def create_board_string(board):
    board_string = ''
    for i in range(N):
        for j in range(N):
            board_string += str(board[i][j])
    return board_string

board_copy = board.copy()
board_copy[0,1] = 1

create_board_string(board_copy)