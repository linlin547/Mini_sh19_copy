from Api.homeApi import HomeApi
import unittest
from Utils.auto_assert import auto
from Utils.data import Data
from parameterized import parameterized


def home_data():
    # # banner
    # banner_list = []
    # # theme
    # theme_list = []
    # # new_product
    # new_product_list = []
    # value = Data.get_json_data("home.json")

    banner_list = Data.get_json_data("home.json", "banner",
                                     ["banner_code", "banner_id", "banner_name", "banner_length"])
    theme_list = Data.get_json_data("home.json", "theme",
                                    ["ids", "theme_code", "theme_dis", "theme_length_url", "theme_name"])
    new_product_list = Data.get_json_data("home.json", "new_product",
                                          ["new_code", "new_length", "new_keys"])
    # for x in value.get("banner"):
    #     banner_list.append((x.get("banner_code"), x.get("banner_id"),
    #                         x.get("banner_name"), x.get("banner_length")))
    # for y in value.get("theme"):
    #     theme_list.append((y.get("ids"), y.get("theme_code"),
    #                        y.get("theme_dis"), y.get("theme_length_url"),
    #                        y.get("theme_name")))
    # for z in value.get("new_product"):
    #     new_product_list.append((z.get("new_code"), z.get("new_length"),
    #                              z.get("new_keys")))
    return {"banner": banner_list, "theme": theme_list, "new": new_product_list}


class TestHome(unittest.TestCase):
    @parameterized.expand(home_data().get("banner"))
    def test_banner(self, banner_code, banner_id, banner_name, banner_length):
        print("banner_code:{}".format(banner_code))
        print("banner_id:{}".format(banner_id))
        print("banner_name:{}".format(banner_name))
        print("banner_length:{}".format(banner_length))
        # 请求
        res = HomeApi().banner()
        # 断言 -状态码
        auto(self, res.status_code, banner_code)
        # 断言 id
        auto(self, res.json().get("id"), banner_id)
        # 断言 name
        auto(self, res.json().get("name"), banner_name)
        # 断言items长度大于0
        auto(self, len(res.json().get("items")), banner_length, tag="more")
        # 断言图片utl不为空
        auto(self, len(res.json().get("items")[0].get("img").get("url")), banner_length, tag="more")

    @parameterized.expand(home_data().get("theme"))
    def test_theme(self, ids, theme_code, theme_ids, theme_length_url, theme_name):
        print("ids:{}".format(ids))
        print("theme_code:{}".format(theme_code))
        print("theme_ids:{}".format(theme_ids))
        print("theme_length_url:{}".format(theme_length_url))
        print("theme_name:{}".format(theme_name))
        # 请求
        res = HomeApi().theme(ids)
        # 断言 -状态码
        auto(self, res.status_code, theme_code)
        # 断言 -id=1 id=2 id =3
        for i in theme_ids:
            auto(self, i, res.text, tag="in")
        # 断言 长度
        auto(self, len(res.json()), theme_length_url, tag="more")
        # 断言 -name
        auto(self, res.json()[0].get("name"), theme_name)
        # 断言 -url
        auto(self, len(res.json()[0].get("topic_img").get("url")), theme_length_url, tag="more")

    @parameterized.expand(home_data().get("new"))
    def test_new_product(self, new_code, new_length, new_keys):
        print("new_code:{}".format(new_code))
        print("new_length:{}".format(new_length))
        print("new_keys:{}".format(new_keys))
        # 请求
        res = HomeApi().new_product()
        # 断言 -状态码
        auto(self, res.status_code, new_code)
        # 断言 - 长度
        auto(self, len(res.json()), new_length, tag="more")
        # 断言 -关键字段
        for i in new_keys:
            auto(self, i, res.text, tag="in")
