import csv
from selenium import webdriver
from ecshop.case.public_model import ecshop_login
file=[]
data = csv.reader(open('../../data/login_file.csv','r'))
#循环读取本地csv 文件并添加至全局的数组中
for lines in data:
    file.append(lines)
b=(len(file))
#获取某单元格的值#a=file[1][0]
#print(a)#获取用户密码，数组的下标以0开始，密码位于数组的第二列，所以指密码的下标为[1]
#for line in data:
#print(line[1])
#循环打印每一行的值
'''while(i < b):
print('this is'+str(i)+'row----'+ str(file[i]))
print(file[i])
i += 1
'''
#循环打印每一行的值，并传参登录
class login():
    def test_admin_login1(self):
        for i in range(1,len(file)):
            word=file[i]
            driver=webdriver.Chrome()
            driver.implicitly_wait(10)
            driver.get("http://localhost:8081/ecshop/admin/index.php")
            ecshop_login.login().user_login(driver, file[i][0], file[i][1])
login().test_admin_login1()
