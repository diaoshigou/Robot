import unittest
from selenium import webdriver
import time

class LearnElement(unittest.TestCase):
    #初始化，打开浏览器
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://www.baidu.com')

    def testXpath(self):
        #定位百度首页的输入框，绝对路径定位成功
        element = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/span/input')
        #定位百度首页的输入框，相对路径
        element = self.driver.find_element_by_xpath("//input[@id='kw']")
        #定位百度首页的输入框，相对路径下的布尔逻辑运算
        element=self.driver.find_element_by_xpath("//input[@id='kw'and @name='wd']")
        element.send_keys('http://wsbm.sdzk.cn')
        time.sleep(5)

    #--------关闭浏览器------------
    #def tearDown(self):
     #   self.driver.quit()

if __name__ == '__main__':
    unittest.main()