'''
    LoginPage：登录页，只为系统的登录业务而生成的页面对象。
'''
from selenium import webdriver

from base_page.base_page import BasePage
from my_conf.contants import default_url

# 登录页



class LoginPage(BasePage):
    '''
        页面对象类的模板：
            1.url
            2.关键元素
            3.行为
    '''
    # url
    url = default_url + '?s=/index/user/logininfo.html'

    # 关键元素
    username = ('name', 'accounts')
    password = ('name', 'pwd')
    login_button = ('xpath', '//button[text()="登录"]')

    # 行为
    def login(self, user, pwd):
        # 访问登录页
        self.visit(self.url)
        # 输入账号和密码
        self.input(self.username, user)
        self.input(self.password, pwd)
        # 点击登录按钮，实现登录操作
        self.click(self.login_button)


# 调试
if __name__ == '__main__':
    driver = webdriver.Chrome()
    user = 'shanjing'
    pwd = 'shanjing@.000'
    lp = LoginPage(driver)
    lp.login(user, pwd)
