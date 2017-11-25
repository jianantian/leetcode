import datetime as dt


def fib(n):
    a, b = 0, 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            a, b = b, a+b
        return b


start = dt.datetime.now()
print fib(4)
print dt.datetime.now() - start
