class Point:
    def __init__(self, x: int, y: int, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i, i) if i != 3 else Point(i, i, 'yellow') for i in range(1, 2000, 2)]
print(points[999].color)
