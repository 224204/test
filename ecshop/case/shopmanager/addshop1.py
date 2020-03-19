#coding:utf-8
import sys
from selenium import webdriver

sys.path.append("../")
from public_model import ecshop_login

#参数化搜索关键字
username = ['admin','admin1','admin2']
password = ['test1234','test','123']
#内置的zip函数可以让我们使用for循环来并行使用多个序列。在基本运算中，
#zip会取得一个或多个序列为参数，然后返回元组的列表，将这些序列中的并排的元素配成对
list(zip(username,password))

#存在多个数组，通过遍历循环执行，传入的参数没有配成对来执行，所以以下方法不太实用
'''
class LoginTest():
    def test_admin_login(self):
            for text in username:
                for pwd in password:
                        driver=webdriver.Chrome()
                        driver.implicitly_wait(10)
                        driver.get("http://localhost:8081/ecshop/admin/index.php")
                        ecshop_login.login().user_login(driver, text, pwd)


'''
#通过zip将元组配成对，则for循环元组执行
class LoginTest1():
    def test_admin_login1(self):
            for (text,pwd) in zip(username,password):
                        driver=webdriver.Chrome()
                        driver.implicitly_wait(10)
                        driver.get("http://199.169.1.12:8081/ecshop/admin")
                        ecshop_login.login().user_login(driver, text, pwd)


LoginTest1().test_admin_login1()
