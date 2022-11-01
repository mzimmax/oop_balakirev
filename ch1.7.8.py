from string import ascii_uppercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_uppercase
    DIGITS = digits

    @classmethod
    def check_card_number(cls, number):
        a = [i for i in number.split("-") if not (len(i) == 4) or not (set(i) <= set(cls.DIGITS))]
        if a:
            return False
        else:
            return True

    @classmethod
    def check_name(cls, name):
        b = name.split(" ")
        a = [i for i in b if len(b) != 2 or not (set(i) <= set(cls.CHARS_FOR_NAME))]
        if a:
            return False
        else:
            return True