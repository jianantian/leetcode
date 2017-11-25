from matplotlib import pyplot as plt
from math import *


def sigmiod(x):
    return 1./(1 + exp(-x))

x = range(-10, 11, 1)
y = map(sigmiod, x)
fig = plt.figure(1)
plt.plot(x, y)
plt.show()


