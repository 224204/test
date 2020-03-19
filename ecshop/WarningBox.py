#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from time import *

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

sleep(3)
#模拟鼠标悬浮
link=driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

driver.find_element_by_link_text("搜索设置").click()
sleep(3)

driver.find_element_by_class_name("prefpanelgo").click()
#以下为windows弹框,不能操作
#点击弹框确定按钮
#driver.switch_to.alert().accept()

#获得弹窗中的文本信息
#text=driver.switch_to.alert()
#text.text
sleep(3)


