

#基类：最基本的方法，driver 实例化，find()等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    #driver:WebDriver
    #base_url配置想要打开的页面
    base_url = ''

    def __init__(self,driver:WebDriver = None):
        '''解决driver传递和复用问题'''
        '''用例第一次实例化MainPage()的时候，会创建一个driver,当完成页面切换的时候，会传递driver，实现driver的复用'''
        if driver == None:
            #第一次初始化
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            #进行页面跳转的操作
            self.driver = driver

        if self.base_url !="":
            self.driver.get(self.base_url)

    '''封装find方法'''
    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)
    '''封装显式等待'''
    def wait_for_click(self,locator,timeout = 10):
        element:WebElement = WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))
        return element
