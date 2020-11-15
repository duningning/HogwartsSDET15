from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:

    def __init__(self,driver:WebDriver):
        self.driver =driver

    #注册信息
    def registerpage(self):
        self.driver.find_element(By.ID,'corp_name').send_keys('dnn')
        self.driver.find_element(By.ID,'manager_name').send_keys('')
