#Christian Flores 19/02/2021

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    print(len(max(bin(n)[2:].split("0"))))

    
