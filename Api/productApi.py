import requests
from Utils import app


class ProductApi:

    def __init__(self):
        # 商品分类
        self.category_url = app.host_url + "/category/all"
        # 分类下商品
        self.product_url = app.host_url + "/product/by_category"
        # 商品详情
        self.product_detail_url = app.host_url + "/product/{}"

    def category(self):
        """
        分类
        :return:
        """
        return requests.get(self.category_url)

    def product(self, category_id=2):
        """
        分类下商品
        :param category_id:分类id
        :return:
        """
        data = {"id": category_id}
        return requests.get(self.product_url, params=data)

    def product_detail(self, product_id=2):
        """
        商品详情
        :param product_id: 商品id
        :return:
        """
        return requests.get(self.product_detail_url.format(product_id))
