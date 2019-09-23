import random
import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

brower = webdriver.Firefox()
brower.implicitly_wait(2)

# 打开网页
brower.get("https://magicube.moredian.com/#/login")

# 登陆
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
print("1、登陆成功")

# 跳转我的机构
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/i[2]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()

# 确认是否满机构
try:
    # brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[15]/td[1]/div').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[15]/td[1]/div')
    print("15个机构已满")

except selenium.common.exceptions.NoSuchElementException:
    #新增机构
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').click()
    # num = range(1,99999999)
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/input').send_keys(random.randint(100000,999999))
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/span').click()
    brower.find_element_by_xpath('//*[@id="search-input"]').click()
    brower.find_element_by_xpath('//*[@id="search-input"]').send_keys("北京")
    try:
        element = WebDriverWait(brower, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="amap-sug1"]')))
    finally:
        brower.find_element_by_xpath('//*[@id="amap-sug1"]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div/div[1]/ul/li[1]/div[1]').click()
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]').click()   # 保存地址
    time.sleep(2)
    # brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[1]').click() # 创建机构
    brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[3]/div/div[2]').click()
except Exception as e:
    print(e)

# print(flag)
