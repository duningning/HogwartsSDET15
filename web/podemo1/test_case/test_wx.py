from web.podemo1.page.main_page import MainPage


class TestWX:
    def setup(self):
        self.main = MainPage()

    def test_addmember(self):
        #添加联系人
        # self.main.goto_addmember().add_member()
        #验证添加联系人无异常
        #assert  self.main.goto_addmember().add_member()
        username = "霍格沃兹21x"
        account = "aaaaaah_hogwarts21"
        phonenum = "13430000007"

        addmember = self.main.goto_addmember()
        #addmember.add_member()
        addmember.add_member(username, account, phonenum)
        #断言
        assert username in addmember.get_member(username)