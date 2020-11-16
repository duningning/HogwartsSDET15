from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from web.podemo1.page.add_memeber_page import AddMemberPage


class MainPage:
    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def goto_addmember(self):
        #点击添加成员
       # self.driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]')
        self.driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)