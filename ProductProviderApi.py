import requests


class ProductProviderApi:
    def __init__(self, url):
        self.url = url

    def get_products(self, token):
        my_headers = {}
        my_headers["Authorization"] = f'Token {token}'
        resp = requests.get(f'{self.url}/product_provider/',
                            headers=my_headers)
        return resp.json()

    def create_new_product(self, token, new_product_data):
        my_headers = {}
        my_headers["Authorization"] = f'Token {token}'
        body = new_product_data
        resp = requests.post(f'{self.url}/product_provider/',
                             headers=my_headers, json=body)
        return resp.json()
