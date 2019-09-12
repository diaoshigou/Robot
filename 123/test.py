from selenium import webdriver
import time

brower = webdriver.Firefox()
# brower.get("http://www.baidu.com")
#
# brower.find_element_by_id('kw').send_keys('selenium')
# brower.find_element_by_id('su').click()
brower.get("https://magicube.moredian.com/#/login")
time.sleep(2)
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()

time.sleep(2)
brower.close()
