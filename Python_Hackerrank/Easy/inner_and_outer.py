#Christian Flores 18/02/2021

import numpy

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

A = numpy.array(A1)
B = numpy.array(A2)

print(numpy.inner(A,B))
print(numpy.outer(A, B))
