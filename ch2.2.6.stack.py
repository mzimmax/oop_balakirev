class StackObj:
    def __init__(self, data: str) -> None:
        self.__data = self.__next = None
        self.data = data

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

    @property
    def next(self) -> object:
        return self.__next

    @next.setter
    def next(self, obj: object):
        if type(obj) == StackObj or obj is None:
            self.__next = obj

    def __repr__(self):
        return f"data: {self.data} next: {self.next}"


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj: StackObj):
        tmp = self.top
        if tmp:
            while tmp.next:
                tmp = tmp.next
            tmp.next = obj
        else:
            self.top = obj

    def pop(self) -> StackObj:
        tmp = self.top
        prev = None
        while tmp.next:
            tmp, prev = tmp.next, tmp
        if isinstance(prev, StackObj):
            prev.next = None
        else:
            self.top = None
        return tmp

    def get_data(self) -> list:
        tmp = self.top
        list_data = []
        while tmp:
            list_data.append(tmp.data)
            tmp = tmp.next
        return list_data


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.push(StackObj("obj4"))
print(*[st.pop() for _ in range(5)], sep='\n')
print()
res = st.get_data()  # ['obj1', 'obj2']
print(res)
