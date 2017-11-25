# fr = open('A-large.in', 'r')
# li = fr.readlines()
# n = int(li[0])
# s_list = li[1:]


def revert(s, k):
    s_v = ''
    for x in s[:k]:
        if x == '+':
            x = '-'
        else:
            x = '+'
        s_v += x
    return s[k:] + s_v


def check(s):
    num = 0
    for x in s:
        if x == '-':
            num += 1
    return num

s = '--+-'
m = len(s)
# for i in range(n):
#     s = s_list[i]
#     m =len(s)
#     l = []

times = 0
while check(s):
    for k in range(1, m + 1):
        s = revert(s, k)
        times += 1
print s
print times

