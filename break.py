import random
def max_power2(num):
    r = 0
    if num%2 == 0:
        r = 1 + max_power2(num/2)
    return r


def modexp(x, a, n):
    if a == 0:
        return 1
    y = modexp(x, a/2, n)
    if a % 2 == 0:
        return (y*y) % n
    else:
        return (x*y*y) % n


def fermat(nu):
    # r = max_power2(nu-1)
    # u = nu/(2**r)
    k = 0
    for i in range(10):
        a = random.randint(1, nu - 1)
        if modexp(a, nu - 1, nu) != 1:
            print a
            print modexp(a, nu - 1, nu)
            k += 1
            break
    return k


print fermat(27)
