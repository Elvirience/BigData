from abc import ABC, abstractmethod


class Clothe(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class TheCoat(Clothe):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V

    @property
    def tissue_consumption(self):
        return self.V / 6.5 + 0.5


class TheCostume(Clothe):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H

    @property
    def tissue_consumption(self):
        return 2 * self.H + 0.3


clothe_1 = TheCoat("Пальто", 50)
clothe_2 = TheCostume("Костюм", 50)

print(f'Расход ткани на пальто: {clothe_1.tissue_consumption}')
print(f'Расход ткани на костюм: {clothe_2.tissue_consumption}')
print(f'Общий расход ткани: {clothe_1 + clothe_2}')
