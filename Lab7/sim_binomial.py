import numpy as np
import matplotlib.pyplot as plt

num_sim = 100000

def bernoulli(p, print = 1):
    x = np.random.random(num_sim) < p
    if print:
        plt.hist(x.astype(int), bins=[-0.5, 0.5, 1.5], density=True, edgecolor="black")
        plt.xticks([0,1])

    return x.astype(int)


def binomial(n, p, print = 1):
    # x = [bernoulli(p, 0) for _ in range(n)]
    x = np.random.random((n, num_sim)) < p 
    sums = np.sum(x, axis = 0)

    if print:
        plt.hist(sums.astype(int), bins=np.arange(n + 2) - 0.5, density=True, edgecolor="black")
        plt.xticks(np.arange(n + 1))
    
    return sums

print(binomial(10, 1/2))

plt.show()

