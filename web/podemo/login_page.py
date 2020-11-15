from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver =driver
    #扫码
    def scan(self):
        pass
    #进入到注册页
    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'login_registerBar_link')#dirver传过来识别不了类型，所以需要在__init__指定一个driver类型
        return RegisterPage()