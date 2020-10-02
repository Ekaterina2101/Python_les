class OwnError(Exception):
    def __init__(self, tex):
        self.text = tex


a = input('Введите делимое:')
b = input('Введите делитель')
try:
    if int(b) == 0:
        raise OwnError('Делитель не должен быть равен нулю!')
    else:
        rez = int(a) / int(b)
except ValueError:
    print('Вы ввели не число!')
except OwnError as err:
    print(err)
else:
    print(f'{a}/{b} = {rez}')
finally:
    print('Программа завершена!')
