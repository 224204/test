# coding=utf-8
import unittest,random,string
from ecshop.case.public_model.common import *
from selenium import webdriver
from time import sleep
from ecshop.case.shopmanager.callmethod import num
from selenium.webdriver.common.action_chains import ActionChains

class delshop(unittest.TestCase):
    """
          登录
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost:8081/ecshop/admin/index.php")
        self.username ="admin"
        self.password ="test1234"

    #用例执行体
    def del_shop(self):
        Webdriver().text_input(self.driver, method="name", path='username', key='admin')
        Webdriver().text_input(self.driver, method="name", path='password', key='test1234')
        Webdriver().click(self.driver, 'xpath', "//input[@value='进入管理中心']")
        sleep(3)
        value=self.driver.find_element_by_css_selector('frame#menu-frame')
        print(value)
        Webdriver().frame(self.driver,value)
        Webdriver().click(self.driver, 'xpath', "//div[@id='menu-list']//a[text()='商品列表']")
        self.driver.switch_to.default_content()
        value1=self.driver.find_element_by_css_selector("frame#main-frame")
        Webdriver().frame(self.driver,value1)
        Webdriver().text_input(self.driver, method="name", path='keyword', key=num)
        Webdriver().click(self.driver, 'xpath', "//input[@value=' 搜索 ']")
        double_click=self.driver.find_element_by_xpath("//*[@id='listDiv']/table[1]/tbody/tr[3]/td[3]/span")
        ActionChains.double_click(double_click).perform()
        #self.driver.find_element_by_xpath("//*[@id='listDiv']/table[1]/tbody/tr[3]/td[3]/span").send_keys("123456")
        #Webdriver().text_input(self.driver, method="xpath", path="//*[@id='listDiv']/table[1]/tbody/tr[3]/td[3]/span",key='123456')
        Webdriver().click(self.driver, 'name', "keyword")
        text=self.driver.find_element_by_xpath("//*[@id='listDiv']/table[1]/tbody/tr[3]/td[3]/span").text
        print(text)
        self.assertEqual('123456',text,msg="不相等")
        self.driver.switch_to.default_content()

    #执行结束
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()