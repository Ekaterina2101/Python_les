def int_func(var):
    for i in var:
        if ord(i) < 97 or ord(i) > 122:
            return print('Слово должно быть из маленьких латинских букв')

    return var.title()


str_my = []
arr = input('Введите строку слов из латинских букв в нижнем регистре, разделенных пробелом').split()
try:
    for j in arr:
        str_my.append(int_func(j))
    print(' '.join(str_my))

except TypeError:
    print('Ошибка ввода')
