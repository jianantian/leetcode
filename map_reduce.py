def normliz(l):
    return map(str.capitalize, l)


def prod(l):
    def mul(a, b):
        return a*b
    return reduce(mul, l)


print normliz(['adam', 'LISA', 'barT'])
