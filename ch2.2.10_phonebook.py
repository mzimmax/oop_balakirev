class PhoneBook:
    def __init__(self):
        self.pages = []

    def add_phone(self, phone):
        # - добавление нового номера телефона (в список);
        self.pages.append(phone)

    def remove_phone(self, indx):
        # - удаление номера телефона по индексу списка;
        del self.pages[indx]

    def get_phone_list(self):
        return self.pages
        # - получение списка из объектов всех телефонных номеров.


class PhoneNumber:
    def __init__(self, number, fio):
        self.__number = self.__fio = None
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if type(value) == int and len(str(value)) == 11:
            self.__number = value

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value: str):
        if type(value) == str:
            self.__fio = value

    def __repr__(self):
        return f"Phone: {self.__number}, fio: {self.__fio}"


p = PhoneBook()
p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
p.add_phone(PhoneNumber(21345678901, "Панда"))
p.add_phone(PhoneNumber(21340078901, "Lа"))
p.add_phone(PhoneNumber(23345678901, "Пан"))
p.remove_phone(2)
phones = p.get_phone_list()
print(phones)