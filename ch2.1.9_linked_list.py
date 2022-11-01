class ObjList:
    def __init__(self, data: str) -> None:
        self.__prev = None  # ссылка на предыдущий объект связного списка
        self.__data = ""    # строка с данными.
        self.__next = None  # ссылка на следующий объект связного списка
        self.set_data(data)

    def set_next(self, obj) -> None:
        """- изменение приватного свойства __next на значение obj;"""
        self.__next = obj

    def set_prev(self, obj) -> None:
        """- изменение приватного свойства __prev на значение obj;"""
        self.__prev = obj

    def get_next(self) -> object:
        "- получение значения приватного свойства __next;"
        return self.__next

    def get_prev(self) -> object:
        """- получение значения приватного свойства __prev;"""
        return self.__prev

    def set_data(self, data: str) -> None:
        """- изменение приватного свойства __data на значение data;"""
        self.__data = data

    def get_data(self) -> str:
        """- получение значения приватного свойства __data."""
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None  # ссылка на первый объект связного списка
        self.tail = None  # ссылка на последний объект связного списка

    def add_obj(self, obj: ObjList) -> None:
        """добавление нового объекта obj класса ObjList
         в конец связного списка;"""
        if self.head:
            obj.set_prev(self.tail)
            self.tail.set_next(obj)
            self.tail = obj
        else:
            self.head = obj
            self.tail = obj

    def remove_obj(self) -> None:
        """удаление последнего объекта из связного списка;"""
        tmp = self.tail.get_prev()
        if tmp and tmp.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail, self.head = None, None

    def get_data(self):
        """получение списка из строк локального свойства __data
         всех объектов связного списка."""
        data = []
        obj = self.head
        while obj:
            data.append(obj.get_data())
            obj = obj.get_next()
        return data


ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
assert ls_one.get_data() == [1], "метод get_data вернул неверные данные"

h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
ls_one.remove_obj()
assert ls_one.get_data() == [], "метод get_data вернул неверные данные для пустого списка, возможно, неверно работает метод remove_obj"

ls2 = LinkedList()
assert ls.head != ls2.head, "атрибут head должен принадлежать объекту класса LinkedList, а не самому классу"
assert ls.tail != ls2.tail, "атрибут tail должен принадлежать объекту класса LinkedList, а не самому классу"

h = ls.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.head
n = 0
while h:
    h = h._ObjList__next
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __next"

h = ls.tail
n = 0
while h:
    n += 1
    h = h.get_prev()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.tail
n = 0
while h:
    h = h._ObjList__prev
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __prev"