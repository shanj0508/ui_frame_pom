'''
    测试用例类：所有的测试代码都在该类实现
'''
import unittest

from ddt import ddt, file_data
from selenium import webdriver

from page_object.cart_page import CartPage
from page_object.login_page import LoginPage
from page_object.phon_product_page import PhonePage


@ddt
class AddCartCase(unittest.TestCase):
    # 前置条件
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.pp = PhonePage(cls.driver)
        cls.cp = CartPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 登录
    @file_data('../data/login.yaml')
    def test_01_login(self, user, pwd):
        self.lp.login(user, pwd)

    # 添加商品
    @file_data('../data/add_cart.yaml')
    def test_02_add_cart(self, count):
        self.pp.add_cart(count)

    # 购物车校验
    def test_03_assert_cart(self):
        self.cp.cart_info()


if __name__ == '__main__':
    unittest.main()
