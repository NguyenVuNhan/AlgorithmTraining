#https://www.hackerrank.com/challenges/breaking-best-and-worst-records

import os

def breakingRecords(scores):
    best = scores[0]
    worse = scores[0]
    
    b_counter = 0
    w_counter = 0
    
    for score in scores[1:]:
        if best < score:
            b_counter += 1
            best = score
        if worse > score:
            w_counter += 1
            worse = score
        
    return [b_counter, w_counter]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
