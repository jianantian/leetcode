def std(L):
    mean = float(sum(L))/len(L)
    tot = 0.0
    for x in L:
        tot += (x-mean)**2
    return (tot/len(L))**0.5

l = [17, 16, 10, 20, 12]
print std(l)