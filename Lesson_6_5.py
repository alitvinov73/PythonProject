class Stationery:
    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(self.title)


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с использованием  {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с использованием  {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки с использованием  {self.title}")

picture = Stationery()
picture.draw()
picture = Pen("Ручка")
picture.draw()
picture = Pencil("Карандаш")
picture.draw()
picture = Handle("Маркер")
picture.draw()