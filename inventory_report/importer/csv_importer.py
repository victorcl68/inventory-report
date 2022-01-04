from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @staticmethod
    def import_data(file_path):
        return Inventory.csv_reader(file_path)
