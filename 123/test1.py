import random
from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

brower = webdriver.Firefox()
brower.implicitly_wait(3)

# 打开网页
brower.get("https://magicube.moredian.com/#/login")

# 登陆
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md1234567890')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
print("1、登陆成功")

sleep(2)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/span[3]/i[1]').click()

brower.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[7]').click()

brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[1]').click()  # 跳转魔点门禁


# 报警记录
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[1]/div/div[2]/div[1]/div[4]/a').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/input').click()  # 点击选择开始日期
brower.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/button[1]').click()   # 往后退一年
brower.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[2]/td[1]/div/span').click() # 当月页面第一天
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[3]/div[1]/table/tr[1]/td[1]/div').click()   # 确认报警记录能被筛选
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/span[3]/i[1]').click() # 点击选择报警类型
brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[4]').click()   # 选择非法移动设备
sleep(0.5)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div/div/span[3]/i[1]').click() # 点击选择报警类型
brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[1]').click()   # 选择全部报警类型
sleep(0.5)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[3]/div[1]/table/tr[1]/td[1]/div').click()   # 确认还有报警记录被成功筛选
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div/div/span[3]/i[1]').click() # 点击选择报警设备
brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[2]').click()   # 选择第一个设备
sleep(0.5)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div[3]/div/div[2]/div/div/span[3]/i[1]').click()
brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[1]').click()   # 切换回全部设备
sleep(0.5)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[3]/div[1]/table/tr[1]/td[1]/div').click()   # 确认记录能被成功筛选
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/div[2]/div/div/span[3]/i[1]').click()   # 点击选择分页逻辑
brower.find_element_by_xpath('/html/body/div[4]/div[1]/ul/li[1]').click()   # 选择5条/页
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/div[7]').click()   # 选择第三页
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/div[3]/i').click()  # 前进一页
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[3]/div/div/div[14]/input').click()   # 聚焦页码跳转搜索框
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[3]/div[1]/table/tr[1]/td[1]/div').click()   # 确认元素的存在
