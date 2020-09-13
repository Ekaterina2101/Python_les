def my_func():
    qu = '0'
    summa = 0
    while qu != 'q':
        my_co = input('Введите числа разделенные пробелом, для окончания введите q').split()
        for i in my_co:
            if i.lower() != 'q':
                summa = summa + int(i)
            else:
                qu = 'q'
                break
        print(f' Сумма введенных чисел равна {summa}')


try:
    my_func()
except ValueError:
    print('Необходимо вводить числа')
    my_func()
