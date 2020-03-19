from selenium.webdriver.support.ui import *
class Webdriver():
    def click(self,driver,objectname,objectvalue):
        'objectname value have name/id/xobjectvalue/class;webdriver is the driver you use'
        if objectvalue=='':
            print( 'you must input the xpath')
        else:
            if objectname=='Id' or objectname=='id':#根据控件元素的ID属性定位元素，速度最快
                print( 'the objectname you useing is Id')
                elem=driver.find_element_by_id(objectvalue)
                elem.click()
            elif objectname=='name' or objectname=='Name':#根据控件元素的name属性定位元素，速度次之
                elem=driver.find_element_by_name(objectvalue)
                elem.click()
            elif objectname=='class' or objectname=='Class':#根据控件元素的class属性定位元素，速度稍慢
                elem=driver.find_element_by_class_name(objectvalue)
                elem.click()
            elif objectname=='xpath' or objectname=='Xpath':#通过xpath方式定位元素，速度最慢
                elem=driver.find_element_by_xpath(objectvalue)
                elem.click()
    def text_input(self,driver,method='Id',path='',key=''):
        'method value have name/id/xpath/class;driver is the driver you use'
        if path=='':
            print( 'you must input the xpath')
        else:
            if method=='Id' or method=='id':#根据控件元素的ID属性定位元素，速度最快
                print( 'the method you useing is Id')
                elem=driver.find_element_by_id(path)
                elem.clear()
                elem.send_keys(key)
            elif method=='name' or method=='Name':#根据控件元素的name属性定位元素，速度次之
                elem=driver.find_element_by_name(path)
                elem.clear()
                elem.send_keys(key)
            elif method=='class' or method=='Class':#根据控件元素的class属性定位元素，速度稍慢
                elem=driver.find_element_by_class_name(path)
                elem.clear()
                elem.send_keys(key)
            elif method=='xpath' or method=='Xpath':#通过xpath方式定位元素，速度最慢
                elem=driver.find_element_by_xpath(path)
                #elem.clear()
                elem.send_keys(key)
    def select_text(self,driver,method='Id',path='',key=''):
        'method value have name/id/xpath/class;driver is the driver you use'
        if path=='':
            print( 'you must input the xpath')
        else:
            if method=='Id' or method=='id':#根据控件元素的ID属性定位元素，速度最快
                print( 'the method you useing is Id')
                elem=Select(driver.find_element_by_name(path))
                elem.select_by_visible_text(key)
            elif method=='name' or method=='Name':#根据控件元素的name属性定位元素，速度次之
                elem=Select(driver.find_element_by_name(path))
                elem.select_by_visible_text(key)
            elif method=='class' or method=='Class':#根据控件元素的class属性定位元素，速度稍慢
                elem=Select(driver.find_element_by_name(path))
                elem.select_by_visible_text(key)
            elif method=='xpath' or method=='Xpath':#通过xpath方式定位元素，速度最慢
                elem=Select(driver.find_element_by_name(path))
                elem.select_by_visible_text(key)
    def frame(self,driver,objectvalue):
         return driver.switch_to.frame(objectvalue)