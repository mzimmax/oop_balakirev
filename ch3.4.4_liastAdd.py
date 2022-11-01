"""
>>> lst = NewList()
>>> lst1 = NewList([0, 1, -3.4, "abc", True])
>>> lst2 = NewList([1, 0, True])
>>> lst1.get_list()  # lst1.get_list() == [0, 1, -3.4, "abc", True], "метод get_list вернул неверный список"
[0, 1, -3.4, 'abc', True]
>>> lst.get_list()  # lst.get_list() == [], "метод get_list вернул неверный список"
[]
>>> lst2.get_list()
[1, 0, True]
>>> res1 = lst1 - lst2
>>> res1.get_list()  # assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
[-3.4, 'abc']
>>> res2 = lst1 - [0, True]
>>> lst1.get_list()
[0, 1, -3.4, 'abc', True]
>>> res2.get_list()
[1, -3.4, 'abc']
>>> res3 = [1, 2, 3, 4.5] - lst2  # lst2 = NewList([1, 0, True])
>>> lst1 -= lst2
>>> res1.get_list()  # assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
[-3.4, 'abc']
>>> res2.get_list()  # assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
[1, -3.4, 'abc']
>>> res3.get_list()  # assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
[2, 3, 4.5]
>>> lst1.get_list()  # assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
[-3.4, 'abc']
>>> lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
>>> lst_2 = NewList([10, True, False, True, 1, 7.87])
>>> res = lst_1 - lst_2
>>> res.get_list()  # assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"
[0, 5.0, 1, True, -7.87]
>>> a = NewList([2, 3])
>>> res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
>>> res_4.get_list()  # assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
[1, 2]
"""


class NewList:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self.elements = elements  # list(elements)

    def get_list(self):
        return self.elements  # [i for i in  self.elements]

    @staticmethod
    def sub(a, b):
        c = []
        for i in a:
            if id(i) not in [id(j) for j in b]:
                c.append(i)
        return c

    def __sub__(self, other):
        a = self.get_list()
        b = other
        if isinstance(other, NewList):
            b = other.get_list()
            res = NewList.sub(a, b)
        elif isinstance(other, list):
            res = NewList.sub(a, b)
        elif isinstance(other, (int, float, str)):
            b = list(other)
            res = NewList.sub(a, b)
        return NewList(res)

    def __isub__(self, other):
        a = self.get_list()
        b = other
        if isinstance(other, NewList):
            b = other.get_list()
            res = NewList.sub(a, b)
        elif isinstance(other, list):
            res = NewList.sub(a, b)
        elif isinstance(other, (int, float, str)):
            b = list(other)
            res = NewList.sub(a, b)
        self.elements = res
        return self

    def __rsub__(self, other):
        a = other
        b = self.get_list()
        if isinstance(other, NewList):
            b = other.get_list()
            res = NewList.sub(a, b)
        elif isinstance(other, list):
            res = NewList.sub(a, b)
        elif isinstance(other, (int, float, str)):
            b = list(other)
            res = NewList.sub(a, b)
        return NewList(res)

    def __repr__(self):
        return f"{self.elements}"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
