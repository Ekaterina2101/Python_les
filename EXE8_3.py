class OwnError(Exception):

    def __init__(self, tex):
        self.text = tex


a = 'Начало'
my_list = []
while True:
    try:
        a = input('Введите число, для завершения введите # :')
        if a == '#':
            break
        for i in a:
            if ord(i) < 48 or ord(i) > 57:

                raise OwnError('Ввести нужно число!')

        my_list.append(int(a))

    except OwnError as err:
        print(err)

print(my_list)
