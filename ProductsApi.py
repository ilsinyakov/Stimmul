import requests


class ProductsApi:
    def __init__(self, url):
        self.url = url

    def get_products(self):
        resp = requests.get(f'{self.url}/products/')
        return resp.json()
