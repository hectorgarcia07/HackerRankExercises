#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    timeDay = s.split(':')
    arr = [ timeDay[2][-2:], timeDay[2][:2] ]
    if(arr[0] == 'PM'):
        return f'{ 12 + int(timeDay[0]) if int(timeDay[0]) != 12 else 12 }:{timeDay[1]}:{arr[1]}'
    else:
        return f'{ "{:02d}".format(0) if int(timeDay[0]) == 12 else timeDay[0]}:{timeDay[1]}:{arr[1]}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()