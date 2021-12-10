import datetime

produtos = [
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2040-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 2,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "2",
    "data_de_fabricacao": "2010-07-04",
    "data_de_validade": "2025-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  },
  {
    "id": 3,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "2",
    "data_de_fabricacao": "2019-07-04",
    "data_de_validade": "2030-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
]


class SimpleReport():
    @staticmethod
    def __diff_date_from_now(date_str):
        date_dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return (date_dt - datetime.date.today()).days

    @classmethod
    def generate(cls, product_list):
        old_fab = product_list[0]["data_de_fabricacao"]
        valid_date = product_list[0]["data_de_validade"]
        diff_time = cls.__diff_date_from_now(
            product_list[0]["data_de_validade"])
        # company_name = product_list[0]["nome_da_empresa"]
        for product in product_list:
            if product["data_de_fabricacao"] < old_fab:
                old_fab = product["data_de_fabricacao"]
            product_diff_time = cls.__diff_date_from_now(
                product["data_de_validade"])
            if product_diff_time < diff_time:
                diff_time = product_diff_time
                valid_date = product["data_de_validade"]
        return old_fab, valid_date


print(SimpleReport.generate(produtos))
