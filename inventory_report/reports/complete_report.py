from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def __format_report(product_list):
        enterprises = set()
        company_stock_dictionary = dict()

        index = -1

        head = "Produtos estocados por empresa: \n"
        body = str()

        for product in product_list:
            enterprises.add(product["nome_da_empresa"])

        for each_enterprise in enterprises:
            company_stock_dictionary[each_enterprise] = 0

        for product in product_list:
            company_stock_dictionary[product["nome_da_empresa"]] += 1

        for i in company_stock_dictionary:
            index += 1
            company_name = list(company_stock_dictionary.keys())[index]
            stock = list(company_stock_dictionary.values())[index]
            body += f"- {company_name}: {stock}\n"

        return head + body

    @classmethod
    def generate(cls, product_list):
        simple_report = super().generate(product_list)
        complement_report = cls.__format_report(product_list)
        complete_report = simple_report+"\n"+complement_report
        return complete_report
