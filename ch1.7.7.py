from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput


class Input:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if len(name) < 3 or len(name) > 50:
            raise ValueError("некорректное поле name")
        for i in set(name):
            if i not in cls.CHARS_CORRECT:
                raise ValueError("некорректное поле name")
        return name

    def __new__(cls, *args, **kwargs):
        if cls.check_name(args[0]):
            return super().__new__(cls)
        else:
            raise ValueError("некорректное поле name")

    def __init__(self, name, size=10):
        self.name = self.check_name(name)
        self.size = size  # len(name)


class TextInput(Input):
    def get_html(self):
        return "".join(["<p class='login'>",
                        self.name,
                        ": <input type='text' size=",
                        str(self.size),
                        " />"])


class PasswordInput(Input):

    def get_html(self):
        return "".join(["<p class='password'>",
                        self.name,
                        ": <input type='text' size=",
                        str(self.size),
                        " />"])


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин."), PasswordInput("Пароль"))
html = login.render_template()
print(html)
