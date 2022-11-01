class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and 1 < len(model) < 101:
            self.__model = model


car = Car()
car.model = "Toyota"
car.model = 'E'
print(car.model)
car.model = 22
car.model = '22'
car.model = "AUDI"
print(car.model)
