#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ess
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
url="http://localhost:8081/ecshop/admin/index.php"
driver.get(url)
locate=(By.NAME,'username')
try:
     WebDriverWait(driver,10).until(ess.presence_of_element_located(locate))
except Exception:
     print("找不到该元素信息")
else:
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("test1234")
