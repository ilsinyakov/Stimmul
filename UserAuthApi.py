import requests


class UserAuthApi:
    def __init__(self, url):
        self.url = url

    def get_test_auth_sms(self, phone):
        body = {
            "phone": phone
        }
        resp = requests.post(f'{self.url}/user/test-auth-sms/', json=body)
        return resp.json()

    def verify_sms_code(self, phone, code):
        body = {
            "phone": phone,
            "code": code
        }
        resp = requests.post(f'{self.url}/user/verify-code/', json=body)
        return resp.json()
