from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
#注册页

class RegisterPage:

    def __init__(self,driver:WebDriver):#注解功能，指定driver类型,方便书写代码规范
        self.driver = driver

    #注册信息
    def register(self):
        self.driver.find_element(By.ID,'corp_name').send_keys('dnn')
        self.driver.find_element(By.ID,'manager_name').send_keys('dnn01')
        self.driver.find_element(By.ID,'register_tel').send_keys('13271433391')
        self.driver.find_element(By.ID,'submit_btn').click()
        return True

