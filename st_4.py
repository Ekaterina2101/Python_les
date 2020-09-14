def my_func(x, y):

    num = 1
    if y >= 0:
        print('Второе число должно быть отрицательным, но я вас прощаю и принимаю, что вы просто забыли минус')
    y = abs(y)

    for i in range(1, y + 1):
        num = num / x

    print(f'{x} в степени -{y} равно: {num}')


try:
    my_func(float(input('Введите положительное число')), int(input('Введите целое отрицательное число')))
except ValueError:
    print('Некорректный ввод. Нужно ввести число')
