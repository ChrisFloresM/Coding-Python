#Christian Flores 17/02/2021

from itertools import combinations

S, K = input().split()
[print("".join(element)) for i in range(1, (int(K)+1)) for element in combinations(sorted(S), i)]

