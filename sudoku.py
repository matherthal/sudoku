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

_board = []

def initialize(n, values):
    possible = deque(range(1, n+1))
    possible_str = [str(p) for p in possible]
    
    try:
        for i in range(n):
            _board.append([])
            for j in range(n):
                v = values[i*n + j]
                if v in possible_str:
                    _board[i].append(deque([int(v)]))
                else:
                    _board[i].append(possible.copy())
    except:
        draw()
        raise

def remove_dups_row(n, pos_i, pos_j):
    value = _board[pos_i][pos_j][0]

    for i in range(n):
        if i == pos_i:
            continue
        if value in _board[i][pos_j]:
            _board[i][pos_j].remove(value)

def remove_dups_col(n, pos_i, pos_j):
    value = _board[pos_i][pos_j][0]

    for j in range(n):
        if j == pos_j:
            continue
        if value in _board[pos_i][j]:
            _board[pos_i][j].remove(value)

def remove_dups_quadrant(n, pos_i, pos_j):
    value = _board[pos_i][pos_j][0]

    quad_size = int(sqrt(n))
    quad_start_i = int(pos_i / quad_size) * quad_size
    quad_start_j = int(pos_j / quad_size) * quad_size
    quad_end_i = quad_start_i + quad_size
    quad_end_j = quad_start_j + quad_size
    
    for i in range(quad_start_i, quad_end_i):
        for j in range(quad_start_j, quad_end_j):
            if i == pos_i and j == pos_j:
                continue
            if value in _board[i][j]:
                _board[i][j].remove(value)

def count():
    total = 0
    for i in range(len(_board)):
        for j in range(len(_board[i])):
            total += len(_board[i][j])
    return total

def draw():
    for i in range(len(_board)):
        print()
        for j in range(len(_board[i])):
            for k in _board[i][j]:
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
    
    # Create a _board after a list of values with all possible values filled in empty possitions
    initialize(n, list_values)

    max_values = n**2
    last_count = 0
    
    while True:
        for i in range(n):
            for j in range(n):
                if len(_board[i][j]) == 1:
                    remove_dups_row(n, i, j)
                    remove_dups_col(n, i, j)
                    remove_dups_quadrant(n, i, j)
       
        curr_count = count()
        
        if curr_count == max_values:
            break
        
        if curr_count == last_count:
            print('Cannot finish...')
            break
        last_count = curr_count

    end = datetime.datetime.now()
    elapsed = end - start
    
    print('Elapsed time: {} milliseconds'.format(elapsed.microseconds / 1000))
    
    draw()

run(9, values)