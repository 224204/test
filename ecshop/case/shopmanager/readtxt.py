from selenium import webdriver
import os
#sys.path.append("../")
from case.public_model import ecshop_login
from time import sleep
'''
class readtxt():
    def readtxt(self,user,pwd):
        user_file=open(user,'r')
        user1=user_file.readlines()
        pwd_file=open(pwd,'r')
        pwd1=pwd_file.readlines()
        list(zip(user1,pwd1))
        for (x,y) in zip(user1,pwd1):
            driver=webdriver.Chrome()
            url="http://localhost:8081/ecshop/admin/index.php"
            driver.get(url)
            ecshop_login.login().user_login(driver,x,y)

user='../../data/user.txt'
pwd='../../data/pwd.txt'
readtxt().readtxt(user,pwd)
'''
pwd=open('../../data/pwd.txt','r')
print(pwd.readlines())
pwd=open('../../data/user.txt','r')
print(pwd.readlines())

'''
class login():
    def readtxt(self,username,password):
        user_file=open(username,'r')
        user1=user_file.readlines()
        name=user1.strip('\t\r\n')
        pwd_file=open(password,'r')
        pwd=pwd_file.readlines()
        pwd1=pwd.strip('\t\r\n')
        #list(zip(user1,pwd))
        for a in user1:
            for b in pwd:
                driver=webdriver.Chrome()
                url="http://localhost:8081/ecshop/admin/index.php"
                driver.get(url)
                ecshop_login.login().user_login(driver,a,b)

login().readtxt('../../data/user.txt','../../data/pwd.txt')
'''



