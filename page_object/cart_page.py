'''
    CartPage：购物车页面，校验商品是否添加成功
'''
from base_page.base_page import BasePage
from my_conf.contants import default_url


# 购物车页面
class CartPage(BasePage):
    # url
    url = default_url + '?s=/index/cart/index.html'
    # 关键元素
    goods = ('xpath', '//div[@class="goods-base"]')
    goods_counts_attr = ('value')

    # 行为:校验商品是否存在
    def cart_info(self):
        self.visit(self.url)
        self.sleep(1)
        self.wait(self.goods)
