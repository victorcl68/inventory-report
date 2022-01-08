import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Verifique os argumentos\n')
        return False
    if ".csv" in sys.argv[1]:
        inventory_importer = InventoryRefactor(CsvImporter)
    if ".json" in sys.argv[1]:
        inventory_importer = InventoryRefactor(JsonImporter)
    if ".xml" in sys.argv[1]:
        inventory_importer = InventoryRefactor(XmlImporter)
    report = inventory_importer.import_data(sys.argv[1], sys.argv[2])
    print(str(report)[:-1])
