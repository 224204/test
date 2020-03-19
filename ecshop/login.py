#coding: utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import *
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://localhost:8081/ecshop/admin")
driver.set_window_size(400,800)

driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("username").send_keys(Keys.SPACE)
sleep(3)
driver.find_element_by_name("username").send_keys("admin")
sleep(5)
'''
driver.find_element_by_name("password").send_keys("test1234")
driver.find_element_by_xpath("//input[@value='进入管理中心']").click()
title=driver.title
print("页面标题：%r" %title)
url=driver.current_url
print("url:%r" %url)
'''




'''
driver.find_element_by_name("goods_name").clear()
driver.find_element_by_name("goods_name").send_keys("admin")
driver.find_element_by_name("goods_name").click()




print("设置浏览器宽480、高800显示")
driver.set_window_size(480,800)

print("设置浏览器全屏")
driver.maximize_window()
#driver.switch_to.frame("header-frame")
#driver.find_element_by_link_text("商品列表").click()
#driver.switch_to.default_content()
sleep(5)
driver.switch_to.frame(driver.find_element_by_css_selector("frame#menu-frame"))
driver.find_element_by_link_text("添加新商品").click()
driver.switch_to.default_content()
#重新进入另一个框架
driver.switch_to.frame(driver.find_element_by_css_selector("frame#main-frame"))
sleep(5)
#下拉第几个进行选择
Select(driver.find_element_by_name("cat_id")).select_by_index(1)
#option value值选择
Select(driver.find_element_by_name("cat_id")).select_by_value("1")
#下拉选择文本信息选择
Select(driver.find_element_by_name("cat_id")).select_by_visible_text("手机")

#driver.quit()
'''