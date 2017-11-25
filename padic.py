# todo: 可以定义padic类, 把p进制数的相关内容封装起来


def padic(p, n):
    """把十进制数n转换为p进制"""
    s = ''
    while n:
        s = str(n % p) + s
        n /= p
    return s


def padic_digits(p, n):
    """计算十进制数n转换为p进制后的位数"""
    return len(padic(p, n))


def padic_sum(p, n):
    """计算十进制数n转换为p进制后各个位数的和"""
    res = 0
    for i in padic(p, n):
        res += int(i)
    return res


def times_in_factorial(p, n):
    """计算n!中素因子p出现的次数"""
    return (n - padic_sum(p, n))/(p-1)


print(int('1001010001000001', base=4))
