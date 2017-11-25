import math


def sum_fac(n):
    res = 1
    for i in range(n, 0, -1):
        res += 1/math.factorial(i)
    return res

print sum_fac(3)/math.e

