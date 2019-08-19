from selenium import webdriver
import time
import unittest


try:
    driver.find_element_by_xpath("xxx x").is_displayed()
except:
    print("未找到元素")
else:
    print("元素存在")