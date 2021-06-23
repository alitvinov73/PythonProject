# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width, height, density):
        self._length = length
        self._width = width
        self._height = height
        self._density = density

    def calc_mass(self):
        return f'Масса асфальта: {int(self._length) * int(self._width) * int(self._height) * int(self._density)}'


res = Road(10, 5, 25, 5)
print(res.calc_mass())
