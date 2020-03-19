#coding:utf-8
from selenium import webdriver
import unittest
from ecshop.case.public_model import ecshop_login

class TestCount(unittest.TestCase):
    #执行用例前执行
        def setUp(self):
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get("http://199.169.1.12:8081/ecshop/admin")
    #admin用户登录
        def test_htt(self):
            username='admin'
            password='test1234'
            ecshop_login.login().user_login(self.driver, username, password)
            title=self.driver.title
            self.assertEqual(title,"ECSHOP 管理中心",msg="没有登录成功")
            try:
                value1=self.driver.find_element_by_css_selector("frame#main-frame")
                self.driver.switch_to.frame(value1)
                self.driver.find_element_by_link_text("添加新商品")
            except Exception:
                return False
            return True


    #普通用户登录
        # def test_guest(self):
        #     username='tl'
        #     password='123'
        #     ecshop_login.login().user_login(self.driver, username, password)
    #执行用例后执行
        def tearDown(self):
            ecshop_login.login().user_logout(self.driver)
#unittest提供了全局的main()方法，使用它可以方便地将一个单元测试模块可以变成直接运行的测试脚本
#__name__作为模块的内置属性，可以直接.py调用执行，如果等于__main__直接可以执行
if __name__ == '__main__':
    unittest.main()
# #构造测试用例集
#     suite=unittest.TestSuite()
#     suite.addTest(TestCount("test_htt"))
#     suite.addTest(TestCount("test_guest"))
#     # #执行测试用例集
#     runner=unittest.TextTestRunner()
#     runner.run(suite)




