import numpy as np
import matplotlib.pyplot as plt

num_sim = 1000


def geometric(p, print = 1):
    
    x = np.random.random(num_sim) >= p
    incercari = np.ones(num_sim, dtype=int)

    while x.any():
        incercari[x] += 1
        x[x] = np.random.random(x.sum()) >= p

    if print:
        plt.hist(incercari.astype(int), bins=incercari.max() + 0.5, density=True, edgecolor="black")
    
    return incercari

print(geometric(2/4))

plt.show()

