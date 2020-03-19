import unittest
from ecshop.case.shopmanager.callmethod import *
from ecshop.case.shopmanager.modifyshop import *
from ecshop.case.shopmanager.unittestshop import *
from HTMLTestRunner import HTMLTestRunner
import time

#构造测试用例集
suite=unittest.TestSuite()
suite.addTest(Caselog("test_login"))
suite.addTest(delshop("del_shop"))


if __name__ == '__main__':
    #按照一定格式获取当前时间
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    #定义报告存放路径
    filename='../../Report/'+now+'result.html'
    path=open(filename,'wb')
    #定义测试报告，stream：生成的报告路径，title：报告标题，description：报告的副标题
    runner=HTMLTestRunner(stream=path,
                          title='ecshop测试报告',
                          description='用例执行情况')
        #执行测试
    #runner=unittest.TextTestRunner()
    runner.run(suite)
    #关闭报告文件
    path.close()
