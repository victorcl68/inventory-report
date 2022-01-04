from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_path):
        return Inventory.json_reader(file_path)
