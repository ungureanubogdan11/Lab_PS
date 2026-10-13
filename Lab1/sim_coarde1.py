import numpy as np
import matplotlib.pyplot as plt

test_cases = 10000

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

probabilities = []
count = 0

for i in range(test_cases):
    theta1 = np.random.random() * np.pi * 2
    theta2 = np.random.random() * np.pi * 2

    x1 = np.cos(theta1)
    x2 = np.cos(theta2)
    y1 = np.sin(theta1) 
    y2 = np.sin(theta2)

    L = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    current_prob = count / (i + 1)
    probabilities.append(current_prob)
    if L > np.sqrt(3):
        count += 1


plt.plot(probabilities)

plt.show()