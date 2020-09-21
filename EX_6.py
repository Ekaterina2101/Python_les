
from itertools import cycle, count

n = 0

for el in cycle("ПРИВЕТСТВУЮ"):
    if n > 15:
        break
    print(el)
    n += 1


for el in count(5):
    if el > 15:
        break
    else:
        print(el)
