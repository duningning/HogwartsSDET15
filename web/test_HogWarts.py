
from selenium import webdriver

class TestHogwards():
    def setup(self):
        self.driver = webdriver.Chrome()#启动浏览器
        self.driver.maximize_window() #窗口最大化
        self.driver.implicitly_wait(10)#等待
    def teardown(self):
        #self.driver.quit()#执行完用例退出，回复初始化
        pass
    def test_hogwards(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.find_element_by_link_text("最新").click()#定位元素并操作
        self.driver.find_element_by_link_text('欢迎光临霍格沃兹测试学院 | Powered by 霍格沃兹测试学院').click()#定位元素并操作




