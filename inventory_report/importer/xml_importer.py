from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        Inventory.check_extension(file_path, ".xml")
        return Inventory.reader(file_path)
        # return super().import_data(file_path)
