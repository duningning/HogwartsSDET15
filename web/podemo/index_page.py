from selenium import webdriver

from selenium.webdriver.common.by import By
#首页
from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):#实例化driver
        self.driver =webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        #点击登录
        #使用css_selector定位，元素前面要加 . 否则可能定位不到，无法执行通过
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        #跳转登录页面
        return LoginPage(self.driver)#把dirver传到loginpage页面
    def goto_register(self):
        #点击注册
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)

