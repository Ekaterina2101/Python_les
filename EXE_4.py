with open("text_4.txt", "r", encoding="utf-8") as f_obj:
    with open("text_new.txt", "w", encoding="utf-8") as new_obj:
        for line in f_obj:
            new_line = line.split(' ')
            trans = {'one': 'Один', 'two': 'Два', 'three': 'Три', 'four': 'Четыре', 'five': 'Пять', 'fix': 'Шесть',
                     'seven': 'Семь', 'eight': 'Восемь', 'nine': 'Девять', 'ten': 'Десять'}
            new_line[0] = trans.get(new_line[0].lower())
            new_obj.write(f'{" ".join(new_line)}')
