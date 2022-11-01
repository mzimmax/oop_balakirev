class Book:

    def __init__(self, title, author, price):
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_title(self, title):
        "запись в локальное приватное свойство __title объектов класса Book значения title;"
        self.__title = title

    def set_author(self, author):
        "запись в локальное приватное свойство __author объектов класса Book значения author;"
        self.__author = author

    def set_price(self, price):
        "запись в локальное приватное свойство __price объектов класса Book значения price;"
        self.__price = price

    def get_title(self):
        "получение значения локального приватного свойства __title объектов класса Book;"
        return self.__title

    def get_author(self):
        "получение значения локального приватного свойства __author объектов класса Book;"
        return self.__author

    def get_price(self):
        "получение значения локального приватного свойства __price объектов класса Book;"
        return self.__price

#
# Объекты класса Book предполагается создавать командой:
#
# book = Book(автор, название, цена)
#
# При этом, в каждом объекте должны создаваться приватные локальные свойства:
#
# __author - строка с именем автора;
# __title - строка с названием книги;
# __price - целое число с ценой книги.

book = Book('50 Cent', 'Aboba', 999)
book.set_title('Amogus')
book.set_author('NLE Choppa')
book.set_price(123)
book.get_title()
book.get_author()
book.get_price()