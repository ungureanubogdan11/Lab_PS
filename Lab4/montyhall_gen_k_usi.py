import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

nr_sim = 10000

nr_usi = 4
nr_usi_deschise = 1

premiu = np.random.randint(0, nr_usi, size = nr_sim)

alegere_initiala = np.zeros(nr_sim)
nu_schimb = (premiu == alegere_initiala)

schimb = (~nu_schimb) & (np.random.randint(0, nr_usi - nr_usi_deschise - 1, size = nr_sim) == 0)

print(f"Daca avem {nr_usi} usi, se deschid {nr_usi_deschise} usi:\n daca nu schimbam usa: {(nu_schimb.sum() / nr_sim)}\n daca schimb usa: {schimb.sum() / nr_sim}") 

probabilities = (premiu.cumsum() / np.arange(1, nr_sim + 1))
plt.plot(probabilities)
# plt.show()