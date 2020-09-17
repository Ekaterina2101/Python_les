def fact(m):
    f = 1
    for elem in range(1, m + 1):
        f = f * elem
        yield elem, f


n = int(input('Введите число'))
print(f'{n}! = ', end='')
for el in fact(n):
    if el[0] == n:
        print(f'{n} = {el[1]}')
    else:
        print(el[0], end='*')
