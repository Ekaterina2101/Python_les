with open("text.txt", "r", encoding="utf-8") as f_obj:
    i = 0
    for line in f_obj:
        n = 0
        for el in line:
            if el == ' ':
                n = n + 1
        if n > 0:
            n = n+1
        i = i + 1
        print(f'Количество слов в {i} строке равно: {n}')
    print(f'Количество строк в файле {f_obj.name} равно:{i}')
