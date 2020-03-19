import unittest
from ecshop.case.shopmanager.unittestshop import TestCount

#构造测试用例集
suite=unittest.TestSuite()
suite.addTest(TestCount("test_htt"))
suite.addTest(TestCount("test_guest"))

#执行用例
if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    runner.run(suite)

