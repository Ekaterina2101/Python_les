def my_func(var_1, var_2, var_3):
    print(f'Сумма наибольших двух аргументов равна {sum([var_1, var_2, var_3]) - min(var_1, var_2, var_3)}')


my_func(int(input('Введите первое число')), int(input('Введите второе число')), int(input('Введите третье число')))
