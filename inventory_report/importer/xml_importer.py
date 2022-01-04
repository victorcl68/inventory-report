from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_path):
        return Inventory.xml_reader(file_path)
