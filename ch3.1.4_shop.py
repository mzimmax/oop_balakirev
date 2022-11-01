class Product:
    valid_values = {"id": int, "name": str, "weight": (int, float), "price": (int, float)}

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = 1

    def __setattr__(self, key, value):
        check_type = isinstance(value, (self.valid_values[key]))
        # check_value = value > self.valid_values[key]
        if check_type:
            if type(value) == str:
                object.__setattr__(self, key, value)
            elif value > 0:
                object.__setattr__(self, key, value)
            else:
                print(value)
                raise TypeError("Неверный тип присваиваемых данных.")

        else:
            print(value)
            raise TypeError("Неверный тип присваиваемых данных.")

    def __delattr__(self, item):
        if item == "id":
            raise AttributeError("Атрибут id удалять запрещено.")


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)
        product.id = len(self.goods)

    def remove_product(self, product: Product):
        self.goods.remove(product)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")

shop1 = Shop("svetofor")
shop1.add_product(Product("meat", 2, 450))
shop1.add_product(Product("salt", 20, 50.56))
shop1.add_product(Product("onion", 2, -450))
shop1.remove_product(shop1.goods[1])
for p in shop1.goods:
    print(f"{p.id}, {p.name}, {p.weight}, {p.price}")