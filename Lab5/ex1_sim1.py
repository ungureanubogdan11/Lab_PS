import numpy as np
import matplotlib.pyplot as plt

# simulare fara faliment

balance = 100
target = 10 * balance
cost_per_game = 70
p = 1 / 6
max_prize = -1

while balance < target:
    balance -= cost_per_game
    prize = 1
    while np.random.random() > p:
        prize *= 2
    balance += prize
    max_prize = max(max_prize, prize)
    print(balance)

print(f"Max prize won in a game: {max_prize}")
