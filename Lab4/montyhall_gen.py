import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

nr_sim = 10000
nr_usi = 10

premiu = np.random.random(nr_sim)
premiu = np.round(premiu * 1000000) % nr_usi + 1

# alegem usa 1

premiu = np.where(premiu == 1, 0, 1)
count = premiu.sum()
probabilities = premiu.cumsum() / np.arange(1, nr_sim + 1)

print(f"Probabilitatea de castig daca avem {nr_usi} usi si schimbam usa: {count / nr_sim}") 

plt.plot(probabilities)
plt.show()