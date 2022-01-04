from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        Inventory.check_extension(file_path, ".csv")
        return Inventory.reader(file_path)
