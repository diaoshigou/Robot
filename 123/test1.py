from selenium import webdriver
import time

brower = webdriver.Firefox()

#打开网页
brower.get("https://magicube.moredian.com/#/login")
time.sleep(2)#等待网页加载
#登陆
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[3]/div/div[2]/div/input').send_keys('18368387155')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[4]/div/div[2]/div/input').send_keys('Md123456')
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div[5]/div').click()
time.sleep(2)
print("1、登陆成功")

#跳转我的机构
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]').click()
brower.find_element_by_xpath('/html/body/div[3]/ul/li[3]').click()
time.sleep(3)

#搜索机构
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/input').send_keys("+——-=")
time.sleep(1)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/i').click()
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div/span[2]')    #无相关记录
time.sleep(1)
brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/i').click()    #清除搜索内容
time.sleep(1)
# brower.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/table/tr[1]/td[5]/div/div[3]').click()

