def my_fun(var_1, var_2):
    try:
        div = var_1 / var_2
        print(f' Деление {var_1} на {var_2} равно: {round(div, 4)}')
    except ZeroDivisionError:
        print('Деление на ноль')


try:
    my_fun(int(input('Введите делимое')), int(input('Введите делитель')))
except ValueError:
    print(' Ошибка ввода данных. Введите число ')
