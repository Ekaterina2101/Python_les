from random import randint
source_list = [el * randint(1, 20) for el in range(1, 15)]
print(source_list)
i = 0
new_list = [el for prev_el, el in zip(source_list, source_list[1:]) if el > prev_el]
print(new_list)
