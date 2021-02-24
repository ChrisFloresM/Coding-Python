#Christian Flores 17/02/2021

from itertools import permutations

S, K = input().split()
K = int(K)
[print("".join(element), end="\n") for element in sorted(list(permutations(S, K)))]
    


