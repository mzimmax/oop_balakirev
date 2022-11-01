class RenderDigit:
    def __call__(self, *args, **kwargs):
        try:
            digit = int(args[0])
        except ValueError:
            digit = None
        return digit


class InputValues:
    def __init__(self, render: RenderDigit):
        self.__render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self.__render(i) for i in func().split()]
        return wrapper


render = RenderDigit()
# d1 = render("123")   # 123 (целое число)
# d2 = render("45.54")   # None (не целое число)
# d3 = render("-56")   # -56 (целое число)
# d4 = render("12fg")  # None (не целое число)
# d5 = render("abc")   # None (не целое число)
# # print(d1, d2, d3, d4, d5)


@InputValues(render)
def input_dg():
    return input()


res = input_dg()
print(res)
