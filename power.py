# coding:utf8

import datetime as dt

def mul(a, b):

    """这就是普通的乘法计算方法, 假定 a,b 均为 N 位数, 则共需要 N 次循环,
    每次循环中要计算一次按位与运算 O(1), 两次加法 2 * O(N), 一次右移O(1),
    从而总的计算复杂度为 (2*O(1) + 2*O(N))*O(N), 即为 O(N^2)."""

    res = 0
    m = abs(b)
    while m:
        if m & 1 == 1:
            res += a
        a += a
        m >>= 1
    if b >= 0:
        return res
    else:
        return -res


def power(a, m):
    
    """与上面类似, 这事实上也是普通的幂的计算方法, 计算复杂度为 O(N)*(2*O(1)+2*O(N^2)),
    记为 O(N^3)"""

    res = 1
    n = abs(m)
    while n:
        if n & 1 == 1:
            res *= a
        a *= a
        n >>= 1
    if m >= 0:
        return res
    else:
        return 1.0/res
