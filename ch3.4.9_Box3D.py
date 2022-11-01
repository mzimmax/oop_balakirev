class Box3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other):
        if type(other) == Box3D:
            return Box3D(self.width + other.width,
                          self.height + other.height,
                          self.depth + other.depth)
        else:
            return Box3D(self.width + other,
                          self.height + other,
                          self.depth + other)

    def __mul__(self, other):
        return Box3D(self.width * other,
                     self.height * other,
                     self.depth * other)

    def __rmul__(self, other):
        return Box3D(self.width * other,
                     self.height * other,
                     self.depth * other)

    def __sub__(self, other):
        return Box3D(self.width - other.width,
                     self.height - other.height,
                     self.depth - other.depth)

    def __floordiv__(self, other):
        return Box3D(self.width // other,
                     self.height // other,
                     self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other,
                     self.height % other,
                     self.depth % other)


def test_mod():
    box1 = Box3D(53, 7, 28)
    constant = 12
    res1 = box1 % constant

    assert type(res1) is Box3D
    assert res1.width == box1.width % constant
    assert res1.height == box1.height % constant
    assert res1.depth == box1.depth % constant

test_mod()