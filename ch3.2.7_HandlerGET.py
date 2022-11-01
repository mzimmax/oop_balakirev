class HandlerGET:

    def __init__(self, func):
        self.__func = func

    def get(self, func, request, *args, **kwargs):
        if "method" not in request.keys() or request["method"] == "GET":
            return f"GET: {self.__func(request)}"

    def __call__(self, *args, **kwargs):
        return self.get(self.__func, args[0])


@HandlerGET
def contact(request):
    return "Сергей Балакирев"

print(contact({}))

@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
print(res)
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
print(res)
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
print(res)
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"
print(res)

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
print(res)
