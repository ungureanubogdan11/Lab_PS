import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))

num_sim = 10000
R = 2 + 3 * (np.random.random(num_sim) < 0.5)
V = 1 + 3 * (np.random.random(num_sim) > (1/6))
N = 3 + 3 * (np.random.random(num_sim) > (5/6))

print("rosu: 2 2 2 5 5 5")
print("verde: 3 3 3 3 3 6")
print("negru: 1 4 4 4 4 4")
print()

negru_verde = (N > V)
rosu_negru = (R > N) 
verde_rosu = (V > R) 

# plt.plot(negru_verde / np.arange(1, num_sim + 1))
# plt.plot(rosu_negru / np.arange(1, num_sim + 1))
# plt.plot(verde_rosu / np.arange(1, num_sim + 1))

# plt.show()

print("negru verde: ")
print(negru_verde.sum() / num_sim)
print("rosu negru: ")
print(rosu_negru.sum() / num_sim)
print("verde rosu:")
print(verde_rosu.sum() / num_sim)


castiga_rosu = ((R > V) & (R > N)).sum() / num_sim
castiga_negru = ((N > R) & (N > V)).sum() / num_sim
castiga_verde = ((V > R) & (V > N)).sum() / num_sim

print()
print("rosu vs negru vs verde")
print(f"castiga rosu: {castiga_rosu}")
print(f"castiga negru: {castiga_negru}")
print(f"castiga verde: {castiga_verde}")

