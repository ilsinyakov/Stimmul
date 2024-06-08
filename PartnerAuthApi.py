import requests


class PartnerAuthApi:
    def __init__(self, url):
        self.url = url

    def get_partner_auth_token(self, email, inn, password):
        body = {
            "email": email,
            "inn": inn,
            "password": password
        }
        resp = requests.post(f'{self.url}/partner/auth-token/', json=body)
        return resp.json()
