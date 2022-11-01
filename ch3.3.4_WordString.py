class WordString:
    def __init__(self, string=""):
        self.string = string

    def __call__(self, indx, *args, **kwargs):
        return self.string.split()[indx]

    def __len__(self):
        return len(self.string.split())

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value):
        self.__string = value


words = WordString()
words.string = "Курс по Python    ООП от  Сергея Балакирева"
print(words.string)
# assert words.string == "Курс по Python    ООП от  Сергея Балакирева"
n = len(words)

first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")



