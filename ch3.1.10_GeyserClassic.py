import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.slots = {1: [Mechanical, None], 2: [Aragon, None], 3: [Calcium, None]}

    def add_filter(self, slot_num, filterr):
        if self.slots[slot_num][1] is None and type(filterr) == self.slots[slot_num][0]:
            self.slots[slot_num][1] = filterr

    def remove_filter(self, slot_num):
        self.slots[slot_num][1] = None

    def get_filters(self):
        return [self.slots[i][1] for i in self.slots]

    def water_on(self):
        return all(my_water.get_filters())\
               and len(["esxpirate" for i in self.slots
                        if (time.time() - self.slots[i][1].date) <= self.MAX_DATE_FILTER]) == 3


class Slot:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        pass


class Mechanical(Slot):
    "- для очистки от крупных механических частиц;"
    pass


class Aragon(Slot):
    "- для последующей очистки воды;"
    pass


class Calcium(Slot):
    "- для обработки воды на третьем этапе."
    pass


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3,
                                                                            Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"
my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
w = my_water.water_on()  # False
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on()  # True
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
