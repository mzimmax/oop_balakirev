from random import choice, randint

class Shape:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = a, b
        self.ep = c, d


class Line(Shape):
    pass


class Rect(Shape):
    pass


class Ellipse(Shape):
    pass


def g4rc():
    # get list of 4 random numbers in 0 to 100
    list4 = [randint(0, 100) for i in range(4)]
    return list4


a = Line, Rect, Ellipse
elements = [choice(a)(*g4rc()) for i in range(217)]

for i in elements:
    if isinstance(i, Line):
        i.ep = 0, 0
        i.sp = 0, 0

