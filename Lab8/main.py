import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt
from math import e


def find_distribution(n, perm, pos):

    ans = np.zeros(n)
    for p in perm:
        x = 20000000
        for i in range(0, pos):
            x = min(x, p[i])

        ales = p[-1]
        for i in range(pos, n):
            if p[i] < x:
                ales = p[i]
                break
        ans[ales - 1] += 1
    
    ans /= len(perm)
    return ans



def find_best_distribution(n, to_print = False):
    perm = permutations([i for i in range(1, n + 1)])
    perm = list(perm)

    winner = -1
    maxim = -1 
    max_idx = -1
    probs = []
    for i in range(n):
        dist = find_distribution(n, perm, i)
        print(dist)
        probs.append(dist[0])
        if dist[0] > maxim:
            maxim = dist[0]
            winner = dist
            max_idx = i 

    print(probs)

    return winner, max_idx, probs

n = 5
winner, max_idx, probs = find_best_distribution(n, True)
e = np.exp(1)

print(f"Best Distribution: {winner}")
print(f"Best Probability: {winner[0]}")
print(f"Best Index: {max_idx}")
print(f"Prediction for best K = (N / e): {round(n / e)}" )

plt.bar(np.arange(n), probs, edgecolor="black")
plt.show()