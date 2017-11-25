def triangles(n):
    l = []
    for i in range(n):
        if len(l) >= 2:
            m = l[:]
            for j in range(1, len(l)):
                l[j] = m[j-1] + m[j]
        l.append(1)
        yield l

