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
value=driver.find_element_by_css_selector("frame#menu-frame")
print(value)
value=driver.find_element_by_css_selector("frame#menu-frame")
driver.switch_to.frame(driver.find_element_by_css_selector("frame#menu-frame"))
driver.find_element_by_xpath("//div[@id='menu-list']//a[text()='商品列表']").click()
#跳出frame
driver.switch_to.default_content()
#重新进入另一个框架
driver.switch_to.frame(driver.find_element_by_css_selector("frame#main-frame"))
sleep(5)



#选择页面上的所有标签为input的元素
inputs=driver.find_elements_by_tag_name("input")
print(len(inputs))
#获取到的input元素过滤type为checkbox的元素，单击勾选
for i in inputs:
    if i.get_attribute("type") == "checkbox":
        i.click()
        sleep(1)
sleep(5)
#跳出
driver.switch_to.default_content()
#退出浏览器
driver.quit()
