import numpy as np
import matplotlib.pyplot as plt
import time

plt.figure(figsize=(6, 6))
plt.gca().set_facecolor('white')

start_time = time.time()

count = 0
tests = 100000
probabilities = []
diff = []

for i in range(tests):
    number = np.random.random()
    count += (number < 0.5)
    probabilities.append(count / (i + 1))
    diff.append(count - (i + 1) / 2)

end_time = time.time()

print(count / tests)
print(count - (tests / 2))

print(end_time - start_time)

plt.plot(probabilities)
plt.plot(diff)
plt.show()