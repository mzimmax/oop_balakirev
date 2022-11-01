class DigitRetrieve:
    DIGITS = "1234567890"

    def __call__(self, *args, **kwargs):
        if type(args[0]) == str:
            if args[0][0] == '-':
                if set(args[0][1:]) < set(self.DIGITS):
                    return int(args[0])
            else:
                if set(args[0]) < set(self.DIGITS):
                    return int(args[0])



dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
print(digits)


