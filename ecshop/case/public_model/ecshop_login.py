#coding:utf-8
#新增登录模块

class login():
    def user_login(self,driver,username,password):
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//input[@value='进入管理中心']").click()

    def user_logout(self,driver):
        driver.quit()


'''
class login():
    def user_login(self,driver):
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("test1234")
        driver.find_element_by_xpath("//input[@value='进入管理中心']").click()

    def user_logout(self,driver):
        driver.quit()
'''

