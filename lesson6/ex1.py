from itertools import cycle, count
import time


class TrafficLight:

    color = cycle(['Красный', 'Желтый', 'Зеленый'])

    def running(self):
        for i in count():
            print(next(self.color))
            time.sleep(7)
            print(next(self.color))
            time.sleep(2)
            print(next(self.color))
            time.sleep(7)


street = TrafficLight()
print(street.running())
