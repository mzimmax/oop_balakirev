class Record:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

    def get_attr_by_idx(self, idx):
        if idx > len(self.__dict__) - 1:
            raise IndexError('неверный индекс поля')
        return tuple(self.__dict__.keys())[idx]

    def __getitem__(self, key):
        attr = self.get_attr_by_idx(key)
        return getattr(self, attr)

    def __setitem__(self, key, value):
        attr = self.get_attr_by_idx(key)
        self.__dict__[attr] = value


r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.pk, r.title, r.author)
r[0] = 2  # доступ к полю pk
print(r.pk, r.title, r.author)
r[1] = 'Супер курс по ООП'  # доступ к полю title
r[2] = 'Балакирев С.М.'  # доступ к полю author
print(r[1])  # Супер курс по ООП
r[3]  # генерируется исключение IndexError
