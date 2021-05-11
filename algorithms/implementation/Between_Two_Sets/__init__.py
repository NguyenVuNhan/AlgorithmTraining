# https://www.hackerrank.com/challenges/between-two-sets/problem

import sys
import os
from math import gcd
from functools import reduce

def lcm(a, b):
    return (a*b)//gcd(a,b)

def getTotalX(a, b):
    _lcm = reduce(lcm, a, 1)
    _gcd = reduce(gcd, b)
        
    t_lcm = _lcm

    count = 0
    for i in range(_lcm, _gcd+_lcm, _lcm):
        if(_gcd % i) == 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
