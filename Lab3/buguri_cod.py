import numpy as np
import matplotlib.pyplot as plt
import time

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

p_b = 3/4
p_bc = 1 - p_b
p_a_b = 1/20
p_a_bc = 98/100

p_b_a = (p_a_b * p_b) / (p_a_b * p_b + p_a_bc * p_bc)
p_bc_a = (p_a_bc * p_bc) / (p_a_bc * p_bc + p_a_b * p_b)
print(f"P(B|A): {p_b_a * 100}%")
print(f"P(Bc|A): {p_bc_a * 100}%")


p_ac_b = 1 - p_a_b
p_ac_bc = 1 - p_a_bc

p_b_ac = (p_ac_b * p_b) / (p_ac_b * p_b + p_ac_bc * p_bc)
p_bc_ac = (p_ac_bc * p_bc) / (p_ac_bc * p_bc + p_ac_b * p_b)
print(f"P(B|Ac): {p_b_ac * 100}%")
print(f"P(Bc|Ac): {p_bc_ac * 100}%")

nr_sim = 100000
are_bug = np.random.random(nr_sim) < p_b
prob_acceptat = np.random.random(nr_sim)
acceptat = np.where(are_bug, prob_acceptat < p_a_b, prob_acceptat < p_a_bc)

count_acceptat = acceptat.sum()
print(f"P(A): {count_acceptat / nr_sim *100}%")
count_acceptat_bug = (are_bug & acceptat).sum()
print(f"P(A intersectat cu B): {count_acceptat_bug / nr_sim *100}%")

plt.plot(acceptat.cumsum() / np.arange(1, nr_sim + 1))
plt.plot((are_bug & acceptat).cumsum() / np.arange(1, nr_sim + 1))

plt.show()
