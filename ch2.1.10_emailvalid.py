from random import choice, randint


class EmailValidator:
    ALFABET_LOWERCASE = 'abcdefgihjklmnopqrstuwxyz'
    ALFABET = ALFABET_LOWERCASE + ALFABET_LOWERCASE.upper()
    DIGITS = '0123456789'
    VALID_CHAR = ALFABET + DIGITS + '_.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email: str):
        if cls.__is_email_str(email):
            if email.find("@") > 0:
                email_part = email.split("@")
                return all([len(email_part) == 2,
                            set(email_part[0]) < set(cls.VALID_CHAR),
                            set(email_part[1]) < set(cls.VALID_CHAR),
                            len(email_part[0]) < 101,
                            len(email_part[1]) < 51,
                            '.' in set(email_part[1]),
                            email_part[0].find("..") < 0,
                            email_part[1].find("..") < 0])
        return False

    @classmethod
    def get_random_email(cls):
        random_email = "".join([choice(cls.VALID_CHAR) for _ in range(randint(1,101))])
        random_email += "@gmail.com"
        return random_email

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)


assert EmailValidator._EmailValidator__is_email_str('abc') == True
assert EmailValidator.check_email("sc_lib@list.ru") == True
assert EmailValidator.check_email("sc_lib@list_ru") == False
assert EmailValidator.check_email("sc@lib@list_ru") == False
assert EmailValidator.check_email("sc.lib@list_ru") == False
assert EmailValidator.check_email("sclib@list.ru") == True
assert EmailValidator.check_email("sc.lib@listru") == False
assert EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False
