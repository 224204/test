import csv
from selenium import webdriver
from public_model import ecshop_login

file=[]
data = csv.reader(open('../../data/login_file.csv','r'))
#循环读取本地csv 文件并添加至全局的数组中

for lines in data:
    file.append(lines)
print(file)

print(file[0])


#循环打印每一行的值，并传参登录
class login():
    def test_admin_login1(self,a,b):
        for i in range(1,len(file)):
              word=file[i]
              print(word)
              driver=webdriver.Chrome()
              driver.implicitly_wait(10)
              driver.get("http://localhost:8081/ecshop/admin/index.php")
              a=file[i][0]
              print(a)
              b=file[i][1]
              print(b)
              ecshop_login.login().user_login(driver, a, b)

login().test_admin_login1()



#获取某单元格的值,第一个下标为：行，第二个下标为列
#a=file[1][0]
#print(a)
#获取用户密码，数组的下标以0开始，密码位于数组的第二列，所以指密码的下标为[1]

#for line in data:
   # print(line[0])

#循环打印每一行的值

#b=(len(file))
'''
i=0
while(i < b):
    print('this is'+str(i)+'row----'+ str(file[i]))
    print(file[i])
    i += 1
'''




