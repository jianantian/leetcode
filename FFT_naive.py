import cmath
import numpy as np

PI = cmath.pi


def root_unity(n):
    """
    计算 n 阶本原单位根
    """
    return cmath.exp((-2*PI)/n*1j)


def fft_naive(l, w):
    """
    快速Fourier变换, 计算复杂度为O(N*log(N)), N 为 l 的长度.

    输入值: l 为长度 n=2**k 的列表, w 为 n 次本原单位根.
    返回值: 长度 n 的列表 res.
            res[i] = sum([l[j] * (w**j) for j in range(len(l))]),
            也即是以 l 为系数的的 len(l)-1 次多项式在 w**i 处的取值.
    """

    if abs(w - 1) <= 0.0001:
        return l
    n = len(l)
    le = [l[2*i] for i in range(round(n/2))]
    lo = [l[2*i + 1] for i in range(round(n/2))]
    rese = fft_naive(le, w**2)
    reso = fft_naive(lo, w**2)
    res = np.zeros(n)
    for i in range(round(n/2)):
        res[i] = rese[i] + (w**i) * reso[i]
        res[n/2 + i] = rese[i] - (w**i) * reso[i]
    return res


if __name__ == '__main__':
    input_list = [1, 2, 3, 4]
    unity_root = root_unity(len(input_list))
    r = fft_naive(input_list, unity_root)
    print(r)


# from fractions import Fraction
# res = 0
# for i in range(1, 1001):
#     res += Fraction(1, i)
# print(float(res))
