from Api.apiFactory import ApiFactory
import unittest
from Utils.auto_assert import auto
from Utils import app


class TestUser(unittest.TestCase):
    def test_1token(self):
        # 数据-状态码
        category_code = 200
        # 数据-长度
        category_length = 0
        # 请求
        res = ApiFactory.get_user().token_api()
        # 断言
        auto(self, res.status_code, category_code)
        auto(self, len(res.json().get("token")), category_length, tag="more")
        # 存储token
        app.header["token"] = res.json().get("token")
        print("app:{}".format(app.header))

    def test_verify(self):
        # 数据-状态码
        category_code = 200
        # 数据-长度
        category_length = True
        res = ApiFactory.get_user().verify_api()
        auto(self, res.status_code, category_code)
        auto(self, res.json().get("isValid"), category_length)

    def test_address(self):
        name = "李白"
        mobile = "13012345678"
        res = ApiFactory.get_user().address_api()
        print("add:{}".format(res.json()))

        auto(self, res.json().get("name"), name)
        auto(self, res.json().get("mobile"), mobile)


