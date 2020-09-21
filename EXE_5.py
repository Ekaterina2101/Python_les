with open("text_5.txt", "w", encoding="utf-8") as f_obj:
    new_str = input('Введите числа, разделенные пробелом')
    f_obj.write(new_str)

with open("text_5.txt", "r", encoding="utf-8") as my_obj:
    lis = my_obj.readline().split()
    summa = 0
    try:
        for el in lis:
            summa = summa + float(el)
        print(f'Сумма чисел в файле равна: {summa}')
    except ValueError:
        print('Некорректно введеные данные. Необходимо ввести числа, разделенные пробелом')
