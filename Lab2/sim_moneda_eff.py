import numpy as np
import matplotlib.pyplot as plt
import time

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

start_time = time.time()

num_sim = 10000
coins = np.random.random(num_sim)
coins = coins < 0.5
prob_list = np.cumsum(coins) / np.arange(1, num_sim + 1)
prob_list2 = np.cumsum(coins) - (np.arange(1, num_sim + 1) / 2)

prob = coins.sum() / num_sim
prob2 = coins.sum() - (num_sim / 2)

end_time = time.time()
print(end_time - start_time)

print(prob)
print(prob2)

plt.plot(prob_list)
plt.plot(prob_list2)
plt.show()