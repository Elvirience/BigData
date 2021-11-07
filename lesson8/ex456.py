class OfficeEquipment:

    """
    Атрибуты, используемые в методах "warehouse", "transportation"
    """
    my_dict = {}
    names = []
    quantities = []
    prices = []

    """
    По сценарию объект класса находится в оффисе, но может быть взят со склада.
    В коде программы я заполнил склад и забрал оттуда нужные товары,
     попутно выполнив небольшие методы классов-наследников
    """
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        print('Атрибут поступил в оффис')

    def needs(self, staff):
        if self.quantity < staff:
            spend = self.price * (staff - self.quantity)
            print(f'Необходимо закупить {self.name} на сумму {spend} руб')
        else:
            print('Закупки не требуются')

    """
    Метод для 6-го номера
    Он проверяет вводимость числа
    Использовал его в методе "warehouse", контролируя данные, вводимые в реестр склада
    """
    @staticmethod
    def validator(parametr):
        if type(parametr) is str:
            while parametr.isdigit() is False:
                parametr = input('Введите число!')
                return int(parametr)
        else:
            return int(parametr)

    """
    Проверяю являются ли количесвто и цена, введенные пользователем, числами
    если нет, предлагаю повторить ввод
    Если на складе уже есть товар с таким названием, то список с названиями остается прежним,
    а количество обновляется (определяется индекс введенного названия товара в списке, где оно уже есть
    и по этому индексу в списке с количествами соответствующих товаров выбирается нужное нам и складывается
    с введенным)
    Далее формируется словарь (реестр склада)
    """
    @classmethod
    def warehouse(cls, name, quantity, price):
        cls.validator(quantity)
        cls.validator(price)
        if cls.names.count(name) >= 1:
            index = cls.names.index(name)
            value = cls.quantities[index]
            cls.quantities[index] = value + quantity
        else:
            cls.names.append(name)
            cls.quantities.append(quantity)
            cls.prices.append(price)
        cls.my_dict = {'Наименование': cls.names, 'Цена': cls.prices, 'Количество': cls.quantities}
        print(f"Атрибут '{name}' вписан в реестр склада")
        return cls.my_dict

    """
    После пополнения склада методом "warehouse" появляется словарь (реестр) my_dict
    Его значения - списки с данными (названия, количество, цена)
    В методе "transportation" извлекается ключ-список по соответсвующему значению
     затем проверяется, если на складе товар "name".
    Если есть, то определяется индекс его названия в списке
     и по этому индексу берется соотвествующее нужному товару количество.
    Из количества товара на складе вычитается необходимое,
     если разность при этом останется больше нуля.
    Полученная разность становится в словаре "my_dict" на место прежнего значения количества,
    что сопровождается соответствующим сообщением
    """
    @classmethod
    def transportation(cls, name, quantity):
        lst = cls.my_dict.get('Наименование')
        if lst.count(name) == 0:
            print(f"Атрибут '{name}' отсутсвтует на складе")
        else:
            index = lst.index(name)
            cls.quantities[index] = cls.my_dict.get('Количество')[index] - quantity
            if cls.quantities[index] > 0:
                cls.my_dict = {'Наименование': cls.names, 'Цена': cls.prices, 'Количество': cls.quantities}
                print(f"{quantity} атрибутов '{name}' взято со склада ")
                print('Реестр склада обновлен')
                return cls.my_dict
            else:
                print(f"Атрибут {name} закончился")

    def __del__(self):
        pass


class PC(OfficeEquipment):
    def __init__(self, name, quantity, price, os):
        super().__init__(name, quantity, price)
        self.os = os

    @classmethod
    def os_choice(cls):
        cls.os = input('Введите название ОС: ')
        print('Вы перешли на новую операционную систему')
        return cls.os


class Printer(OfficeEquipment):
    def __init__(self, name, quantity, price, paper):
        super().__init__(name, quantity, price)
        self.paper = paper

    def condition(self):
        if self.paper is False:
            print('Нужна бумага')
        else:
            pass


class Cartridge(OfficeEquipment):
    @property
    def condition(self):
        if self.quantity < 20:
            print('Нужно больше картриджей')
        else:
            pass


a = OfficeEquipment.warehouse('PC', 325, 526436)
b = OfficeEquipment.warehouse('Принтер', 214, 5264)
c = OfficeEquipment.warehouse('PC', 325, 526436)
print(OfficeEquipment.my_dict)
d = OfficeEquipment.transportation('PC', 20)
e = PC('laptop', 2134, 200000, 'windows')
e = PC.os_choice()
e = PC.warehouse('laptop', 2134, 200000)
e = PC.transportation('laptop', 1)
