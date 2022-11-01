class Dictionary:
    pass


dict_attr = {'rus': 'Питон', 'eng': 'Python'}
for k, j in dict_attr.items():
    setattr(Dictionary, k, j)

print(getattr(Dictionary, "rus_word", False))
