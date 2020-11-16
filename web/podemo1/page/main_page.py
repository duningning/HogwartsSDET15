from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from web.podemo1.page.add_memeber_page import AddMemberPage
from web.podemo1.page.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class MainPage(BasePage):#继承父类的话，会先调用父类的方法
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    #     self.driver.implicitly_wait(5)

    def goto_addmember(self):
        '''直接在首页点击添加成员'''
        # # self.driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]')
        # #self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        # self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        # return AddMemberPage(self.driver)

        '''点击联系人，再点击添加联系人按钮'''
        #self.driver.find_element(By.CSS_SELECTOR,'.menu_contacts').click()
        self.find(By.CSS_SELECTOR,'#menu_contacts').click()

        '''显式等待的应用'''
        #self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
        locator = (By.CSS_SELECTOR,'.js_has_member>div:nth-child(1)>a:nth-child(2)')
        # #element:WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # element = self.wait_for_click(locator,timeout)
        # element.click()

        #自己定义的方法
        def wait_for_next(x:WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID,'username')
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)