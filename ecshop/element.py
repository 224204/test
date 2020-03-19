#coding:utf-8
from selenium import webdriver
from time import *
from public import login

driver1 = webdriver.Chrome()
login().user_login(driver1)
sleep(5)

'''
#获得输入框的尺寸
size1=driver.find_element_by_name("username").size
print("用户名输入框尺寸大小：%r" %size1)
#获得元素的属性值（id,name,type,.....）
attribute=driver.find_element_by_xpath("(//table//input)[1]").get_attribute("name")
print("用户名输入框name属性的值：%r" %attribute)
#查看元素是否可见
result = driver.find_element_by_xpath("(//table//input)[1]").is_displayed()
print("用户名输入框是否可见：%r" %result)

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("test1234")
driver.find_element_by_xpath("//input[@value='进入管理中心']").click()
sleep(5)
'''

driver1.switch_to.frame(driver1.find_element_by_css_selector("frame#menu-frame"))
#获取元素的文本信息
text=driver1.find_element_by_xpath("(//div[@id='menu-list']//a)[1]").text
print("获得链接的文本信息：%s" %text)

login().user_logout(driver1)




