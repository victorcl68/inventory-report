from collections.abc import Iterable, Iterator


class ListaSemNone(Iterable):
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return MeuIterator(self.data.copy())


class MeuIterator(Iterator):
    def __init__(self, iter_data):
        self.iter_data = iter_data
        self.indice = -1

    def __next__(self):
        try:
            if self.iter_data[self.indice] is None:
                self.indice += 1
            item = self.iter_data[self.indice]
        except IndexError:
            raise StopIteration
        else:
            self.indice += 1
            return item


# - - - - - -
lista = ListaSemNone([1, 20, 34, "Alfa", None, "Beta", -7.8])

for item in lista:
    print(item)
