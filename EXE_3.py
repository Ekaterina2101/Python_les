with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    print('Сотрудники, имеющие оклад менее 20000:')
    midl = 0
    n = 0
    for line in f_obj:
        new_line = line.split(' ')
        if float(new_line[1]) < 20000:
            print(new_line[0])
        midl = midl + float(new_line[1])
        n = n + 1
    print(f'Средний оклад сотрудниковв равен: {midl / n}')
