from Api.apiFactory import ApiFactory
from Utils import app

# 轮播图
# print("轮播图:{}".format(HomeApi().banner().json()))
#
# # 专题栏
# print("专题栏:{}".format(HomeApi().theme().json()))
#
# # 最近新品
# print("最近新品:{}".format(HomeApi().new_product().json()))

# print("分类:{}".format(ApiFactory.get_product().category().json()))
# print("分类下商品:{}".format(ApiFactory.get_product().product().json()))
# print("商品详情:{}".format(ApiFactory.get_product().product_detail().json()))
# res = ApiFactory.get_user().token_api().json()
# print("token:{}".format(res))
# app.header["token"] = res.get("token")
# print("app:{}".format(app.header))
#
# print("verify:{}".format(ApiFactory.get_user().verify_api().json()))
#
# print("address:{}".format(ApiFactory.get_user().address_api().json()))

print("下单:{}".format(ApiFactory.get_order().create_api().json()))
print("查询订单:{}".format(ApiFactory.get_order().query_api().json()))
print("用户订单:{}".format(ApiFactory.get_order().user_api().json()))
