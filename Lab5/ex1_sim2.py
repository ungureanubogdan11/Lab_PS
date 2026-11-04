import numpy as np
import matplotlib.pyplot as plt

# simulare cu faliment

nr_sim = 10000
balance = 100
target = 1000 * balance
cost_per_game = 50
p = 1 / 6
count = 0
probabilities = []

for i in range(nr_sim):
    balance = 100
    while balance >= cost_per_game and balance < target:
        balance -= cost_per_game
        prize = 1
        while np.random.random() > p:
            prize *= 2
        balance += prize
    
    if balance >= target:
        count += 1
    probabilities.append(count / (i + 1))

print(f"Probabilitatea de castig (10 * suma initiala) : {count / nr_sim}")

plt.plot(probabilities)
plt.show()
    
    

