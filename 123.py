from selenium import webdriver
import time

brower = webdriver.Firefox()
brower.get("http://www.baidu.com")

brower.find_element_by_id('kw').send_keys('selenium')
brower.find_element_by_id('su').click()

time.sleep(3)
brower.close()