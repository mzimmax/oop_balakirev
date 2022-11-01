class PolyLine:
    """
    >>> poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
    >>> poly.add_coord(0, 11)
    >>> poly.remove_coord(0)
    >>> poly.get_coords()
    [(3, 5), (0, 10), (-1, 8), (0, 11)]
    >>> poly.remove_coord(2)
    >>> poly.get_coords()
    [(3, 5), (0, 10), (0, 11)]
    """
    def __init__(self, *coords):
        self.coords: list = list(coords)

    def add_coord(self, x, y):
        """добавление новой координаты (в конец);"""
        point = x, y
        self.coords.append(point)

    def remove_coord(self, indx):
        """удаление координаты по индексу (порядковому номеру, начинается с нуля);"""
        self.coords.pop(indx)

    def get_coords(self):
        """получение списка координат (в виде списка из кортежей)."""
        return self.coords


if __name__ == "__main__":
    import doctest
    doctest.testmod()