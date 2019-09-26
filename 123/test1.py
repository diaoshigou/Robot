import random
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


brower = webdriver.Firefox()
brower.implicitly_wait(3)

# 打开网页
brower.get("https://magicube.moredian.com/#/login")

# 登陆
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
print("1、登陆成功")

# 选择机构
sleep(2)
brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/div/div/span[3]/i[1]').click()
brower.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[7]').click()

# 进入魔点门禁
# brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[10]/td[5]/div/div[1]').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()

