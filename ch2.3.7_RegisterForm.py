class ValidateString:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        if type(string) == str and \
                self.min_length <= len(string) <= self.max_length:
            return True


class StringValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if instance.validate(value):
            setattr(instance, self.name, value)

    def __init__(self, validator=ValidateString(3, 100)):
        self.validate = validator


class RegisterForm:
    st = ValidateString(3, 100).validate("aaa")
    login = StringValue(st)
    password = StringValue(ValidateString(5, 100))
    email = StringValue(ValidateString(5, 100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print("<form>")
        print(f"{self.login}: <login>")
        print(f"{self.password}: <password>")
        print(f"{self.email}: <email>")
        print("</form>")


# validate = ValidateString(min_length=3, max_length=100)
validate = ValidateString(3, 100)
print(validate.validate("22"))
# st = StringValue(validator=ValidateString(min_length, max_length))
# st = StringValue(validate)
# st = StringValue(ValidateString(3, 100))
form = RegisterForm("логин", "пароль121", "email")

form.show()
