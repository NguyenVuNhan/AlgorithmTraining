#https://www.hackerrank.com/challenges/2d-array/problem

import os
import sys

def hourglassSum(arr):
    highest = -sys.maxsize
    
    for i in range(1,5):
        for j in range(1,5):
            hour_glass_val = arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i][j] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
            highest = hour_glass_val if hour_glass_val > highest else highest
    
    return highest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
