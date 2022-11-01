class Vector:
    def __init__(self, *coords):
        if all([isinstance(i, (int, float)) for i in coords]):
            self.coords = coords

    def __len__(self):
        return len(self.coords)

    def __add__(self, other):
        return Vector(*Vector.take_operation(self, other, "add"))

    def __sub__(self, other):
        return Vector(*Vector.take_operation(self, other, "sub"))
    
    def __mul__(self, other):
        return Vector(*Vector.take_operation(self, other, "mul"))

    def __iadd__(self, other):
        if type(other) in (int, float):
            self.coords = tuple([i + other for i in self.coords])
        else:
            self.coords = tuple(Vector.take_operation(self, other, "add"))
        return self
    
    def __isub__(self, other):
        if type(other) in (int, float):
            self.coords = tuple([i - other for i in self.coords])
        else:
            self.coords = tuple(Vector.take_operation(self, other, "sub"))
        return self

    def __eq__(self, other):
        return all(Vector.take_operation(self, other, "eq"))

    @staticmethod
    def take_operation(A, B, opp):
        if isinstance(A, Vector) and isinstance(B, Vector) and len(A) == len(B):
            op = {"add": lambda a: a[0] + a[1],\
                  "sub": lambda a: a[0] - a[1],\
                  "mul": lambda a: a[0] * a[1],\
                  "eq": lambda a: a[0] == a[1]} 
            return  map(op[opp], zip(A.coords, B.coords))
        raise ArithmeticError('размерности векторов не совпадают')


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(6, 7)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True

print(v1 + v3)   # Error
