#Christian Flores 12/02/2021
#Día 3: Condicionales
#Numeros raros y no raros

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

mod = N % 2
if mod == 0:
    if (N >= 2 and N <= 5) or (N > 20):
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")