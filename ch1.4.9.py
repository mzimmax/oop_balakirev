import sys

# программу не менять, только добавить два метода
#sys.stdin = open('input.txt', 'r', encoding='utf-8')
#lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    """для добавления в список lst_data новых данных из переданного списка строк data;"""

    '''
    def insert(self, data):
        #print(data)
        for n, i in enumerate(data):
            d = {}
            for j, k in enumerate(i.split()):
                d[DataBase.FIELDS[j]] = k
            DataBase.lst_data.insert(n, d)
        #print(DataBase.lst_data)
        return
    '''
    def insert(self, data):
        for c in data:
            self.lst_data += [dict(zip(self.FIELDS, c.split()))]

    """ возвращает список из элементов списка lst_data в диапазоне[a; b] (включительно) по их индексам."""

    def select(self, a, b):
        print(DataBase.lst_data[a: b + 1])
        return DataBase.lst_data[a: b + 1]

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
db = DataBase()
db.insert(lst_in)
db.select(1, 2)
