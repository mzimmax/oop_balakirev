class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __len__(self):
        return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) **
                    2) ** 0.5)
    



line1 = Line(1, 1, 3, 3)
print(len(line1))
line2 = Line(0.1, 0.1, 0.3, 0.3)
print(len(line2))
line2 = Line(0.1, 0.1, 0.3, 0.3)
print(bool(line2))

