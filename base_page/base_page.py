''''
    基类：pom体系下的底层代码，用于封装各类行为操作，便于页面对象类进行调用。
         核心是关键字驱动的设计理念。
'''
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


# 基类
class BasePage:
    # 定义常规的测试操作行为
    # 创建构造函数，用于初始化self.driver对象,driver对象可能是任意一种浏览器对象
    def __init__(self, driver):
        self.driver = driver
        # 隐式等待
        self.driver.implicitly_wait(10)

    # 访问url
    def visit(self, text):
        self.driver.get(text)

    # 关闭浏览器driver释放资源
    def quit(self):
        self.driver.quit()

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 输入
    def input(self, loc, text):
        self.locator(loc).send_keys(text)

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 强制等待
    def sleep(self, text):
        sleep(text)

    # 显示等待
    def wait(self, loc):
        WebDriverWait(self.driver, 10, 0.1).until(lambda el: self.driver.find_element(*loc),
                                                  message='等待失败')

    # 句柄的切换：包含关闭原页面
    def handle_close(self):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 句柄的切换：不包含关闭原页面
    def handle(self, text=1):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[text])

    # 切换frame
    def switch_frame(self, text):
        self.driver.switch_to.frame(text)

    # 获取元素文本
    def get_text(self, loc):
        return self.locator(loc).text

    # 获取属性值
    def get_attribute(self, loc, text):
        return self.locator(loc).get_attribute(text)

    # 文本断言
    def assert_text(self, loc, expect):
        try:
            reality = self.locator(loc).text
            assert reality == expect, '断言失败'
            return True
        except Exception:
            self.log.exception('出现异常，断言失败：{0}!={1}'.format(expect, reality))
            return False

    # 属性断言
    def assert_attr(self, loc, txt, expect):
        try:
            reality = self.locator(loc).get_attribute(txt)
            assert reality == expect, '断言失败'
            return True
        except Exception:
            self.log.exception('出现异常，断言失败：{0}!={1}'.format(expect, reality))
            return False

    # 清除文本框内容
    def clear(self, loc):
        self.locator(loc).clear()

    # 清除文本框内容并输入新值
    def clear_input(self, loc, text):
        el = self.locator(loc)
        el.clear()
        el.send_keys(text)
