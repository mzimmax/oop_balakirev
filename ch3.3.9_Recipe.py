class Ingredient:
    """
    ing = Ingredient(name, volume, measure)
    name - название ингредиента (строка);
    volume - объем ингредиента в рецепте (вещественное число);
    measure - единица измерения объема ингредиента (строка), например, литр, чайная ложка, грамм, штук и т.д.;
    """

    def __init__(self, name, volume, measure):
        self.name = name if isinstance(name, str) else ""
        self.volume = volume if isinstance(volume, (int, float)) else 0
        self.measure = measure if isinstance(measure, str) else ""

    def __str__(self):
        """
        str(ing)  # название: объем, ед. изм.
        >>> ing = Ingredient("Соль", 1, "столовая ложка")
        >>> str(ing) #
        'Соль: 1, столовая ложка'
        """
        return f"{self.name}: {self.volume}, {self.measure}"


class Recipe:
    """
    recipe = Recipe()
    recipe = Recipe(ing_1, ing_2, ..., ing_N)
    >>> recipe = Recipe()
    >>> recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
    >>> recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
    >>> recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
    >>> ings = recipe.get_ingredients()
    >>> n = len(recipe)
    >>> print(n)# n = 3
    3
    """

    def __init__(self, *args):
        self.ings: list = list(args)

    def add_ingredient(self, ing: Ingredient):
        self.ings.append(ing)

    def get_ingredients(self):
        """получение кортежа из объектов класса Ingredient текущего рецепта."""
        return self.ings

    def remove_ingredient(self, ing):
        """удаление ингредиента по объекту ing (объект класса Ingredient) из рецепта;"""
        self.ings.remove(ing)

    def __len__(self):
        """возвращает число ингредиентов в рецепте."""
        return len(self.ings)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    i1 = Ingredient("Соль", 1, "столовая ложка")
    i2 = Ingredient("Мука", 1, "кг")
    i3 = Ingredient("Мясо баранины", 10, "кг")
    i4 = Ingredient("Масло", 100, "гр")
    recipe = Recipe(i1, i2, i3)
    recipe.add_ingredient(i4)
    recipe.remove_ingredient(i3)

    assert len(recipe) == 3, "функция len вернула неверное значение"
    lst = recipe.get_ingredients()
    for x in lst:
        assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
        assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x,
                                                                       'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"

    assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"

    i4 = Ingredient("Масло", 120, "гр")
    recipe.add_ingredient(i4)
    assert len(recipe) == 4, "функция len вернула неверное значение"
