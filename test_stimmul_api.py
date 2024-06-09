from PartnerAuthApi import PartnerAuthApi
from ProductProviderApi import ProductProviderApi
from UserAuthApi import UserAuthApi
from ProductsApi import ProductsApi
from CartApi import CartApi


base_url = 'https://api.dev.opt.sarawan.ru/api'

partner_auth_api = PartnerAuthApi(base_url)
product_provider_api = ProductProviderApi(base_url)
user_auth_api = UserAuthApi(base_url)
products_api = ProductsApi(base_url)
cart_api = CartApi(base_url)

email = "zaytceva.jula@gmail.com"
inn = "5675432167"
password = "11111111"

phone = "+79991112233"
code = "1111"


def test_partner_add_product():
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


def test_add_product_to_cart():
    sms = user_auth_api.get_test_auth_sms(phone)
    assert sms["success"] is True, "SMS code doesn't get"

    verify_sms = user_auth_api.verify_sms_code(phone, code)
    assert verify_sms["success"] is True, "SMS code doesn't verify"
    user_token = verify_sms["token"]

    products = products_api.get_products()
    assert len(products["results"]) > 0, "Products list doesn't get"
    product_id = products["results"][1]["id"]
    quantity = products["results"][1]["unit_quantity"]

    add_product_to_cart = cart_api.add_product_to_cart(user_token, product_id,
                                                       quantity)
    assert add_product_to_cart["product"]["id"] == product_id, \
        "Product id in the cart is not equal"

    cart = cart_api.get_cart(user_token)
    is_product_in_cart = False
    for product in cart["products"]:
        if product["product"]["id"] == product_id:
            is_product_in_cart = True
    assert is_product_in_cart, "There is not product in the cart"
