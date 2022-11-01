class Track:
    def __init__(self, *coords):  # start_x, start_y):
        self.start_x, self.start_y = coords
        self.path = []

    def add_point(self, x, y, speed):
        self.path.append([(x, y), speed])

    def __getitem__(self, item):
        indx = self.check(item)
        return self.path[indx][0], self.path[indx][1]

    def __setitem__(self, key, value):
        self.path[key][1] = value

    def check(self, indx):
        if isinstance(indx, int) and 0 <= indx < len(self.path):
            return indx
        else:
            raise IndexError('некорректный индекс')


tr = Track(10, -5.4)
tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3]  # IndexError
