#coding:utf-8
import sys
from selenium import webdriver

sys.path.append("../")
from public_model import ecshop_login
#声明全局变量
user=[]
passwd=[]
user_file=open('../../data/login.txt','r')
lines = user_file.readlines()
for line in lines:
            username = line.split(',')[0] #使用“，”进行分割线，获取逗号前一个参数
            password = line.split(',')[1] #使用“，”进行分割线，获取逗号后一个参数
            a=username.strip('\t\n')  #将获取到的数组，存在\t\r\n 删除掉
            b=password.strip('\t\n')
            user.append(a)  #user数组中添加参数
            passwd.append(b)

#zip对数组中元素配对
list(zip(user,passwd))

#传入用户名及密码参数，并循环执行
class LoginTest1():
    def test_admin_login1(self):
            for (text,pwd) in zip(user,passwd):
                        driver=webdriver.Chrome()
                        driver.implicitly_wait(10)
                        driver.get("http://localhost:8081/ecshop/admin/index.php")
                        ecshop_login.login().user_login(driver, text, pwd)

#调用方法执行
LoginTest1().test_admin_login1()







