import datetime


class SimpleReport:
    @staticmethod
    def __diff_date_from_now(date_str):
        date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return abs((date_dt - datetime.date.today()).days)

    def __count_products(cp_name, product_list):
        count_products = 0
        for product in product_list:
            if product["nome_da_empresa"] == cp_name:
                count_products += 1
        return count_products

    def __format_report(old_fab, valid_date, cp_name):
        return (
            f"Data de fabricação mais antiga: {old_fab}\n"
            f"Data de validade mais próxima: {valid_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {cp_name}\n"
        )

    @classmethod
    def generate(cls, product_list):
        old_fab = product_list[0]["data_de_fabricacao"]
        valid_date = product_list[0]["data_de_validade"]
        diff_time = cls.__diff_date_from_now(
            product_list[0]["data_de_validade"]
        )
        cp_name = product_list[0]["nome_da_empresa"]
        count_total = 0
        for product in product_list:
            if product["data_de_fabricacao"] < old_fab:
                old_fab = product["data_de_fabricacao"]

            product_diff_time = cls.__diff_date_from_now(
                product["data_de_validade"]
            )
            if product_diff_time < diff_time:
                diff_time = product_diff_time
                valid_date = product["data_de_validade"]

            count_products = cls.__count_products(
                product["nome_da_empresa"], product_list
            )
            if count_products > count_total:
                count_total = count_products
                cp_name = product["nome_da_empresa"]
        return cls.__format_report(old_fab, valid_date, cp_name)
