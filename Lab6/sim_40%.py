import numpy as np
import matplotlib.pyplot as plt
from math import log

nr_sim = 10000
nr_aruncari = 300

wins = []
win_sum = 0
count_losses = 0

for i in range(nr_sim):
    sum = 1
    for j in range(nr_aruncari):
        x = np.random.random()
        if x < (1/6):
            sum += 0.4 * sum / 2
        elif x >= (1/6) and x < (5/6):
            sum += 0.4 * sum / 20
        else:
            sum -= 0.4 * sum / 2
    wins.append(sum)
    win_sum += sum
    count_losses += sum < 1

print(f"{win_sum / len(wins):.2f}")
print(count_losses)

log_wins = list(map(log, wins))
plt.plot(log_wins, [i for i in range(len(wins))])
plt.show()
