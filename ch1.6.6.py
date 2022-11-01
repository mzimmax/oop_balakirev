class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"

obj = AbstractClass()




obj123 = AbstractClass()
assert obj123 == "Ошибка: нельзя создавать объекты абстрактного класса"




