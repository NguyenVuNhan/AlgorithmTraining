#https://www.hackerrank.com/challenges/magic-square-forming/problem

import os
from typing import List
from math import floor

"""
All magic squares
8 1 6 | 6 1 8          
3 5 7 | 7 5 3
4 9 2 | 2 9 4
-------------
4 9 2 | 2 9 4
3 5 7 | 7 5 3
8 1 6 | 6 1 8

8 3 4 | 4 3 8
1 5 9 | 9 5 1
6 7 2 | 2 7 6
-------------
6 7 2 | 2 7 6
1 5 9 | 9 5 1
8 3 4 | 4 3 8
"""
        
magic_squares = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
    [[2, 7, 6], [9, 6, 1], [4, 3, 8]],
]

def formingMagicSquare(s: List[List[int]]) -> int:
    totals = []
    for square in magic_squares:
        total = 0
        for row, s_row in zip(square, s):
            for i, j in zip(row, s_row):
                if not i == j:
                    total += abs(i - j)
        totals.append(total)
    return min(totals)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
