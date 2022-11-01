class StackObj:
    def __init__(self, data):
        self.__data = self.__next = None
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) == StackObj or obj is None:
            self.__next = obj

    def __repr__(self):
        return f"{self.data}"


class Stack:
    def __init__(self):
        self.top = None
        self.obj_count = 0

    def __len__(self):
        return self.obj_count

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            trev = self.top
            while trev.next:
                trev = trev.next
            trev.next = obj
        self.obj_count += 1

    def pop(self):
        if self.top:
            trev1 = self.top
            trev2 = trev1
            while trev1.next:
                trev2 = trev1
                trev1 = trev1.next
            self.obj_count -= 1
            if len(self) == 0:
                self.top = None
            trev2.next = None
            return trev1
        else:
            raise ValueError("empty")

    def __getitem__(self, item):
        self.check_indx(item)
        trev = self.top
        n = 0
        while n != item:
            trev = trev.next
            n += 1
        return trev

    def __setitem__(self, indx, obj):
        self.check_indx(indx)
        if indx == 0:
            obj.next = self.top.next
            self.top = obj
        else:
            trev1 = self.top
            trev2 = None
            n = 0
            while n < indx:
                trev2 = trev1
                trev1 = trev1.next
                n += 1
            if trev1.next:
                obj.next = trev1.next
            else:
                obj.next = None
            trev2.next = obj

    def check_indx(self, indx):
        if type(indx) == int and 0 <= indx < len(self):
            return True
        raise IndexError('неверный индекс')


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"

