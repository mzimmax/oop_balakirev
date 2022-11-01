class Line:

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, *args):
        "- для изменения координат линии;"
        self.__x1, self.__y1, self.__x2, self.__y2 = [i for i in args]

    def get_coords(self):
        "- для получения кортежа из текущих координат линии."
        return [i for i in self.__dict__.values()]

    def draw(self):
        print(*self.get_coords())


line = Line(1, 2, 3, 4)
print(line.get_coords())  # (1, 2, 3, 4)
line.set_coords(5, 6, 7, 8)  # 5 6 7 8
line.draw()
