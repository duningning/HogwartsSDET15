from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
#登陆页
from web.podemo.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver:WebDriver):#通过init接受上一个页面的driver，确保能够继续使用
        self.driver =driver
    #扫码
    def scan(self):
        pass

    #进入到注册页
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click() #dirver传过来识别不了类型，所以需要在__init__指定一个driver类型
        return RegisterPage(self.driver)