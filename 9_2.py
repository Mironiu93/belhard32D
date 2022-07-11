from math import *
lst = [[-3, 0, -5, 0, 2], [0, 5, 0, 3, 0], [-2, 0, -5, 0, 5], [0, -3, 0, 3, 0], [-1, 0, 1, 0, -1]]
count = 0
for i in range(0, len(lst) + 1, 2):
    i = lst[i]
    for j in range(0, len(i), 2):
        j = i[j]
        if j < 0:
            count += abs(j)
for i in range(1, len(lst), 2):
    i = lst[i]
    for j in range(1, len(i), 2):
        j = i[j]
        if j < 0:
            count += abs(j)
print(count)