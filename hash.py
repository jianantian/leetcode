import random


def collision_prob(n, k):
    prob = 1
    for i in range(1, k):
        prob *= (n-i)/float(n)
    return 1-prob

print collision_prob(365, 70)
