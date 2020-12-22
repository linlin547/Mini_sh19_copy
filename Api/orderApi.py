import requests
from Utils import app


class OrderApi:

    def __init__(self):
        # 商品分类
        self.create_order_url = app.host_url + "/order"
        # 分类下商品
        self.query_order_url = app.host_url + "/order/{}"
        # 商品详情
        self.user_order_url = app.host_url + "/order/by_user"

    def create_api(self):
        data = {"products": [{"product_id": 8, "count": 1}]}

        return requests.post(self.create_order_url, json=data, headers=app.header)

    def query_api(self, order_id=50):
        return requests.get(self.query_order_url.format(order_id), headers=app.header)

    def user_api(self, page=1):
        data = {"page": page}
        return requests.get(self.user_order_url, headers=app.header, params=data)
