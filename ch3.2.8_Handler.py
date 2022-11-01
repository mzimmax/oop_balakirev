class Handler:
    def __init__(self, methods):
        self.methods = methods

    def __call__(self, func):
        def wrapper(request: dict, *args, **kwargs):
            if not request or request["method"] in self.methods:
                if not request or request["method"] == "GET":
                    return self.get(func, request)
                if request["method"] == "POST":
                    return self.post(func, request)

        return wrapper

    def get(self, func, request):
        return f"GET: {func(request)}"

    def post(self, func, request):
        return f"POST: {func(request)}"


assert hasattr(Handler, 'get') and hasattr(Handler, 'post'), "класс Handler должен содержать методы get и post"


@Handler(methods=('GET', 'POST'))
def contact2(request):
    return "контакты"


print(contact2({"method": "POST"}))
assert contact2({"method": "POST"}) == "POST: контакты", "декорированная функция вернула неверные данные"
print(contact2({"method": "POST"}))
assert contact2({"method": "GET"}) == "GET: контакты", "декорированная функция вернула неверные данные"
print(contact2({"method": "GET"}))
assert contact2({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
print(contact2({"method": "DELETE"}))
assert contact2({}) == "GET: контакты", "декорированная функция вернула неверные данные при указании пустого словаря"
print(contact2({}))


@Handler(methods=('POST'))
def index(request):
    return "index"


assert index({"method": "POST"}) == "POST: index", "декорированная функция вернула неверные данные"
print(index({"method": "POST"}))
assert index({"method": "GET"}) is None, "декорированная функция вернула неверные данные"
print(index({"method": "GET"}))
assert index({"method": "DELETE"}) is None, "декорированная функция вернула неверные данные"
print(index({"method": "DELETE"}))
