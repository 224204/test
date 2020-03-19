# coding=utf-8
'''
Created on 2016-8-13
@author: Jennifer
Project:使用unittest框架编写测试用例。
'''
import unittest
import sys
sys.path.append("../public_model")

from case.public_model.login import LoginPage
from selenium import webdriver

class Caselog(unittest.TestCase):
    """
          登录
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url ="http://localhost:8081/ecshop/admin/index.php"
        self.username ="admin"
        self.password ="test1234"

    #用例执行体
    def test_login_mail(self):
        #声明LoginPage类对象
        login_page =self.driver.get(self.url)
        #调用用户名输入
        login_page.input_username(self.username)
        #调用密码输入
        login_page.input_password(self.password)
        #调用点击登录按钮
        login_page.click_submit()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()