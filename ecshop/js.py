from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
'''
file_path='file:///'+os.path.abspath('D:/shimei/web/js.html')
driver.get(file_path)
driver.switch_to.alert().accept()
'''

driver.get("http://127.0.0.1/zentao/my")
driver.find_element_by_name("account").send_keys("admin")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_id("submit").click()
sleep(3)
driver.find_element_by_link_text("测试").click()
driver.find_element_by_link_text("用例").click()
driver.find_element_by_xpath("//a[contains(text(),'导入')]").click()
#driver.switch_to.alert().accept()
sleep(5)
#driver.find_element_by_xpath("(//button[@class='close'])[2]").click()
driver.switch_to.frame("modalIframe")
sleep(6)
driver.find_element_by_name("file").click()




