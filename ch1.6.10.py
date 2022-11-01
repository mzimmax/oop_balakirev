class Factory:

    def __init__(self):
        self.string = None

    def build_sequence(self):
        return []

    def build_number(self, string):
        self.string = string
        return float(self.string)


def parse_format(string, factory):
    seq = factory.build_sequence()
    for sub in string.split(","):
        item = factory.build_number(sub)
        seq.append(item)

    return seq


class Loader:
    pass


# эти строчки не менять!
ld = Loader()
s = "4, 5, -6.5" #input()
res = parse_format(s, Factory())
print(res)
