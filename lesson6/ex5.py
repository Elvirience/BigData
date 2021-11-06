class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen("ручкой")
pen.draw()

pencil = Pen("карандашом")
pencil.draw()

handle = Pen("маркером")
handle.draw()
