#coding:utf-8
#Coding=utf-8
#登录自动化测试
from selenium import webdriver
from time import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("http://127.0.0.1/zentao/my")
driver.find_element_by_name("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("submit").click()
sleep(3)
driver.get_screenshot_as_file("D:\\ecshop_jpg")
driver.find_element_by_link_text("项目").click()
driver.find_element_by_xpath("//a[contains(text(),'添加项目')]").click()
#driver.find_element_by_id("submit").click()
#js="window.scrollTo(0,document.body.scrollHeight);"
js="window.scrollTo(0,2000)"
driver.execute_script(js)
sleep(5)
driver.find_element_by_id("submit").click()
driver.get_screenshot_as_png("D:\\ecshop_jpg")
driver.quit()