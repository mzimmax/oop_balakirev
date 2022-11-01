class Item:
    def __init__(self, name, money):
        if type(name) == str:
            self.name = name
        if type(money) in (int, float):
            self.money = money

    def __repr__(self):
        return f"name: {self.name}, money: {self.money}\n"

    def __add__(self, other):
        if type(other) == Item:
            return self.money + other.money

    def __radd__(self, other):
        if type(other) in (int, float):
            return other + self.money


class Budget:
    def __init__(self):
        self.items = []

    def add_item(self, it: Item):
        self.items.append(it)

    def remove_item(self, indx: int):
        self.items.pop(indx)

    def get_items(self):
        return self.items

    def total(self):
        return sum([i.money for i in self.items])


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))
print(my_budget.get_items())
my_budget.remove_item(2)
print(my_budget.get_items())
print(my_budget.total())
# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)








