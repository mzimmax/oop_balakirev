class StackObj:
    def __init__(self, data):
        self.__data = self.__next = None
        self.data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            tmp = self.top
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj

    def show(self):
        item = self.top
        while item.next:
            print(item.data, end=" ")
            item = item.next
        print(item.data)

    def pop_back(self):
        if self.top:
            tmp = self.top
            prev = None
            while tmp.next:
                prev = tmp
                tmp = tmp.next
            prev.next = None

    def __add__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
            return self

    def __iadd__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
            return self

    def __mul__(self, other):
        if isinstance(other, (list, tuple)):
            for i in other:
                self.push_back(StackObj(i))
        return self

    def __imul__(self, other):
        if isinstance(other, (list, tuple)):
            for i in other:
                self.push_back(StackObj(i))
        return self


h = StackObj('5')
print(h.data)  # 5
st = Stack()
st.push_back(StackObj('1'))
st.push_back(StackObj('2'))
st.push_back(StackObj('3'))
st.show()  # 1 2 3
st = st + StackObj('4')
st += StackObj('5')
st.show()  # 1 2 3 4 5
st = st * [str(i) for i in range(6, 9)]
st *= [str(i) for i in range(9, 12)]
st.show()  # 1 2 3 4 5 6 7 8 9 10 11

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
