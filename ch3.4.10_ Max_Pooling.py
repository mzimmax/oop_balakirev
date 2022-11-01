class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    @staticmethod
    def check_input(matrix):
        height = len(matrix)
        widths = [len(matrix[i]) for i in range(height)]
        width = max(widths) if max(widths) == min(widths) else None
        if width != height or width is None:
            raise ValueError("Неверный формат для первого параметра matrix.")  # height width
        if not all([isinstance(matrix[i][j], (int, float)) for i in range(width) for j in range(height)]):
            raise ValueError("Неверный формат для первого параметра matrix.")  # value not in (int, float)
        return height, width

    def __call__(self, matrix):  # *args, **kwargs):
        height, width = MaxPooling.check_input(matrix)
        new_matrix_w = width // self.step[0]
        new_matrix_h = height // self.step[1]
        result_zero_matrix = [[0 for _ in range(new_matrix_w)] for _ in range(new_matrix_h)]
        for k in range(new_matrix_w):
            for m in range(new_matrix_h):
                result_zero_matrix[k][m] = max([matrix[i + self.step[1] * k][j + self.step[0] * m]
                                                for j in range(self.size[0])
                                                for i in range(self.size[1])])
        return result_zero_matrix


mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
