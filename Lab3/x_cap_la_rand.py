import numpy as np
import matplotlib.pyplot as plt

n = 20
nr_sim = 10000

siruri = [np.random.random(n) for _ in range(nr_sim)]
siruri = [np.where(siruri[i] < 1/2, "cap", "pajura") for i in range(nr_sim)]
print(siruri[1])
print(siruri[2])

prob_list_3 = []
prob_list_4 = []
count_3 = 0
count_4 = 0
for i in range(nr_sim):
    gasit3 = False
    gasit4 = False
    for j in range(n - 3):
        if siruri[i][j] == siruri[i][j + 1] and siruri[i][j + 1] == siruri[i][j + 2] and siruri[i][j] == "cap":
            gasit3 = True
            if siruri[i][j] == siruri[i][j + 3]:
                gasit4 = True

    count_3 += gasit3
    count_4 += gasit4
    prob_list_3.append(count_3 / (i + 1))
    prob_list_4.append(count_4 / (i + 1))



print(f"P 3 cap la rand in {n} aruncari (empiric): {count_3 / nr_sim * 100}%")
print(f"P 4 cap la rand in {n} aruncari (empiric): {count_4 / nr_sim * 100}%")

plt.plot(prob_list_3)
plt.plot(prob_list_4)
plt.show()