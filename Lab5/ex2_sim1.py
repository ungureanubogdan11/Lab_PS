import numpy as np
import matplotlib.pyplot as plt

nr_sim = 10000
balance = 100_000
target = 10 * balance
prizes = [1, 2, 6, 22, 200, 1_000_000]
count = 0
bev = 1
for x in prizes:
    bev = bev * (x ** (1/6)) 
price = bev
print(f"BEV: {bev}")

for i in range(nr_sim):
    balance = 100_000
    while balance >= price and balance < target:
        balance -= price
        balance += prizes[np.random.randint(0, 6)]
    count += (balance >= target)

print(f"probabilitate castig: {count / nr_sim}")