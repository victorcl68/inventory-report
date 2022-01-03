import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(file_path, report_type):
        with open(file_path) as file:
            if "csv" in file_path:
                reader = list(csv.DictReader(file))
            else:
                reader = json.load(file)
            if report_type == "simples":
                return SimpleReport.generate(reader)
            else:
                return CompleteReport.generate(reader)
