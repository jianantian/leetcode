from matplotlib import pyplot as plt


def harmonic_average(x, y):
    if x * y != 0:
        return 2 * x * y / float(x + y)


def average(x, y):
    return (x+y)/2.0


def geo_average(x, y):
    return (x * y) ** 0.5


plt.figure(1)
x = range (1, 11)
y_1 = [harmonic_average(i,5) for i in x]
y_2 = [average(i,5) for i in x]
y_3 = [geo_average(i,5) for i in x]
plt.plot(x, y_1, 'blue', label='Harmonic Average')
plt.plot(x, y_2, 'red', label='Average')
plt.plot(x, y_3, 'green', label= 'Geometric Average')
plt.legend(loc = 'upper left')
plt.show()
