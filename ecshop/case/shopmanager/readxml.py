from xml.dom import minidom
#打开xml文档
dom=minidom.parse('../../data/a.xml')
from selenium import webdriver
from case.public_model import ecshop_login

#获得所有标签名
logins=dom.getElementsByTagName('login')

#获得login 标签中的username属性值
username=logins[0].getAttribute("username")
print("login 标签中的username属性值 %r" %username)
password=logins[0].getAttribute("password")
print("login 标签中的password属性值 %r" %password)

#获得标签对之间的数据,文本信息
citys=dom.getElementsByTagName('city')

#获得第二列city 标签对的值
c2=citys[0].firstChild.data
print("第二列city 标签对的值 %r" %c2)
class LoginTest1():
    def test_admin_login1(self):
                        driver=webdriver.Chrome()
                        driver.implicitly_wait(10)
                        driver.get("http://localhost:8081/ecshop/admin/index.php")
                        ecshop_login.login().user_login(driver, username, password)

LoginTest1().test_admin_login1()
