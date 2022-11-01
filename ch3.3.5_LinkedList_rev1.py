class Obj:
    def __set_name__(self, owner, name):
        self.__name = f"_{owner.__name__}__{name}"

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class ObjList:
    next = Obj()
    prev = Obj()
    data = Obj()

    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add_obj(self, obj: ObjList):
        if not self.head:
            self.head = self.tail = obj
        else:
            # tmp = self.tail
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def get_obj_by_index(self, indx):
        current = self.head
        if indx < len(self):
            for _ in range(indx):
                current = current.next
        return current

    def remove_obj(self, indx: int):
        if len(self) > 1 and indx < len(self):
            deleted_obj = self.get_obj_by_index(indx)
            if deleted_obj.prev:
                deleted_obj.prev.next = deleted_obj.next
            else:
                deleted_obj.next.prev = None
                self.head = deleted_obj.next
            if deleted_obj.next:
                deleted_obj.next.prev = deleted_obj.prev
            else:
                deleted_obj.prev.next = None
                self.tail = deleted_obj.prev
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            raise ValueError(f"index: {indx} out of LinkedList range")

    def __len__(self):
        """Возвращает число объектов в связном списке"""
        count = 0 #  1 if self.head else 0
        tmp = self.head
        while tmp:
            count += 1
            tmp = tmp.next
        return count

    def __call__(self, indx):
        return self.get_obj_by_index(indx).data


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"
print(len(ln), ln.__dict__)
ln.remove_obj(0)
print(len(ln), ln.__dict__)
ln.remove_obj(0)
print(len(ln), ln.__dict__)
ln.remove_obj(0)
print(len(ln), ln.__dict__)
ln.remove_obj(0)
print(len(ln), ln.__dict__)
ln.remove_obj(2)
print(len(ln), ln.__dict__)