from Api.apiFactory import ApiFactory
import unittest
from Utils.auto_assert import auto


class TestOrder(unittest.TestCase):
    def test_create(self):
        # 数据-状态码
        order_code = 200
        # 数据-pass
        order_pass = True
        # 数据-长度
        order_length = 0
        # 请求
        res = ApiFactory.get_order().create_api()
        # 断言
        auto(self, res.status_code, order_code)
        auto(self, len(res.json().get("order_no")), order_length, tag="more")
        auto(self, len(res.json().get("order_id")), order_length, tag="more")
        auto(self, res.json().get("pass"), order_pass)

    def test_query(self):
        # 数据-状态码
        order_code = 200
        # 数据-id
        order_id = 50
        # 数据-no
        order_no = "CB15039906369944"
        # 数据-total_price
        order_total_price = '0.03'
        res = ApiFactory.get_order().query_api(order_id)
        auto(self, res.status_code, order_code)
        auto(self, res.json().get("id"), order_id)
        auto(self, res.json().get("order_no"), order_no)
        auto(self, res.json().get("total_price"), order_total_price)

    def test_user(self):
        current_page = 1
        order_length = 0

        res = ApiFactory.get_order().user_api(current_page)

        auto(self, res.json().get("current_page"), current_page)
        auto(self, len(res.json().get("data")), order_length,"more")
