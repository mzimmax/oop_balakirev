class Integer:
    def __init__(self, start_value=0) -> None:
        self.__value: int = start_value

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, val: int) -> None:
        if not (isinstance(val, int)):
            raise ValueError('должно быть целое число')
        self.__value = val

    def __repr__(self):
        return f"{self.value}"


class Float:
    def __init__(self, start_value=0.0) -> None:
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        if not (isinstance(val, (int, float))):
            raise ValueError('должно быть вещественное число')
        self.__value = val / 1.0


class Array:
    def __init__(self, max_length: int, cell):
        self.items = [cell() for _ in range(max_length)]

    def check_indx(self, indx: int):
        if not (isinstance(indx, int) and 0 <= indx < len(self.items)):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __getitem__(self, item: int):
        self.check_indx(item)
        return self.items[item].value

    def __setitem__(self, key: int, val):
        self.check_indx(key)
        self.items[key].value = val

    def __repr__(self):
        text = [str(i.value) for i in self.items]
        return " ".join(text)


# cell = Integer()
ar_int = Array(10, cell=Integer)
print(ar_int[0])
ar_int[3] = 20
print(ar_int[3])
print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
ar_int[1] = 10
print(ar_int)

ar_int[1] = 10.5 # должно генерироваться исключение ValueError
ar_int[10] = 1 # должно генерироваться исключение IndexError
