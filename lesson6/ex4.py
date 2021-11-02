class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{name} едет')

    def stop(self):
        print(f'{name} остановилась')

    def turn(self, direction):
        print(f'{name} поворачивает на{direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if 40 <= self.speed <= 60:
            print(f'{self.name} движется по городу со скоростью {self.speed}')
        elif self.speed > 60:
            print(f'{self.name} превышает скоростной режим на {self.speed - 60} км/ч')
        else:
            print(f'{self.name} едет слишком медленно')


class SportCar(Car):

    def show_speed(self):
        if 90 < self.speed < 120:
            print('Отличная скорость')
        elif self.speed > 120:
            print('Малыш на драйве')
        elif 60 < self.speed < 90:
            print('Еду на трек')
        else:
            print('Паркуюсь')

    def tunning(self, max_speed):
        if max_speed < 250:
            print('Обратитесь к механику')
        else:
            print(f'У {self.name} Полный порядок')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Сбавьте скорость')
        elif 20 <= self.speed <= 40:
            print('Придерживайтесь данной скорости')
        else:
            print(f'{self.name} паркуется')


class PoliceCar(Car):

    def call_centre(self):
        print('Это полицейский автомобиль. Что у вас случилось?')

    def show_speed(self, police_speed):
        if police_speed > 120 and self.speed > 120:
            print(f'Догоняю нарушителя на {self.name}')
            print(f'Цвет: {self.color}')
            print(f'Скорость: {self.speed}')
        elif police_speed > 120:
            print('Меня угнали')
        elif 90 < police_speed < 120:
            print('Двигаюсь к месту')
        elif 60 < police_speed < 90:
            print('Патрулирую')


print('для TownCar')
car_1 = TownCar(121, "Silver", "Hyunday", False)
print(f'Марка: {car_1.name}')
car_1.show_speed()

print('для SportCar')
car_2 = SportCar(180, "Red", "BMW", False)
print(f'Марка: {car_2.name}')
car_2.tunning(270)

print('для WorkCar')
car_3 = WorkCar(19, "Black", "Mercedes", False)
print(f'Марка: {car_3.name}')
car_3.show_speed()

print('для PoliceCar')
police = PoliceCar(180, "Black", "Audi", False)
police.call_centre()
police.show_speed(140)




