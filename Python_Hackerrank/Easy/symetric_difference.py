#Christian Flores
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
set_M = set(list(map(int, input().split()))[:M])
N = int(input())
set_N = set(list(map(int, input().split()))[:N])

set_differences = set(set_M.difference(set_N))
set_differences.update(set_N.difference(set_M))
[print(element) for element in sorted(list(set_differences))]
