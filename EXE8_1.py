class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def my_method_1(cls, data):
        param = data.split("-")
        num = int(param[0])
        month = int(param[1])
        year = int(param[2])
        return cls.my_method_2(num, month, year)

    @staticmethod
    def my_method_2(par_1, par_2, par_3):
        if par_1 < 1 or par_1 > 31:
            print(' Вы ввели неправильно дату.')
        elif par_2 < 1 or par_2 > 12:
            print(' Вы ввели неправильно месяц.')
        elif par_3 < 1 or par_3 > 9999:
            print(' Вы ввели неправильно год.')
        else:
            print(f'Введенная дата: {par_1} : {par_2} : {par_3}')


Data.my_method_1(input('Введите дату в формате: "день-месяц-год" '))
