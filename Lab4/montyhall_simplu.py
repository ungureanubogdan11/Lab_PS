import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

nr_sim = 10000

premiu = np.random.random(nr_sim)
premiu = np.where(premiu < (1 / 3), 1, premiu)
premiu = np.where(premiu < (2 / 3), 2, premiu)
premiu = np.where(premiu < 1, 3, premiu)

# alegem usa 1

premiu = np.where(premiu == 1, 0, 1)
probabilities = premiu.cumsum() / np.arange(1, nr_sim + 1)

count = premiu.sum()

print(f"Probabilitatea de castig daca schimbam usa: {count / nr_sim}")

plt.plot(probabilities)
plt.show()

