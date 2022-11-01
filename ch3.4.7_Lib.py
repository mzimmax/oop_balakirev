class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"\n{self.title}, {self.author}, {self.year}"


class Lib:
    def __init__(self, book_list=None):
        if book_list is None:
            book_list = []
        self.book_list = book_list

    def __len__(self):
        print(self.__dict__)
        return len(self.book_list)

    def __add__(self, other):
        if isinstance(other, Book):
            self.book_list.append(other)
            return self

    # def __iadd__(self, other):
    #     if isinstance(other, Book):
    #         self.book_list.append(other)
    #         return self

    def __sub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        if type(other) == int:
            self.book_list.pop(other)
        return self

    def __isub__(self, other):
        if type(other) == Book:
            self.book_list.remove(other)
        if type(other) == int:
            self.book_list.pop(other)
        return self


lib = Lib()
lib = lib + Book('Процесс', 'Кафка', 2020)  # добавление новой книги в библиотеку
lib += Book('Три товарища', 'Ремарк', 2021)
lib += Book('Бесы', 'Достоевский', 2022)
lib += Book('1984', 'Оруэлл', 2022)
print("1- liba: ", len(lib))
lib -= 1
print("1- liba: ", len(lib))
lib1 = Lib()
lib1 += lib1 + Book('Бесы', 'Достоевский', 2022)
lib1 += Book('Три товарища', 'Ремарк', 2021)
lib1 -= 0
print("1 - liba: ", len(lib))
# print("2 - liba: ", len(lib1))




