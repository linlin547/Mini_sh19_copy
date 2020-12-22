from Api.homeApi import HomeApi
from Api.productApi import ProductApi
from Api.userApi import UserApi
from Api.orderApi import OrderApi


class ApiFactory:
    @staticmethod
    def get_home():
        return HomeApi()

    @staticmethod
    def get_product():
        return ProductApi()

    @staticmethod
    def get_user():
        return UserApi()

    @staticmethod
    def get_order():
        return OrderApi()
