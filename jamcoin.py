import random


def create(n):
    l = []
    ma = 2**(n-2) - 1
    x = random.randint(0, ma)
    s = str(bin(x))
    re = n - len(s)
    return '1' + '0' * re + s[2:] + '1'


def tran(s):
    l = [int(x) for x in s]
    return l


def su(s):
    return reduce(lambda x, y: x+y, tran(s))


def num(s, p):
    return int(s, base=p)


def max_power2(num):
    r = 0
    if num%2 == 0:
        r = 1 + max_power2(num/2)
    return r


def modexp(x,a,n):
    if a == 0:
        return 1
    y = modexp(x, a/2, n)
    if a % 2 == 0:
        return (y*y)%n
    else:
        return (x*y*y)%n


def fermat(nu):
    # r = max_power2(nu-1)
    # u = nu/(2**r)
    k = 0
    for i in range(10):
        a = random.randint(1, nu - 1)
        if modexp(a, nu -1, nu) != 1:
            k += 1
            break
    return k


def check0(nu, f_l):
    res = 0
    if len(f_l) != 0:
        m = int(nu ** 0.5) + 1
        x = f_l[0]
        print 'x = ' + str(x)
        if nu % x:
            f_l2 = [y for y in f_l if y%x != 0]
            f_l = f_l2
            res += check0(nu, f_l)
        else:
            res = x
        return res

def check(s, p):
    l = tran(s)
    res = num(s, p)
    m = int(res ** 0.5) + 1
    f_l = range(2, m)
    result = check0(res, f_l)
    return result


# l = tran('100011')
# print check(l, 2)

filename = 'C-small-attempt1.in'
fr = open(filename, 'r')
li = fr.readlines()
t = int(li[0])
print t
nj_list = li[1:]
l = []
for i in range(t):
    l.append([])
    pair = nj_list[i].rstrip().split(' ')
    n = int(pair[0])
    j = int(pair[1])
    print 'n = ' + str(n)
    print 'j = ' + str(j)
    it = 0
    while it < j:
        item = create(n)
        print 'item = ' + item
        fac_list = []
        for p in range(2, 11):
            print 'p = ' + str(p)
            print 'num = ' + str(num(item, p))
            if fermat(num(item, p)) == 0:
                print 'going to break'
                break
            elif (su(item)*p) % 2 != 0:
                res = 2
            else:
                print 'bingo'
                res = check(item, p)
            fac_list.append(res)
        if 0 not in fac_list:
            l[i].append([item] + fac_list)
            print it
            it += 1

out = open('c_small_out.out', 'w')
for ci in range(t):
    out.write('Case #' + str(ci+1) + ':\n')
    for si in range(len(l[ci])):
        for ni in range(len(l[ci][si])):
            out.write(str(l[ci][si][ni]) + ' ')
    out.write('\n')
out.close()








