import datetime


class SimpleReport:
    @staticmethod
    def __diff_date_from_now(date_str):
        date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return abs((date_dt - datetime.date.today()).days)

    @staticmethod
    def __product_counter(company, product_list):
        product_counter = 0
        for product in product_list:
            if product["nome_da_empresa"] == company:
                product_counter += 1
        return product_counter

    @staticmethod
    def __format_report(oldest, newest, company):
        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {newest}\n"
            f"Empresa com maior quantidade de produtos estocados: {company}\n"
        )

    @classmethod
    def generate(cls, product_list):
        oldest = product_list[0]["data_de_fabricacao"]
        newest = product_list[0]["data_de_validade"]

        diff_time = cls.__diff_date_from_now(
            product_list[0]["data_de_validade"]
        )

        company = product_list[0]["nome_da_empresa"]

        total_counter = 0
        for product in product_list:
            if product["data_de_fabricacao"] < oldest:
                oldest = product["data_de_fabricacao"]

            product_diff_time = cls.__diff_date_from_now(
                product["data_de_validade"]
            )

            if product_diff_time < diff_time:
                diff_time = product_diff_time
                newest = product["data_de_validade"]

            product_counter = cls.__product_counter(
                product["nome_da_empresa"], product_list
            )

            if product_counter > total_counter:
                total_counter = product_counter
                company = product["nome_da_empresa"]
        return cls.__format_report(oldest, newest, company)
