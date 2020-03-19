# coding=utf-8
import unittest,random,string
from ecshop.case.public_model.common import *
from selenium import webdriver
from time import sleep
num=random.randint(10000,99999)
print(num)
class Caselog(unittest.TestCase):
    """
          登录
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://199.169.1.12:8081/ecshop/admin")
        self.username ="admin"
        self.password ="test1234"

    #用例执行体
    def test_login_mail(self):
        Webdriver().text_input(self.driver, method="name", path='username', key='admin')
        Webdriver().text_input(self.driver, method="name", path='password', key='test1234')
        Webdriver().click(self.driver, 'xpath', "//input[@value='进入管理中心']")
        sleep(3)
        value=self.driver.find_element_by_css_selector('frame#menu-frame')
        print(value)
        Webdriver().frame(self.driver,value)
        Webdriver().click(self.driver, 'xpath', "//div[@id='menu-list']//a[text()='添加新商品']")
        element=self.driver.find_element_by_link_text("添加新商品")
        if element.is_displayed():
            print("可见")
        self.driver.switch_to.default_content()
        sleep(3)
        value1=self.driver.find_element_by_css_selector("frame#main-frame")
        Webdriver().frame(self.driver,value1)
        # num=random.choice('1234567890')
        # print(num)
        # sleep(3)
        Webdriver().text_input(self.driver, method="name", path="goods_name", key="test2356")
        #多个字符中，选择特定3个字符
        #num= random.sample('abcdefghijklmnopqrstuvwxyz123456789',3)
        #print(num)
        Webdriver().text_input(self.driver, method="name", path="goods_sn", key=num)
        text=self.driver.find_element_by_name("goods_sn").text
        print(text)
        Webdriver().select_text(self.driver, method="name", path="cat_id", key="手机")
        Webdriver().select_text(self.driver, method="name", path="brand_id", key="小米")
        Webdriver().text_input(self.driver, method="xpath", path="//input[@name='shop_price']", key="1999")
        Webdriver().click(self.driver, 'xpath', "//input[@value=' 确定 ']")
        #self.assertEqual(text,num,msg="不相等")
        self.driver.switch_to.default_content()
    #执行结束
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()