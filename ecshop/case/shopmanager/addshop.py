#coding:utf-8
import sys

from selenium import webdriver

sys.path.append("../")
from ecshop.case.public_model import ecshop_login


class LoginTest():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8081/ecshop/admin/index.php")

#admin用户登录
    def test_admin_login(self):
        username='admin'
        password='test1234'
        ecshop_login.login().user_login(self.driver, username, password)
        ecshop_login.login().user_logout(self.driver)

#普通用户登录

    def test_guest_login(self):
        username='tl'
        password='123'
        ecshop_login.login().user_login(self.driver, username, password)
        ecshop_login.login().user_logout(self.driver)

LoginTest().test_admin_login()
LoginTest().test_guest_login()



