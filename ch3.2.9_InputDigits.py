class InputDigits:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.__func().split()]

#
# res = input()
# print(res.split())


@InputDigits
def input_dg():
    return input()


res = input_dg()
print(res)



