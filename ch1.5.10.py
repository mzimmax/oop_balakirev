from random import randint


class Cell:
    def __init__(self, mine=False, around_mines=0):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = True  # False


class GamePole:

    def __init__(self, N: int, M: int):
        self.n = N
        self.m = M
        self.pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]

    def init(self):
        mines: int = 0
        while mines < self.m:
            x = randint(0, self.n - 1)
            y = randint(0, self.n - 1)
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                mines += 1

        offset: list = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not all((i, j))]  # (i == 0 and j == 0)]
        #  print(offset)
        for x in range(self.n):
            for y in range(self.n):
                if self.pole[x][y].mine:
                    for i, j in offset:
                        if 0 <= x + i < self.n and 0 <= y + j < self.n:
                            self.pole[x + i][y + j].around_mines += 1

    def show(self):
        for x in range(self.n):
            for y in range(self.n):
                if self.pole[x][y].fl_open:
                    print("*" if self.pole[x][y].mine else self.pole[x][y].around_mines, " ", end="")
                else:
                    print('#', end="")
            print()


pole_game = GamePole(10, 12)
pole_game.init()
pole_game.show()
