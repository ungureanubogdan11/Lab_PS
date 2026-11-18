import numpy as np
import matplotlib.pyplot as plt

# input_file = "random_discrete_variable.txt"
x = [1, 2, 3, 4, 5, 7]
p = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

# with open(input_file, "r") as r:
#     line = r.readline()
#     x = map(int, line.split(" "))
#     print(x)
#     line = r.readline()
#     p = map(int, line.split(" "))

num_sim = 10000
rezultate = []

cumsum_p = [0]
for prob in p:
    cumsum_p.append(cumsum_p[-1] + prob)
cumsum_p[-1] = 1.0

print(cumsum_p)
num_sim = 10000


for i in range(num_sim):
    u = np.random.random()
    k = 0
    while u >= cumsum_p[k]:
        k += 1
    rezultate.append(x[k - 1])

valori, apps = np.unique(rezultate, return_counts=True)
total = 0
repartizare = rezultate

plt.hist(repartizare, bins = np.arange(max(x) + 2) - 0.5, cumulative=True, density=True, edgecolor="black")
    
print(repartizare)

plt.show()

