from Utils.HTMLTestRunner import HTMLTestRunner
from Scripts.test_home import TestHome
from Scripts.test_order import TestOrder
from Scripts.test_product import TestProduct
from Scripts.test_user import TestUser
import unittest

# 测试套件
suite = unittest.TestSuite()
# suite_list = [TestUser, TestHome, TestProduct, TestOrder]
suite_list = [TestHome]

# 添加测试类
for i in suite_list:
    suite.addTest(unittest.makeSuite(i))
# 报告文件
report_path = "./report.html"

# 编写报告
with open(report_path, "wb") as f:
    runner = HTMLTestRunner(f, title="小程序", description="v1.1")
    runner.run(suite)
