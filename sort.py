# coding:utf8
from datetime import datetime
import random


def insert_sort(l):
    """插入排序"""

    for i in range(1, len(l)):
        temp = l[i]
        j = i
        # 下面的循环用来插入 temp = l[i]
        while j > 0 and temp < l[j - 1]:
            l[j] = l[j - 1]
            # 因为要插入的值 temp 比它之前的最大元 l[j-1] 小,
            # 需要把 temp 插到更前面去, 从而排在 temp 后的元都要向后移一位
            j -= 1
        l[j] = temp
    return l


def select_sort(l):
    """选择排序"""
    for i in range(len(l) - 1):
        k = i
        for j in range(i + 1, len(l)):
            if l[j] < l[k]:
                k = j
        if i != k:
            l[i], l[k] = l[k], l[i]
    return l


def pop_sort(l):
    """冒泡法排序"""
    for i in range(len(l)):
        for j in range(1, len(l) - i):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
    return l


def merge_sort(l):
    """归并排序"""

    def merge(l_1, l_2):
        """定义归并函数"""
        l = []
        i, j = 0, 0
        while i < len(l_1) and j < len(l_2):
            if l_1[i] < l_2[j]:
                l.append(l_1[i])
                i += 1
            else:
                l.append(l_2[j])
                j += 1
        while i < len(l_1):
            l.append(l_1[i])
            i += 1
        while j < len(l_2):
            l.append(l_2[j])
            j += 1
        return l

    n = len(l)
    if n == 1:
        return l
    return merge(merge_sort(l[:n / 2]), merge_sort(l[n / 2:]))
    # res = [[x] for x in l]
    # while len(res) > 1:
    #     res.append(merge(res.pop(0), res.pop(0)))
    # return res.pop(0)


def quick_sort(l):
    """快速排序"""

    def q_sort_rec(l, lo, hi):

        if lo >= hi:
            return
        ran = random.randint(lo, hi)
        l[lo], l[ran] = l[ran], l[lo]
        m = l[lo]
        i = lo + 1
        j = hi
        while True:
            while l[j] > m:
                if j == lo:
                    break
                j -= 1

            while l[i] < m:
                if i == hi:
                    break
                i += 1

            if i >= j:
                break
            l[i], l[j] = l[j], l[i]
            j -= 1
            i += 1
        l[j], l[lo] = l[lo], l[j]
        q_sort_rec(l, lo, j - 1)
        q_sort_rec(l, j + 1, hi)

    q_sort_rec(l, 0, len(l) - 1)
    return l


def sort_time(alg, l):
    start = datetime.now()
    if alg == 'insert':
        insert_sort(l)
    elif alg == 'select':
        select_sort(l)
    elif alg == 'pop':
        pop_sort(l)
    elif alg == 'merge':
        merge_sort(l)
    elif alg == 'quick':
        quick_sort(l)
    elif alg == 'tim':
        sorted(l)
    return (datetime.now() - start).total_seconds()


def random_list(n, t):
    test = []
    for i in range(t):
        l = []
        for j in range(n):
            l.append(random.uniform(0, 1))
        test.append(l)
    return test


def order_test(n=1000, t=100):
    algs = ['insert', 'select', 'pop', 'merge', 'quick', 'tim']
    for alg in algs:
        time = 0
        for i in range(t):
            test = range(n)
            time += sort_time(alg, test)
        print 'Time for ' + alg + ' is: ' + str(time)


def random_test(n=1000, t=100):
    algs = ['insert', 'select', 'pop', 'merge', 'quick', 'tim']
    for alg in algs:
        time = 0
        # start = datetime.now()
        test = random_list(n, t)
        for l in test:
            time += sort_time(alg, l)
        print 'Time for ' + alg + ' is: ' + str(time)


def reverse_test(n=1000, t=100):
    algs = ['insert', 'select', 'pop', 'merge', 'quick', 'tim']
    for alg in algs:
        time = 0
        for i in range(t):
            test = range(n, 0, -1)
            time += sort_time(alg, test)
        print 'Time for ' + alg + ' is: ' + str(time)


print 'order case is following:'
order_test()
print '\n reverse case is following:'
reverse_test()
print '\n random case is following:'
random_test()
# s = datetime.now()
# for i in range(100):
#     insert_sort(range(1000,0,-1))
# print (datetime.now() - s).total_seconds()
