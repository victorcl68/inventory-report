from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, iter_data):
        self.index = 0
        self.iter_data = iter_data

    def __next__(self):
        try:
            item = self.iter_data[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return item
