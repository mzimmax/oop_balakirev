class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        self.__x = x
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, value):
        if self.check_value(value):
            self.__x = value

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, value):
        if self.check_value(value):
            self.__y = value

    @classmethod
    def check_value(cls, value):
        if not isinstance(value, (int, float)):
            return  # raise ValueError("Координата должна быть float или int")
        if cls.MAX_COORD < value or value < cls.MIN_COORD:
            return  # raise ValueError(f"Координата должна быть от {cls.MIN_COORD} до {cls.MAX_COORD}")
        return True

    @staticmethod
    def norm2(vector):
        return vector.x * vector.x + vector.y * vector.y


v1 = RadiusVector2D()        # радиус-вектор с координатами (0; 0)
v2 = RadiusVector2D(1)       # радиус-вектор с координатами (1; 0)
v3 = RadiusVector2D(1, 2)    # радиус-вектор с координатами (1; 2)
v3.x = "12"
v2.y = -230
vectors = [v1, v2, v3]
print(*[RadiusVector2D.norm2(i) for i in vectors])