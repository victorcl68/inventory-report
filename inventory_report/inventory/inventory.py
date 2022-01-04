import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def csv_reader(file_path):
        with open(file_path) as file:
            return list(csv.DictReader(file))

    @staticmethod
    def json_reader(file_path):
        with open(file_path) as file:
            return json.load(file)

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

    @classmethod
    def import_data(cls, file_path, report_type):
        if "csv" in file_path:
            reader = cls.csv_reader(file_path)
        elif "json" in file_path:
            reader = cls.json_reader(file_path)
        else:
            reader = cls.xml_reader(file_path)
        if report_type == "simples":
            return SimpleReport.generate(reader)
        else:
            return CompleteReport.generate(reader)
