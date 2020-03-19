#coding: utf-8
from selenium import webdriver
from time import *
import os

driver=webdriver.Chrome()
driver.get("http://localhost:8081/ecshop/admin/index.php")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("test1234")
driver.find_element_by_xpath("//input[@value='进入管理中心']").click()
sleep(3)
#跳进frame框架
driver.switch_to.frame(driver.find_element_by_css_selector("frame#menu-frame"))
driver.find_element_by_link_text("添加新商品").click()
#跳出frame
driver.switch_to.default_content()
#重新进入另一个框架
driver.switch_to.frame(driver.find_element_by_css_selector("frame#main-frame"))
#单击打开上传窗口
driver.find_element_by_xpath("//input[@name='goods_img']").click()
sleep(5)
#调用upload.exe上传程序
os.system("D:\\software_install\\automation\\upload.exe")
#点击确定
driver.find_element_by_xpath("//input[@value=' 确定 ']").click()
#跳出frame
#执行js拖动滚动条水平位置
#js="window.scrollTo(0,450)"
#driver.execute_script(js)
#执行js拖动滚动条垂直位置
#js="window.scrollTop(0,450)"
#driver.execute_script(js)
driver.switch_to.default_content()
#driver.quit()