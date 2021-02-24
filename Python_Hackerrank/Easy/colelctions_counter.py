#Christian Flores 17/02/2021
from collections import Counter

n_sizes = int(input())
lst = [int(i) for i in input().split()][:n_sizes]
number_of_clients = int(input())
counts = Counter(lst)

total = 0
for _ in range(number_of_clients):
    size, price = map(int, input().split())
    if size in counts.keys():
        if counts[size]:
            total += price
            counts[size] -= 1

print(total)