import requests
from Utils import app


class UserApi:

    def __init__(self):
        # 商品分类
        self.token_url = app.host_url + "/token/user"
        # 分类下商品
        self.verify_url = app.host_url + "/token/verify"
        # 商品详情
        self.address_url = app.host_url + "/address"

    def token_api(self):
        data = {"code": app.code}

        return requests.post(self.token_url, json=data, headers=app.header)

    def verify_api(self):
        data = {"token": app.header.get("token")}
        return requests.post(self.verify_url, json=data, headers=app.header)

    def address_api(self):
        return requests.get(self.address_url, headers=app.header)
