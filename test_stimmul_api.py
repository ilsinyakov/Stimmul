from PartnerAuthApi import PartnerAuthApi
from ProductProviderApi import ProductProviderApi


base_url = 'https://api.dev.opt.sarawan.ru/api'

partner_auth_api = PartnerAuthApi(base_url)
product_provider_api = ProductProviderApi(base_url)


def test_add_product():
    email = "zaytceva.jula@gmail.com"
    inn = "5675432167"
    password = "11111111"
    partner_auth = partner_auth_api.get_partner_auth_token(email, inn,
                                                           password)

    token = partner_auth["token"]

    new_product_data = {
        "name": "Pig",
        "manufacturer": "RF",
        "country_of_manufacture": "RF",
        "sarawan_category": 2,
        "category": 4,
        "description": "Cool",
        "article": "string",
        "price": 20000,
        "price_type": "it",
        "unit_quantity": 1,
        "quantity_step": 1,
        "product_weight": 300,
        "product_volume": 280,
        "stock_quantity": 10,
        "is_active": True
        }
    new_product = product_provider_api.create_new_product(token,
                                                          new_product_data)
    new_product_id = new_product["id"]
    new_product_name = new_product["name"]
    assert new_product_name == new_product_data["name"], 'Names is not equal'

    products = product_provider_api.get_products(token)
    is_new_product_in_list = False
    for product in products["results"]:
        if new_product_id == product["id"]:
            is_new_product_in_list = True

    assert is_new_product_in_list, \
        "There is not new product in the list of products"
