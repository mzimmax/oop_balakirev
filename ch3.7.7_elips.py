class Ellipse:
    def __init__(self, *coords):
        if len(coords) == 4:
            self.fl_good = True
            self.x1, self.y1, self.x2, self.y2 = coords
        else:
            self.fl_good = False

    def get_coords(self):
        if self.fl_good:
            return self.x1, self.y1, self.x2, self.y2
        else:
            raise AttributeError('нет координат для извлечения')

    def __bool__(self):
        return bool(self.fl_good) 


el = Ellipse(1,2,4)
lst_geom = [Ellipse(1,2,3,4), Ellipse(), Ellipse(), Ellipse(1,2,3,5)]
lst = [i.get_coords for i in lst_geom if i]
print(lst_geom)
print(lst)
