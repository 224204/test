#coding: utf-8
from selenium import webdriver
from time import *

driver=webdriver.Chrome()
driver.get("http://localhost:8081/ecshop/admin/index.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("test1234")
driver.find_element_by_xpath("//input[@value='进入管理中心']").click()
sleep(5)
#跳进frame框架
driver.switch_to.frame(driver.find_element_by_css_selector("frame#menu-frame"))
driver.find_element_by_xpath("//div[@id='menu-list']//a[text()='商品列表']").click()
#跳出frame
driver.switch_to.default_content()
#重新进入另一个框架
driver.switch_to.frame(driver.find_element_by_css_selector("frame#main-frame"))
sleep(5)
#通过xpath找到type=checkbox的元素
checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
#打印当前页面上type为checkbox的个数
print(len(checkboxes))
#全选
driver.find_elements_by_xpath("//input[@type='checkbox']").pop(0).click()
#获取到的input元素过滤type为checkbox的元素，单击勾选
for i in checkboxes:
    i.click()
    sleep(1)
sleep(5)
#把页面上的最后一个checkbox的钩去掉
driver.find_elements_by_xpath("//input[@type='checkbox']").pop().click()
#跳出farme框架
driver.switch_to.default_content()
#退出浏览器
#driver.quit()
