class TriangleChecker:
    def __init__(self, a: int, b: int, c: int):
        self.s = [a, b, c]

    def is_triangle(self):
        if min(self.s) <= 0:
            return 1
        if max(self.s) * 2 > sum(self.s):
            return 2
        return 3


a, b, c = map(int, input().split()) # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

