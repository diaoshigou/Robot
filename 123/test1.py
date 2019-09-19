import selenium
from selenium import webdriver
import time


brower = webdriver.Firefox()
brower.implicitly_wait(3)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




# 打开网页
brower.get("https://magicube.moredian.com/#/login")
# driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
# time.sleep(2)#等待网页加载
# 登陆
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
print("1、登陆成功")
# time.sleep(2)

# 跳转我的机构
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/i[2]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()

# 确认是否满机构
try:
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[15]/td[1]/div')
    print("15个机构已满")
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/span').click()
    if brower.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div[2]/span').text == "所在机构数量达到上限":
        brower.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/span').click()
except selenium.common.exceptions.NoSuchElementException:
    brower.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/span').click()

# print(flag)
