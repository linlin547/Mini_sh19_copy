from Api.apiFactory import ApiFactory
import unittest
from Utils.auto_assert import auto


class TestProduct(unittest.TestCase):

    def test_category(self):
        # 数据-状态码
        category_code = 200
        # 数据-长度
        category_length = 0
        # 请求
        res = ApiFactory.get_product().category()
        # 断言
        auto(self, res.status_code, category_code)
