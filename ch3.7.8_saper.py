from random import randint, choice

class Cell:
    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine
    
    @is_mine.setter
    def is_mine(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, value):
        if type(value) != int or value > 8 or value < 0:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open
    
    @is_open.setter
    def is_open(self, value):
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.is_open

    def __str__(self):
        o = self.is_open
        m = [self.number, "*"][self.is_mine]
        return f" {['[]',m][o]}"


class GamePole:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, N, M, total_mines):
        """ N строк (i), M столбцов (j)"""
        self.n = N
        self.m = M
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for _ in range(self.m)] for _ in range(self.n)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        for _ in range(self.total_mines):
            choice([cell for row in self.pole for cell in row]).is_mine = True
        
        for i, row in enumerate(self.pole):
            for j, b in enumerate(row):
                if b.is_mine:
                #    print(b, i, j)
                   for k in range(-1, 2):
                        for l in range(-1, 2):
                            ii, jj = i + k, j + l
                            if 0 <= ii < self.n and 0 <= jj < self.m:
                                self.pole[ii][jj].number += 1

    def open_cell(self, i, j):
        if 0 <= i <= self.n and  0 <= j <= self.m: 
            self.pole[i][j].is_open = True

    def show_pole(self):
        for i in range(self.n):
            print(*[self.pole[i][j] for j in range(self.m)])
            print()from random import randint, choice
