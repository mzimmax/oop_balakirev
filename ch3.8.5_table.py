class IntegerValue:
    @staticmethod
    def check_value(value):
        return isinstance(value, int)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not self.check_value(value):
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)


class CellInteger:
    value = IntegerValue()

    def __init__(self, value=0):
        self.value = value


class TableValues:
    def __init__(self, rows, cols, cell=CellInteger):  # ...
        if cell is None:
            raise ValueError('параметр cell не указан')
        self.cells = [[cell() for _ in range(cols)] for _ in range(rows)]

    def check_indx(self, indx):
        if isinstance(indx[0], int) and isinstance(indx[1], int) and \
                0 <= indx[0] < len(self.cells) and 0 <= indx[1] < len(self.cells[0]):
            return True

    def __getitem__(self, item):
        if self.check_indx(item):
            return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if self.check_indx(key):
            self.cells[key[0]][key[1]].value = value



table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45  # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()
