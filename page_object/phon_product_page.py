'''
    手机商品详情页：PhonePage，主要显示手机的商品详情内容，用于执行对应的操作行为。
'''
from selenium import webdriver

from base_page.base_page import BasePage
from my_conf.contants import default_url

# 手机商品详情页



class PhonePage(BasePage):
    '''
        页面对象类的模板：
            1.url
            2.关键元素
            3.行为
    '''
    # url
    url = default_url + '?s=/index/goods/index/id/2.html'

    # 关键元素
    suite = ('xpath', '//li[@data-value="套餐一"]')
    color = ('xpath', '//li[@data-value="金色"]')
    memory = ('xpath', '//li[@data-value="128G"]')
    count_input = ('id', 'text_box')
    add_cart_button = ('xpath', '//button[@title="加入购物车"]')

    # 行为:添加购物车
    def add_cart(self, count):
        # 访问登录页
        self.visit(self.url)
        # 选择商品属性
        self.click(self.suite)
        self.sleep(1)
        self.click(self.color)
        self.sleep(1)
        self.click(self.memory)
        self.sleep(1)
        self.clear_input(self.count_input, count)
        # 点击加入购物车按钮
        self.click(self.add_cart_button)


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    count = '4'
    pp = PhonePage(driver)
    pp.add_cart(count)
