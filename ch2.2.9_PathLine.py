class LineTo:
    def __init__(self, x, y):
        self._x = self._y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


class PathLines:
    def __init__(self, *args):
        # self.lines = []
        self.lines = list(args)
        self.x0 = 0
        self.y0 = 0

    def get_path(self):
        """- возвращает список из объектов класса LineTo (если объектов нет, то пустой список);"""
        return self.lines

    def get_length(self):
        """- возвращает суммарную длину пути (сумма длин всех линейных сегментов);
             L = sqrt((x1-x0)^2 + (y1-y0)^2)
        """
        x0, y0 = 0, 0
        lenght = 0
        for line in self.lines:
            lenght += ((line.x - x0) ** 2 + (line.y - y0) ** 2) ** 0.5
            x0, y0 = line.x, line.y
        return lenght

    def add_line(self, line: LineTo):
        """- добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута."""
        self.lines.append(line)


p = PathLines()
print(p.get_length(), p.get_path())
p = PathLines(LineTo(10, 20), LineTo(10, 30))
# print(p.get_path())
p.add_line(LineTo(20, -10))
# print(p.get_path())
dist = p.get_length()
print(dist)