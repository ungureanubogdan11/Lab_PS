import numpy as np
import matplotlib.pyplot as plt

num_corzi = 10000
count = 0

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

probabilities = []

for i in range(num_corzi):
    raza = np.random.random()
    theta = np.random.random() * np.pi * 2

    x1 = np.cos(theta - np.arccos(raza))
    y1 = np.sin(theta - np.arccos(raza))

    x2 = np.cos(theta + np.arccos(raza))
    y2 = np.sin(theta + np.arccos(raza))

    L = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    current_prob = count / (i + 1)
    probabilities.append(current_prob)
    if L > np.sqrt(3):
        count += 1



print(count / num_corzi)
print(len(probabilities))

plt.plot(probabilities)

plt.show()