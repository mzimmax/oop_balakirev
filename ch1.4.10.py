from typing import List, Dict


class Translator:
    dictionary = Dict[str, List[str]]

    def add(self, eng: str, rus: str) -> None:
        if eng not in self.dictionary.keys():
            self.dictionary[eng] = []
        self.dictionary[eng].append(rus)

    def remove(self, eng: str):
        self.dictionary.pop(eng)

    def translate(self, eng: str) -> List[str]:
        return self.dictionary[eng]


tr = Translator()

tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(tr.translate('go'))
