#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    result = [0,0,0]
    # Write your code here
    for x in arr:
        if(x > 0):
            result[0] += 1
        elif(x < 0):
            result[1] += 1
        else:
            result[2] += 1
        
    print( '{:.6}'.format((result[0] / len(arr))) )
    print( '{:.6}'.format((result[1] / len(arr))) )
    print( '{:.6}'.format((result[2] / len(arr))) )

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
