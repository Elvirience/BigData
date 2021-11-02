from itertools import cycle
import time


class TrafficLight:

    _color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for i in cycle(self._color):
            print(self._color[0])
            time.sleep(7)
            print(self._color[1])
            time.sleep(2)
            print(self._color[2])
            time.sleep(7)


street = TrafficLight()
print(street.running())
