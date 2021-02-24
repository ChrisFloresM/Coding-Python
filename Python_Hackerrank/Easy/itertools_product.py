#Christian Flores 17/02/2021

from itertools import product

list_a = [int(i) for i in input().split()]
list_b = [int(i) for i in input().split()]

list_a.sort()
list_b.sort()

print(*product(list_a, list_b))

