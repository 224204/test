#coding: utf-8
from selenium import webdriver
from time import *

driver=webdriver.Chrome()
driver.get("http://localhost:8081/ecshop/admin/index.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("test1234")
driver.find_element_by_xpath("//input[@value='进入管理中心']").click()
sleep(5)
#获得ecshop首页窗口句柄
ecshop_home=driver.current_window_handle
#跳进frame框架
driver.switch_to.frame("header-frame")
driver.find_element_by_link_text("查看网店").click()
#跳出frame
driver.switch_to.default_content()
'''方法一：直接通过计算窗口第几个'''
'''
#进入网店窗口
driver.switch_to.window(driver.window_handles[1])
sleep(5)
#方法二：通过判断进入，首先在进入网店窗口前先获取ecshop首页的窗口句柄会话
#获得当前所有打开的窗口的句柄
'''
all_handles=driver.window_handles

#进入网店窗口

for handle in all_handles:
    if handle != ecshop_home:
        driver.switch_to.window(handle)

#回到ecshop窗口

#网店窗口按分类查找商品
driver.find_element_by_id("keyword").send_keys("手机")
sleep(5)
driver.find_element_by_name("imageField").click()
#退出浏览器
driver.quit()
