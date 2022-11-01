TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog

class Dialog:

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            a = super().__new__(DialogWindows)
        else:
            a = super().__new__(DialogLinux)
        setattr(a, "name", args[0])
        return a


dlg1 = Dialog("Hello")
print(dlg1, dlg1.name)

TYPE_OS = 2

dlg2 = Dialog("Hello")
print(dlg2, dlg2.name)
