from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.podemo1.page.base_page import BasePage


class AddMemberPage(BasePage):

    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    #添加联系人
    def add_member(self,username,account,phonenum):
        # username = 'dnn'
        # account = '123'
        # phonenum = '13271400000'
        # self.driver.find_element(By.ID,'username').send_keys(username)
        # self.driver.find_element(By.ID,'memberAdd_acctid').send_keys(account)
        # self.driver.find_element(By.ID,'memberAdd_phone').send_keys(phonenum)
        # self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        self.find(By.ID,'username').send_keys(username)
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        self.find(By.ID,'memberAdd_phone').send_keys(phonenum)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()

        #判断点击后的下一个页面有没有正常加载出来
        checkbox = (By.CSS_SELECTOR, '.ww_checkbox')
        self.wait_for_click(checkbox)
        return True

    #验证联系人添加成功
    def get_member(self,value):
        # #contactlist = self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # contactlist = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        # #find_elements找到对应的元素就会生成一个列表，找不到就返回一个空列表
        # '''第一种方法，遍历contactlist列表，将遍历出来的用户名都放啊titlelist列表中去'''
        # # titlelist = []
        # # for element in contactlist:
        # #     titlelist.append(element.get_attribute('title'))
        # '''第二种方法和第一种一样，是另一种写作方式'''
        # titlelist = [element.get_attribute('title') for element in contactlist]
        # print(titlelist)
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                return value
            total_list = total_list + titlelist

            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list