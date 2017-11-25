import random

def flip(num_flips):
    heads = 0.0
    for i in range(num_flips):
        if random.random() < 0.5:
            heads += 1
    return heads/num_flips

def flip_sim(num_per_trial, num_trial):
    frac_heads = []
    for i in range(num_trial):
        frac_heads.append(flip(num_per_trial))
    mean = sum(frac_heads)/len(frac_heads)
    return mean

print flip_sim(100, 1000)
