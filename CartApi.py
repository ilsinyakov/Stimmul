import requests


class CartApi:
    def __init__(self, url):
        self.url = url

    def add_product_to_cart(self, token, product_id, quantity):
        my_headers = {}
        my_headers["Authorization"] = f'Token {token}'

        body = {
            "product": product_id,
            "quantity": quantity
        }
        resp = requests.post(f'{self.url}/cart/', headers=my_headers,
                             json=body)
        return resp.json()

    def get_cart(self, token):
        my_headers = {}
        my_headers["Authorization"] = f'Token {token}'
        resp = requests.get(f'{self.url}/cart/', headers=my_headers)
        return resp.json()
