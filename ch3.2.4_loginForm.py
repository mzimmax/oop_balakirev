from string import ascii_lowercase, digits

digits += "1234567890"


class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


# здесь прописывайте классы валидаторов: LengthValidator и CharsValidator

class LengthValidator:
    """
    lv = LengthValidator(min_length, max_length)
    # min_length - минимально допустимая длина;
    max_length - максимально допустимая длина
    """

    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return isinstance(args[0], str) and self.min_length < len(args[0]) < self.max_length


class CharsValidator:
    """
    cv = CharsValidator(chars)
    # chars - строка из допустимых символов
    """

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return isinstance(str(args[0]), str) and set(args[0]) < set(self.chars)


### end
lg = LoginForm("Вход на сайт", validators=[LengthValidator(5, 50), CharsValidator(ascii_lowercase + digits)])
v1 = LengthValidator(5, 50)
assert v1("123") == False, "валиадтор LengthValidator вернул True, хотя данные некорректны"
lg.post({"login": "balakirev", "password": "panda"})
if lg.is_validate():
    print("Дальнейшая обработка данных формы")



