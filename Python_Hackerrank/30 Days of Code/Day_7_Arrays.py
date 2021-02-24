#Christian Flores 16/02/2021

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    [print(f'{item}', end=" ") for item in arr]
