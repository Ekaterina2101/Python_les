class Warehouse:
    def __init__(self):
        self.struct = [{'Printer': 'Цена: 3300, Количество: 2 шт., Свойство- Цветной'},
                       {'Scanner': ' Цена: 2700, Количество: 3 шт., Свойство: Планшетный'},
                       {'Printer': 'Цена: 2700, Количество: 1 шт., Свойство- Монохромный'},
                       {'Xerox': 'Цена: 3200, Количество: 1 шт., Свойство: Вединговый'}]
        self.otk = [{'Printer': 'Цена: 1800, Количество: 1 шт., Свойство- Цветной'},
                    {'Scanner': ' Цена: 2300, Количество: 1 шт., Свойство: Планшетный'}]
        self.secretary = [{'Printer': 'Цена: 1800, Количество: 1 шт., Свойство- Цветной'},
                          {'Xerox': 'Цена: 4000, Количество: 1 шт., Свойство: Портотивный'}]
        self.accounts = [{'Printer': 'Цена: 1800, Количество: 1 шт., Свойство: Монохромный'},
                         {'Scanner': ' Цена: 1950, Количество: 1 шт., Свойство: Планшетный'}]

    def menu(self):

        make = input('Добавить товар-1, посмотреть наличие-2, списать в отдел-3, выйти из программы- иное ')
        if make == '1':
            return Warehouse.add_technic(self)
        if make == '2':
            return Warehouse.show_org(self)
        if make == '3':
            return Warehouse.offs(self)

    def show_org(self):
        init = '2'
        while init == '2':
            show = input('Наличие какого товара вы хотели бы посмотреть: 1-принтер, 2- сканер, 3- ксерокс')
            for i in self.struct:
                if show == '1':
                    if i.get("Printer") is not None:
                        print(f'Принтер {i.get("Printer")}')
                if show == '2':
                    if i.get("Scanner") is not None:
                        print(f'Сканер {i.get("Scanner")}')
                if show == '3':
                    if i.get("Xerox") is not None:
                        print(f'Ксерокс {i.get("Xerox")}')

            org = input('Для просмотра техники числящейся за отделом: 1-ОТК, 2- Секретариат, 3- Бугалтерия ')
            if org == '1':
                print(self.otk)

            if org == '2':
                print(self.secretary)

            if org == '3':
                print(self.accounts)
            init = input('Добавить товар-1, посмотреть наличие-2, списать в отдел-3, выйти из программы- иное ')
            if init == '3':
                return Warehouse.offs(self)
            if init == '1':
                return Warehouse.add_technic(self)

    def add_technic(self):
        init = 1
        while init == 1:

            name = input('Введите название товара: 1- принтер, 2-сканер, 3-ксерокс')
            if name == '1':
                name = 'Printer'
                proper = input('Принтер монохромный-1 , многоцветный-2')
                if proper == '1':
                    proper = 'Монохромный'
                if proper == '2':
                    proper = 'Цветной'
            elif name == '2':
                name = 'Scanner'
                proper = input('Сканер планшетный-1 , листопротяжный-2')
                if proper == '1':
                    proper = 'Планшетный'
                if proper == '2':
                    proper = 'Листопротяжный'
            elif name == '3':
                name = 'Xerox'
                proper = input('Ксерокс портотивный-1, вединговый-2')
                if proper == '1':
                    proper = 'Портотивный'
                if proper == '2':
                    proper = 'Вединговый'

            price = int(input('Введите цену товара'))
            qu = int(input('Введите количество товара'))

            struct1 = {name: f'Цена: {price}, Количество: {qu}, Свойство: {proper}'}
            self.struct.append(struct1)
            init = input('Добавить товар-1, посмотреть наличие-2, списать в отдел-3, выйти из программы- иное ')
            if init == '3':
                return Warehouse.offs(self)
            if init == '2':
                return Warehouse.show_org(self)

    def offs(self):
        init = '3'
        while init == '3':
            product = input("Введите название товара: 1- принтер, 2-сканер, 3-ксерокс")
            if product == '1':
                product = 'Printer'
            if product == '2':
                product = 'Scanner'
            if product == '3':
                product = 'Xerox'

            department = input('В какой отдел списать технику: 1- секритариат, 2- ОТК, 3-Бугалтерия')
            for i in self.struct:
                if i.get(product) is not None:

                    if department == '1':
                        self.secretary.append({product: i.get(product)})
                        self.struct.remove({product: i.get(product)})
                        break

                    if department == '2':
                        self.otk.append({product: i.get(product)})
                        self.struct.remove({product: i.get(product)})
                        break

                    if department == '3':
                        self.accounts.append({product: i.get(product)})
                        self.struct.remove({product: i.get(product)})
                        break

            init = input('Добавить товар-1, посмотреть наличие-2, списать в отдел-3, для выхода- иное ')
            if init == '1':
                return Warehouse.add_technic(self)
            if init == '2':
                return Warehouse.show_org(self)


class OfficeEquipment:

    def __init__(self, prize, qu):
        self.prize = prize
        self.qu = qu


class Printer(OfficeEquipment):

    def __init__(self, prize, qu, multi):
        super().__init__(self, prize, qu)
        self.multi = multi


class Scanner(OfficeEquipment):
    def __init__(self, prize, qu, sort):
        super().__init__(self, prize, qu)
        self.sort = sort


class Xerox(OfficeEquipment):
    def __init__(self, prize, qu, option):
        super().__init__(self, prize, qu)
        self.option = option


Warehouse().menu()
