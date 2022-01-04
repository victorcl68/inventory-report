from abc import ABC, abstractmethod

# from inventory_report.inventory.inventory import Inventory


class Importer(ABC):
    @abstractmethod
    def import_data(file_path):
        raise NotImplementedError
        # return Inventory.reader(file_path)
