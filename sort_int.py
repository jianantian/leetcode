#coding:utf8

def sort_int(l):

    """对整数序列排序, 可以有如下的复杂度为 O(N + M) 的算法. N为序列的长度,
    M为序列最大值与最小值的差"""

    mi, ma = min(l), max(l)

    q = []
    for i in range(len(l)):
        q.append(l[i] - mi)

    que = [[] for i in range(ma - mi + 1)]
    for j in range(len(q)):
        que[q[j]].append(l[j])

    res = []
    for x in que:
        res.extend(x)
    return res


l = [10,2,5,3,-7,13,1,5,6]
print sort_int(l)