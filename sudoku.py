# coding: utf-8

values = """9 _ _ 4 _ _ _ _ 1
_ 7 6 _ 2 _ _ _ _
2 _ 1 9 _ _ _ _ 3
_ _ _ _ _ 2 4 _ _
6 _ 9 3 _ _ 7 _ _
4 _ _ 7 _ 5 8 _ _
_ 9 _ 5 3 _ 6 8 _
3 5 7 _ 6 _ _ _ _
_ _ _ _ 1 _ _ 9 _"""


import re
from collections import deque
from math import sqrt
import time

def initialize(n, values):
    possible = deque(range(1, n+1))
    possible_str = [str(p) for p in possible]
    board = []
    
    try:
        for i in range(n):
            board.append([])
            for j in range(n):
                v = values[i*n + j]
                if v in possible_str:
                    board[i].append(deque([int(v)]))
                else:
                    board[i].append(possible.copy())
    except:
        draw(board)
        raise
    return board

def remove_dups_row(n, board, pos_i, pos_j):
    value = board[pos_i][pos_j][0]

    for i in range(n):
        if i == pos_i:
            continue
        if value in board[i][pos_j]:
            board[i][pos_j].remove(value)

    return board

def remove_dups_col(n, board, pos_i, pos_j):
    value = board[pos_i][pos_j][0]

    for j in range(n):
        if j == pos_j:
            continue
        if value in board[pos_i][j]:
            board[pos_i][j].remove(value)
    
    return board

def remove_dups_quadrant(n, board, pos_i, pos_j):
    value = board[pos_i][pos_j][0]

    quad_size = int(sqrt(n))
    quad_start_i = int(pos_i / quad_size) * quad_size
    quad_start_j = int(pos_j / quad_size) * quad_size
    quad_end_i = quad_start_i + quad_size
    quad_end_j = quad_start_j + quad_size
    
    for i in range(quad_start_i, quad_end_i):
        for j in range(quad_start_j, quad_end_j):
            if i == pos_i and j == pos_j:
                continue
            if value in board[i][j]:
                board[i][j].remove(value)
    
    return board

def count(board):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            total += len(board[i][j])
    return total

def draw(board):
    for i in range(len(board)):
        print()
        for j in range(len(board[i])):
            for k in board[i][j]:
                print(k, end='')
            print(end=' ')
    print()

def run(n, values):
    import datetime
    start = datetime.datetime.now()
    
        # Remove spaces from begin and end of line
    values = re.sub(r"([\s\t]+\n[\s\t]+)|[\s\t]+", r"\n", values)
    
    # Split values by space and new line into a list
    list_values = re.split(' |\n', values)
    
    # Create a board after a list of values with all possible values filled in empty possitions
    board = initialize(n, list_values)

    max_values = n**2
    last_count = 0
    
    while True:
        for i in range(n):
            for j in range(n):
                if len(board[i][j]) == 1:
                    board = remove_dups_row(n, board, i, j)
                    board = remove_dups_col(n, board, i, j)
                    board = remove_dups_quadrant(n, board, i, j)
       
        curr_count = count(board)
        
        if curr_count == max_values:
            break
        
        if curr_count == last_count:
            print('Cannot finish...')
            break
        last_count = curr_count

    end = datetime.datetime.now()
    elapsed = end - start
    
    print('Elapsed time: {} milliseconds'.format(elapsed.microseconds / 1000))
    
    draw(board)

    return board

run(9, values)