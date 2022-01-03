import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, file_path, report_type):
        with open(file_path) as file:
            if "csv" in file_path:
                reader = list(csv.DictReader(file))
            elif "json" in file_path:
                reader = json.load(file)
            else:
                reader = cls.xml_reader(file_path)
            if report_type == "simples":
                return SimpleReport.generate(reader)
            else:
                return CompleteReport.generate(reader)

    # https://www.datacamp.com/community/tutorials/python-xml-elementtree
    @staticmethod
    def xml_reader(file_path):
        root = Et.parse(file_path).getroot()
        reader = []
        for item in root:
            dict_list = {}
            for child in item:
                dict_list[child.tag] = child.text
            reader.append(dict_list)
        return reader
