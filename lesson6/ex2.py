class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self, one_layer_mass, layers):
        mass = self.__length * self.__width * one_layer_mass * layers
        return mass


asphalt = Road(20, 200000)
print(f'Масса асфальта: {asphalt.mass(25, 20) / 1000} тонн')
