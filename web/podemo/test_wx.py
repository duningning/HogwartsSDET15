from web.podemo.index_page import IndexPage


class TestWX:
    def setup(self):
        #拿到入口index的配置
        self.index = IndexPage()


    def test_register(self):
        #调用index中方法从登陆页跳转注册页完成注册
        #assert self.index.goto_login().goto_register().register()

        #首页直接跳转注册页，完成注册
        assert True == self.index.goto_register().register()
        #下面这种断言方式同理
        #assert self.index.goto_register().register()